import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyD1USS9gaxBcZechhtO8mbwmBbC2n-jhBM")
model=genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text,image_data,prompt):
    response=model.generate_content([input_text,image_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no files are uploaded")
    
st.set_page_config(page_title="sris invoce generator")
st.sidebar.header("robo bill")
st.sidebar.write("Made by Gowri")
st.sidebar.write("powered by generative ai")
st.header("Robo Bill")
st.subheader("made by Gowri")
st.subheader("manage your expenses with Robo Bill")
input = st.text_input("what do you want me to do?",key="input")
uploaded_file = st.file_uploader("choose an image from your gallery",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded image",use_column_width=True)

ssubmit=st.button("let's go!")

input_prompt = """
you are an expert in calculus.i am going to upload an image of a calculus question. you will solve it and give me the 
steps of the solution
"""
if ssubmit:
    image_data = input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("here's what you need to know")
    st.write(response)
  
