# styled_image_creator.py

import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from config import HF_API_KEY

def generate_image_from_text(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

def daylight_effect(image):
    # Brighten and soften the image
    image = ImageEnhance.Brightness(image).enhance(1.3)  # 30% brightness
    image = ImageEnhance.Contrast(image).enhance(1.1)    # 10% contrast
    image = image.filter(ImageFilter.GaussianBlur(radius=1))  # Soft blur
    return image

def night_mood_effect(image):
    # Increase contrast, reduce brightness slightly
    image = ImageEnhance.Brightness(image).enhance(0.9)  # 10% darker
    image = ImageEnhance.Contrast(image).enhance(1.4)    # 40% contrast boost
    image = image.filter(ImageFilter.GaussianBlur(radius=0.5))  # Very subtle blur
    return image

def main():
    print("Welcome to the AI Image Stylist Project!")
    prompt = input("Enter your image description:\n").strip()

    try:
        print("Generating your base image...\n")
        image = generate_image_from_text(prompt)

        print("Applying Daylight Edition style...")
        daylight_img = daylight_effect(image)
        daylight_img.show()
        daylight_img.save(f"{prompt.replace(' ', '_')}_daylight.png")
        print("Daylight Edition saved.\n")

        print("Applying Night Mood style...")
        night_img = night_mood_effect(image)
        night_img.show()
        night_img.save(f"{prompt.replace(' ', '_')}_night.png")
        print("Night Mood saved.\n")

    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
