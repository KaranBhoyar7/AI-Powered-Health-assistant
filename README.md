# AI-Powered Health Assistant 🏥  

This project is a Streamlit-based AI chatbot application designed to provide users with healthcare-related information. The assistant, powered by the LLaMA 3.2 model via Ollama, offers general health advice, symptom analysis, medication information, and healthy lifestyle tips in a conversational format.

---

## Features 🌟  
- **Healthcare Assistance:** Get answers to health-related queries, including general advice, symptom insights, and healthy living tips.
- **Contextual Conversations:** Maintains a conversation history to provide better contextual answers.
- **Streamlit UI:** A clean, interactive interface for user engagement.
- **Ethical Health Guidelines:** Polite refusal of non-health-related questions and no replacement for professional medical advice.

---

## Requirements 📋  
- **Python 3.8+**  
- **Required Libraries:**  
  - `streamlit`  
  - `ollama`  

---

## Prerequisites 📦  
Make sure you have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed on your system.  

Additionally, you need to install Ollama and download the `llama3.2:3b` model:  
- Install [Ollama](https://ollama.com/)  
- Download the llama3.2:3b model using:
  ```bash
  ollama pull llama3.2:3b

## Installation and Setup ⚙️
1. Clone the repository:
```bash
  git clone <repository-URL>
  cd <project-directory>
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run app.py
```
## Disclaimer ⚠️
This AI assistant is for educational purposes only and should:

- NOT replace professional medical advice.
- NOT be used in emergency situations.
- NOT provide any diagnosis.

## Future Enhancements 🚀
- Support for additional health data formats.
- UI/UX improvements for better user engagement.
- Enhanced query capabilities with multi-tool integration.
