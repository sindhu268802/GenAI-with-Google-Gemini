from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini API And get response

def get_gemini_response(prompt, image=None):
    model = genai.GenerativeModel("gemini-2.5-flash")
    if image:
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content(prompt)
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return {
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize streamlit app

st.set_page_config(page_title="Gemini Nutrition App")

st.header("Gemini Nutrition App")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about my meal")

prompt= """
You are "Nutritionist Coacher", a personal AI dietician. 
The user will upload an image of foods. 
Your role is to:

1. Identify each food item clearly from the image.  
2. Estimate the approximate calories for each item (kcal).  
3. Provide the total calorie count for the whole plate/meal.  
4. Give a professional nutrition tip about the meal (is it balanced, high in carbs, too oily, etc.).  
5. Suggest a healthier alternative diet plan or modifications to make the meal more nutritious and balanced.  

"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(prompt,image_data)
    st.subheader("The Response is")
    st.write(response)

