from PIL import Image
import requests
from io import BytesIO
import streamlit as st
from openai import OpenAI


st.title('Generate images using DALL·E')
api_key = st.text_input("Enter your OpenAI API key:", type="password")
model_choice = st.selectbox(
   "Which Dall E model would you like to use? ",
   ("DALL·E 3", "DALL·E 2"),
   index=None,
   placeholder="Select DALL·E model",
)

st.write('You selected:', model_choice)

if model_choice == "DALL·E 3":
  model_choice = "dall-e-3"
else:
  model_choice = "dall-e-2"


prompt = st.text_input("Enter a prompt:")

client = OpenAI(
  api_key= api_key
)

# Define the submit button
if st.button("Generate Image"):
  # create the image generation request
  response = client.images.generate(
    model=model_choice,
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1
  )
  image_url = response.data[0].url
  print("Generated Image URL:", image_url)

  response = requests.get(image_url)
  img = Image.open(BytesIO(response.content))

  # Display the image
  st.image(img)



