import streamlit as st
from PIL import Image, ImageDraw
import os

bad_word = "!@#$%^`~&*()_+=-,./?><[]{\\}"

# Function to generate the sign language GIF
def generate_sign_language_gif(input_text):
    # Folder containing sign language images (A to Z)
    image_folder = "sign_language_images"

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

    # Create a composite image of all the sign images
    composite_image = create_composite_image(images)

    return "sign_language.gif", image_filenames, composite_image

# Function to create a composite image from individual sign images
def create_composite_image(images):
    image_size = images[0].size
    composite_width = image_size[0] * len(images)
    composite_height = image_size[1]
    composite_image = Image.new("RGB", (composite_width, composite_height))

    # Paste individual sign images onto the composite image
    for i, img in enumerate(images):
        composite_image.paste(img, (i * image_size[0], 0))

    return composite_image

# Main Streamlit app code
def main():
    st.title("Fantastic Sign Language Generator 🤩")

    # Input text from the user
    input_text = st.text_input("Enter text:")
    
    if st.button("Generate"):
        if input_text:
            # Generate the sign language GIF and composite image
            gif_path, image_filenames, composite_image = generate_sign_language_gif(input_text)
            
            # Display the generated GIF
            st.image(gif_path, use_column_width=True, caption="Sign Language GIF")
            
            # Display all the sign language images in a grid
            st.subheader("Sign Language Images")
            
            # Define the image size
            image_size = (100, 100)
            
            # Determine the number of columns based on the available width
            num_columns = st.columns(6)  # You can adjust the number of columns here
            
            for i, image_filename in enumerate(image_filenames):
                image = Image.open(image_filename)
                
                # Display images in a grid
                with num_columns[i % len(num_columns)]:
                    st.image(image, caption=f"Sign Image {i}", width=image_size[0])
                
if __name__ == "__main__":
    main()
