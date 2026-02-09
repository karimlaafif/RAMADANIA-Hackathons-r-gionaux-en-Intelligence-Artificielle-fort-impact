
---

# SmartCivic Assistant | مساعد (Musa'id) 🇲🇦

**RAMADANIA Hackathon Submission: Digitalisation des Services Publics**

An AI-powered assistant designed to bridge the gap between Moroccan citizens and public administrations. By utilizing **RAG (Retrieval-Augmented Generation)**, the assistant provides accurate guidance on services like CIN, CNSS, and Minhaty in **Darija**, **Arabic**, and **French**.

---

## 🚀 Quick Start (Demo in 5 Mins)

Get the project running locally by following these steps:

1. **Clone the Repository**
2. **Initialize Environment**
```bash
python -m venv venv
source venv/bin/activate # Mac/Linux
# venv\Scripts\activate  # Windows

```


3. **Install Dependencies**
```bash
pip install -r requirements.txt

```


4. **Configure API Key**
* Rename `.env.example` to `.env`
* Add your `OPENAI_API_KEY`.
* *Note: If no key is provided, the system defaults to **Demo Mode** (Retrieval Only).*


5. **Launch Dashboard**
```bash
streamlit run app.py

```



---

## 🏗️ System Architecture

The MVP is built on a modular stack focused on local performance and high-quality retrieval:

| Component | Technology | Role |
| --- | --- | --- |
| **Frontend** | **Streamlit** | Mobile-responsive chat interface. |
| **Orchestrator** | **LangChain** | Manages the logic flow and RAG chain. |
| **Vector DB** | **ChromaDB** | Local storage for administrative knowledge. |
| **Embeddings** | **MiniLM-L6-v2** | Local/Free model for semantic search. |
| **LLM Layer** | **GPT-3.5** | Natural language synthesis (Darija/Arabic). |

---

## 🗺️ The Citizen Journey (User Flow)

1. **Access:** The user opens the web-based assistant.
2. **Language Selection:** User chooses their preferred tongue (e.g., **Darija**).
3. **Query:** User asks: *"Kifash njded la carte dyali?"*
4. **RAG Processing:** * System scans `data/cin.md` for official requirements.
* LLM simplifies technical jargon into conversational Darija.


5. **Outcome:** The assistant provides a checklist and the official link (cnie.ma).

---

## 💬 Conversation Examples

> **المواطن (الدارجة):** "Salam, bghit njded la carte nationale dyali, Shenou khassni?"
> **المساعد:** "Wa alaykum salam! Bash tjded la Carte Nationale, khassk: Shahada sokna, 2 tsawar sans lunettes, l'ancienne carte, w timbre dyal 75 DH. Nwerik kifash takhod rdv?"

> **المواطن (العربية):** "هل يمكنني التقديم لمنحة التعليم العالي الآن؟"
> **المساعد:** "نعم، عبر بوابة www.minhaty.ma. يجب ملء الاستمارة بالمعلومات الشخصية ومعلومات الوالدين قبل الموعد النهائي."

---

## 🌍 Social Impact & Goals

* **Inclusion (الشمولية):** Breaking language barriers for those who struggle with administrative French or Standard Arabic.
* **Efficiency (الفعالية):** Reducing physical crowds at administrative centers by providing clear "before-you-go" checklists.
* **Transparency (الشفافية):** Offering direct, standardized info on fees (e.g., the 75 DH stamp) to prevent misinformation.

---

## 📂 Project Structure

```text
├── data/               # Knowledge base (Markdown files)
├── app.py              # Streamlit UI & Frontend logic
├── utils.py            # RAG implementation & LangChain logic
├── requirements.txt    # Project dependencies
└── .env.example        # Template for API configuration

```

---



