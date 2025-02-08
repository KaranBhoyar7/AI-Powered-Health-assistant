import streamlit as st
import ollama
from typing import List, Dict

# Initialize the healthcare assistant
class HealthcareAssistant:
    def __init__(self, model_name: str = "llama3.2:3b"):
        self.model = model_name
        self.system_prompt = """You are a helpful AI Health Assistant. Your role is to provide:
        - General health information
        - Symptom analysis (with disclaimers)
        - Medication information
        - Healthy lifestyle tips
        - First aid guidance
        - Always maintain professional medical tone
        - Never diagnose or replace real doctors
        - Decline non-health related queries politely"""
        
    def generate_response(self, messages: List[Dict]) -> str:
        try:
            response = ollama.chat(
                model=self.model,
                messages=[{"role": "system", "content": self.system_prompt}] + messages,
                options={'temperature': 0.3}
            )
            return response['message']['content']
        except Exception as e:
            return f"Error generating response: {str(e)}"

# Initialize assistant
assistant = HealthcareAssistant(model_name="llama3.2:3b")

# Streamlit App Configuration
st.set_page_config(
    page_title="HealthAssist AI",
    page_icon="🏥",
    layout="centered"
)

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm HealthAssist AI. How can I help you with healthcare today?"}
    ]

# Sidebar with disclaimer
with st.sidebar:
    st.title("🏥 HealthAssist AI")
    st.markdown("""
    **Disclaimer**:  
    This AI assistant provides general health information and should not:
    - Replace professional medical advice
    - Be used for emergency situations
    - Be considered as a diagnosis tool
    """)
    st.divider()
    st.write("Model: Llama 3.2b (Healthcare Optimized)")

# Chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask your health-related question..."):
    # Check for non-health queries
    non_health_keywords = ["sport", "movie", "weather", "politics", "finance"]
    if any(keyword in prompt.lower() for keyword in non_health_keywords):
        response = "I specialize in healthcare only. Please ask medical or health-related questions."
    else:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Analyzing your health query..."):
                messages = st.session_state.messages[-5:]  # Keep last 5 messages
                response = assistant.generate_response(messages)
                st.markdown(response)
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})