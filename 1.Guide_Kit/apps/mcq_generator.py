import streamlit as st
import google.generativeai as genai

def mcq_generator(api_key):
    # Configure the Gemini API with the provided API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-pro-latest",
        system_instruction="""Generate multiple-choice questions based on the provided text. 
                              Ensure the questions are relevant and have plausible answer options."""
    )

    def generate_mcqs(text):
        response = model.generate_content(text)
        return response.text

    st.title("MCQ Generator")
    st.markdown(
        """
        Welcome to the MCQ Generator app! This app generates multiple-choice questions (MCQs) based on the provided text. 
        Simply enter your text in the text area below, and click the "Generate MCQs" button to generate MCQs.
        """
    )
    text = st.text_area("Enter your text here:", height=200)
    if st.button("Generate MCQs"):
        if text:
            st.info("Generating MCQs...")
            mcqs = generate_mcqs(text)
            st.success("MCQs generated successfully!")
            st.subheader("Generated MCQs:")
            st.write(mcqs)
        else:
            st.error("Please enter some text.")
