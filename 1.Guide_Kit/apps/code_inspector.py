import streamlit as st
import google.generativeai as genai

def code_inspector(api_key):
    # Configure the Gemini API with the provided API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-pro-latest",
        system_instruction="""You are acting as a code checker and coding instructor. 
                              Provide feedback and suggestions to enhance the quality of the given code snippet. Ensure the completion is informative and instructive."""
    )

    def check_code(code):
        response = model.generate_content(code)
        return response.text

    st.title("Code Inspector")
    st.markdown(
        """
        Welcome to the Code Inspector app! This app checks your code for errors 
        and provides suggestions for improvement. Simply enter your code in the text area below, 
        and click the "Check Code" button to see the corrected version.
        """
    )
    code = st.text_area("Enter your code here:", height=200)
    if st.button("Check Code"):
        if code:
            st.info("Checking code...")
            corrected_code = check_code(code)
            st.success("Code checked successfully!")
            st.subheader("Corrected code:")            
            st.write(corrected_code)
        else:
            st.error("Please enter some code.")