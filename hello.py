from PIL import Image
import pandas as pd
import numpy as np

import pickle

import streamlit as st
import plotly.express as px

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

heart_train_df=pd.read_csv('train.csv')
heart_train_df.drop(columns=['id'], inplace=True)

image_2 = Image.open('healthy_heart.jpg')
st.image(image_2, caption='Healthy Heart')

st.write(heart_train_df.sample(15))

genre = st.radio(
    "What's your favorite movie genre",
    [":blue[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

'''
st.write('Hello, World!')
x = st.text_input('Favourite team? ')
st.write(f'Your favourite team is: {x}')

st.button('Click me!')
st.slider('Select a value', 0, 100, 50)


data = pd.read_csv('test.csv')
sample_data = data.sample(15)
st.write(sample_data)

st.bar_chart(sample_data['Age'])
st.line_chart(sample_data['Cholesterol'])
st.area_chart(sample_data['Max HR']) 


image_2 = Image.open('healthy_heart.jpg')
st.image(image_2, caption='Heart Disease Prediction')

st.write('## BMI Calculator')

col1, col2, col3 = st.columns(3)

age = col1.number_input('Age', min_value=0, max_value=120, value=30)    
height = col2.number_input('Height (cm)', min_value=50, max_value=250, value=170)        
weight = col3.slider('Weight (kg)', min_value=0, max_value=300, value=70)        


bmi = weight / ((height / 100) ** 2)
col2.metric('BMI', f'{bmi:.2f} kg/m²')

st.video('heart_beat.mp4', start_time=0, loop=True, autoplay=True, muted=True)

def looping_video(video_url):
    video_html = f"""
        <video width="100%" height="auto" autoplay loop muted playsinline>
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    """
    st.components.v1.html(video_html, height=400)

st.title("Looping Video Example")
looping_video("https://www.w3schools.com/html/mov_bbb.mp4")

# streamlit run hello.py
'''