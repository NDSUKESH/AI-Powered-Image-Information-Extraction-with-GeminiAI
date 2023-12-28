### loading the .env file where the key is present
##load_dotenv is present inside my main.py file in library so i imported like this. 
from dotenv import main
main.load_dotenv()


##importing necessasy libraries
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai



##importing the model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vision')


##function to get the response from the model
def get_data(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text



def image_process(uploaded_file):
    if uploaded_file is not None:

        bytes_date=uploaded_file.getvalue()
        image_parts =[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_date
            }
        ]         
        return image_parts
    else :
        raise FileNotFoundError("Check the file is uploade properly")



st.set_page_config(page_title="Image Information Extraction using GeminiAI",page_icon="📑")



##getting input from the user
input=st.text_input("Input Promt:",key="input",)
uploaded_file=st.file_uploader("Choose an image....📑",type=["jpg","jpeg","png"])
image=""


if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image,use_column_width=True")
submit=st.button("RUN")


input_prompt="""
You are an expert in analysing the image.User will upload the any kind of image and will ask the questions 
about the images you need to answer the questions from the image alone and you can also find the faces in the image
and tell their name if you have the information
"""


if submit:
    image_data=image_process(uploaded_file)
    reponse=get_data(input_prompt,image_data,input)
    st.subheader("The Details is")
    st.markdown(reponse)
