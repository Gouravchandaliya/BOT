from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def my_output(query: str) -> str:
    response = model.generate_content(query)
    return response.text


#### UI development using streamlit

st.set_page_config(page_title = "FAAAHGPT")
st.header("Google Gemini Bot")
input_query = st.text_input("Enter your query here:")
if st.button("Generate Response"):
    if input_query:
        output = my_output(input_query)
        st.subheader("Response:")
        st.write(output)
    else:
        st.warning("Please enter a query to generate a response.")