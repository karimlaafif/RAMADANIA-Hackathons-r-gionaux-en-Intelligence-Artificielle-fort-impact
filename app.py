import streamlit as st
import time
from utils import SmartCivicRAG
import os

# Page Config
st.set_page_config(
    page_title="Musa'id - Smart Public Assistant",
    page_icon="🇲🇦",
    layout="centered"
)

# Custom CSS for styling (Ramadania Theme)
st.markdown("""
<style>
    .stChatInput {border-radius: 20px;}
    .reportview-container {background: #f0f2f6;}
    h1 {color: #2E86C1;}
    .stMarkdown {font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
</style>
""", unsafe_allow_html=True)

# Initialize RAG System (Cached)
@st.cache_resource
def get_rag_system():
    return SmartCivicRAG()

try:
    rag_system = get_rag_system()
except Exception as e:
    st.error(f"Error initializing AI engine: {e}")
    st.stop()

# Sidebar: Language & Settings
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2c/Flag_of_Morocco.svg", width=100)
    st.title("Settings / الإعدادات")
    
    language = st.radio(
        "Choose Language / اختر اللغة",
        ("Darija (Moroccan Arabic)", "Arabic (Standard)", "French", "English")
    )
    
    st.markdown("---")
    st.markdown("**About:**")
    st.markdown("This AI assistant helps you navigate Moroccan public services (CIN, CNSS, Minhaty).")
    st.markdown("*Built for Ramadania AI Hackathon.*")

# Main Content
st.title("🤖 Musa'id (مساعد)")
st.caption("Your Smart Companion for Public Procedures / رفيقك الذكي للإجراءات الإدارية")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Salam! Ana Musa'id. Bghiti chi m3loumat 3la CIN, CNSS, wla l'Minha? (Hello! How can I help you today?)"}
    ]

# Display Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Posez votre question / سولني هنا..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Thinking... / Jari lba7t..."):
            try:
                # Use the RAG system to get answer
                # Map selectbox to language string
                lang_code = language.split(" ")[0]
                response = rag_system.get_response(prompt, language=lang_code)
                
                # Stream the response (simulate typing)
                for chunk in response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)}"
                message_placeholder.markdown(error_msg)
                full_response = error_msg
                
    st.session_state.messages.append({"role": "assistant", "content": full_response})
