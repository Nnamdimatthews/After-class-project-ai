import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import io
import base64

# --- Gemini Setup ---
genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your actual key
text_model = genai.GenerativeModel("gemini-pro")
image_model = genai.GenerativeModel("gemini-pro-vision")

# --- Session State ---
if "tool" not in st.session_state:
    st.session_state.tool = "Text Assistant"
if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""
if "generated_image" not in st.session_state:
    st.session_state.generated_image = None

# --- Prompt Filtering ---
def is_prompt_safe(prompt):
    unsafe_keywords = ["blood", "violence", "weapon", "self-harm", "nudity"]
    return not any(word in prompt.lower() for word in unsafe_keywords)

# --- Gemini Text Response ---
def generate_text_response(prompt):
    response = text_model.generate_content(prompt)
    return response.text

# --- Gemini Image Generation ---
def generate_image_response(prompt):
    response = image_model.generate_content(prompt)
    image_part = next((part for part in response.parts if isinstance(part, types.Blob)), None)
    if image_part:
        return Image.open(io.BytesIO(image_part.data))
    else:
        raise ValueError("No image returned from Gemini")

# --- Image Download Link ---
def get_image_download_link(img, filename="gemini_image.png"):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    b64 = base64.b64encode(buffered.getvalue()).decode()
    return f'<a href="data:image/png;base64,{b64}" download="{filename}">📥 Download Image</a>'

# --- UI Layout ---
st.title("🧠 Modular Multi-Tool AI App")

tool_choice = st.radio("Choose your AI tool:", ["Text Assistant", "Image Generator"])
st.session_state.tool = tool_choice

prompt = st.text_area("Enter your prompt:")

if prompt:
    if tool_choice == "Text Assistant":
        if st.button("Generate Text"):
            try:
                st.session_state.generated_text = generate_text_response(prompt)
            except Exception as e:
                st.error(f"Error generating text: {e}")
        if st.session_state.generated_text:
            st.subheader("Gemini Text Response")
            st.write(st.session_state.generated_text)

    elif tool_choice == "Image Generator":
        if is_prompt_safe(prompt):
            st.success("Prompt is safe ✅")
            if st.button("Generate Image"):
                try:
                    st.session_state.generated_image = generate_image_response(prompt)
                except Exception as e:
                    st.error(f"Error generating image: {e}")
        else:
            st.error("Unsafe prompt detected. Please revise it.")

        if st.session_state.generated_image:
            st.image(st.session_state.generated_image, caption="Gemini Generated Image")
            st.markdown(get_image_download_link(st.session_state.generated_image), unsafe_allow_html=True)
