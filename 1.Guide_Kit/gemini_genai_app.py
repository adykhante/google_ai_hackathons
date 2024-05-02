import streamlit as st
import google.generativeai as genai
from apps.code_inspector import code_inspector
from apps.mcq_generator import mcq_generator
from apps.data_science_ai_tutor import data_science_ai_tutor

def main():
    st.sidebar.title('Tools')
    api_key = st.sidebar.text_input('Enter your Gemini API key', type='password')
    selected_program = st.sidebar.selectbox('Select a program', ['Code Inspector', 'MCQ Generator', 'Data Science AI Tutor'])

    # Configure the Gemini API with the provided API key
    genai.configure(api_key=api_key)

    if selected_program == 'Code Inspector':
        code_inspector(api_key)
    elif selected_program == 'MCQ Generator':
        mcq_generator(api_key)
    elif selected_program == 'Data Science AI Tutor':
        data_science_ai_tutor(api_key)

if __name__ == "__main__":
    main()
