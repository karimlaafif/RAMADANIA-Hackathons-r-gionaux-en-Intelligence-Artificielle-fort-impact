# Smart Public Services Assistant - RAMADANIA Hackathon Plan

## 1. Project Overview
**Name**: SmartCivic Assistant (Musa'id / مساعد)
**Theme**: Digitalisation des services publics
**Objective**: AI-powered assistant for citizens to navigate public services easily.

## 2. Core Features
- **Multilingual Support**: Arabic, Darija, French.
- **Service Guidance**: Step-by-step procedures for documents, deadlines, and fees.
- **Privacy-First**: No personal data storage; purely informational.
- **Accessible**: Simple language, voice-enabled option (if feasible).

## 3. System Architecture (MVP)

**Frontend (User Interface)**
- **Web App**: Simple Chat Interface built with Streamlit or React.
- **Components**: Input field (Text/Voice), Chat History, Language Toggle (AR/FR/Darija).

**Backend (API & Logic)**
- **Framework**: Python (FastAPI or Streamlit for rapid prototyping).
- **Orchestration**: LangChain or LlamaIndex.

**AI Engine**
- **LLM**: GPT-4o-mini or Local LLM (e.g., Qwen 2.5 7B via Ollama) for reasoning and translation.
- **Embeddings**: Multilingual embedding model (e.g., `text-embedding-3-small` or `huggingface/multilingual-e5`).
- **Vector Database**: ChromaDB (local) or FAISS for storing public service knowledge.

**Data Pipeline**
- **Source**: Scraped/Manual data from service-public.ma, cnss.ma, etc.
- **Format**: Structured Markdown/JSON (Service Name, Steps, Documents, Fees).

## 4. User Flow (Citizen Journey)
1.  **Landing**: User selects language (or AI auto-detects).
2.  **Query**: User asks "How do I renew my CIN?" (in Darija: "Kifash njded la carte dyali?").
3.  **Intent Detection**: AI identifies intent -> `Service: CIN_Renewal`.
4.  **Retrieval**: System fetches `CIN_Renewal` data from Vector DB.
5.  **Generation**: LLM generates a simple, step-by-step response in the user's language.
6.  **Follow-up**: User asks about fees/locations; AI responds with context.

## 5. Example Conversations

### A. Darija (CIN Renewal)
**User**: "Salam, bghit njded la carte nationale dyali, Shenou khassni?"
**Assistant**: "Wa alaykum salam! Bash tjded la Carte Nationale (CIN), khassk had lwraq:
1. Shahada dyal sokna (awla fatourat lma/do ila kant bmsgitek).
2. 2 tsawar shamsiya (jdad w b'arriere-plan byed).
3. L'ancienne carte nationale dyalk.
4. Wahed timbre dyal 75 DH.
*Bghiti nwerik fin tmeshi awla kifash takhod rdv?*"

### B. Arabic (Scholarship/Minhaty)
**User**: "هل يمكنني التقديم لمنحة التعليم العالي الآن؟"
**Assistant**: "نعم، يمكنك التقديم لمنحة 'منحتي' (Minhaty).
*الخطوات الأساسية:*
1. التسجيل عبر البوابة الإلكترونية: www.minhaty.ma.
2. ملء الاستمارة بالمعلومات الشخصية ومعلومات الوالدين.
3. آخر أجل للتسجيل عادة يكون في [Date].
*هل تريد معرفة الوثائق المطلوبة للملف الورقي؟*"

### C. French (CNSS Declaration)
**User**: "Comment déclarer un employé à la CNSS?"
**Assistant**: "Pour immatriculer un salarié à la CNSS, voici les étapes :
1. Remplir le formulaire 'Demande d'immatriculation' (Réf. 321-1-01).
2. Joindre une copie de la CIN du salarié.
3. Déposer le dossier à l'agence CNSS ou via le portail Damancom.
*Souhaitez-vous le lien pour télécharger le formulaire ?*"

## 6. Minimal Demo Scope (48h Hackathon)
- **Scope**: Focus on 3 key services to ensure quality.
    1.  **CIN (National ID)**
    2.  **CNSS (Social Security)**
    3.  **Minhaty (Scholarships)**
- **Tech Stack**: Streamlit (Frontend + Backend in one), OpenAI API/Ollama, ChromaDB.
- **Deliverable**: a working URL where judges can ask questions in Darija and get accurate answers.

## 7. Social Impact
- **Inclusion**: Breaks language barriers for Darija-only speakers.
- **Efficiency**: Reduces queues at administrative offices by ensuring citizens arrive with correct documents.
- **Empowerment**: Demystifies complex bureaucracy for the average citizen.
