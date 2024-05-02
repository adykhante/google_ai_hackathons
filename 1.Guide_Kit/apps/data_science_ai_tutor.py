import streamlit as st
import google.generativeai as genai

def data_science_ai_tutor(api_key):
    # Configuring the API Key
    genai.configure(api_key=api_key)
    # Initializing the gemini model
    model = genai.GenerativeModel(
        model_name='gemini-1.5-pro-latest',
        system_instruction=""" Welcome to DataScience AI Tutor! I'm here to guide you through your Data Science journey. Ask me anything about Data Science concepts, tools, or techniques, and I'll provide clear explanations and examples to help you learn and grow. If someone asks about your name, tell them your name is DataScience Tutor. Only provide information about Data Science topics. If you know the answer to a Data Science question, provide it. Otherwise, say "I don't know."If anyone asks a question not related to Data Science, say "I can only help you with Data Science related topics." """
)

    st.title('Data Science  AI Tutor')
    
    # If there is no chat_history in session, init one
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Init the chat object
    chat = model.start_chat(history=st.session_state['chat_history'])

    for msg in chat.history:
        st.chat_message(msg.role).write(msg.parts[0].text)

    user_prompt = st.chat_input()

    if user_prompt:
        st.chat_message('user').write(user_prompt)
        response = chat.send_message(user_prompt, stream=True)
        response.resolve()
        st.chat_message('ai').write(response.text)
        st.session_state['chat_history'] = chat.history

