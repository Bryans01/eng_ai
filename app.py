import openai
import requests
from PIL import Image
from io import BytesIO
import os


openai.api_key = os.getenv('OPENAI_API_KEY')


def enhance_drawing(input_image_path, output_image_path, prompt):
    # Read the image file from disk and resize it
    image = Image.open(input_image_path)
    width, height = 1024, 1024  # adjust size as needed
    image = image.resize((width, height))

    # Convert the image to a BytesIO object
    byte_stream = BytesIO()
    image.save(byte_stream, format='PNG')
    byte_array = byte_stream.getvalue()

    try:
        # Edit the image based on the prompt
        response = openai.Image.create_edit(
            image=byte_array,
            n=1,
            size="1024x1024",
            prompt=prompt
        )

        # Get the URL of the created image
        image_url = response['data'][0]['url']

        # Save the new image to the specified path
        with open(output_image_path, 'wb') as f:
            f.write(requests.get(image_url).content)
        print(f"Saved new image to {output_image_path}")
    except openai.error.OpenAIError as e:
        print(e.http_status)
        print(e.error)

# Call the function with the path to the input image, output image path, and a prompt
enhance_drawing('C:\\Stephen\\Coding\\Image 1\\PFD.png', 'C:\\Stephen\\Coding\\Image 1\\PFD_out.png', 'Change the design to improve efficiency and usability')

