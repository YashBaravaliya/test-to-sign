import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

bad_word = "!@#$%^`~&*()_+=-,./?><[]{\\}"

# Function to generate the sign language GIF
def generate_sign_language_gif(input_text):
    # Folder containing sign language images (a to z)
    image_folder = "sign_language_images"

    # Convert the input text to lowercase
    input_text = input_text.lower()

    # Split the input text into words
    words = input_text.split()

    # Create a list of image filenames for each letter in the input text
    image_filenames = []

    for letter in input_text:
        if letter in bad_word:
            continue
        elif " " in letter:
            letter = "space"
        image_filenames.append(os.path.join(image_folder, letter + ".jpeg"))

    # Create a GIF by combining the images
    images = [Image.open(filename) for filename in image_filenames]
    images[0].save("sign_language.gif", save_all=True, append_images=images[1:], duration=500)

    return "sign_language.gif"

# Main Streamlit app code
def main():
    st.title("Fantastic Sign Language Generator 🤩")

    # Input text from the user
    input_text = st.text_input("Enter text:")
    
    if st.button("Generate"):
        if input_text:
            # Generate the sign language GIF
            gif_path = generate_sign_language_gif(input_text)
            
            # Display the generated GIF
            st.image(gif_path, use_column_width=True, caption=f"{input_text} GIF")
            

if __name__ == "__main__":
    main()
