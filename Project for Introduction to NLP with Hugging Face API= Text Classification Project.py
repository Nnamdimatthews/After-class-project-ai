import requests

# Hugging Fae API endpoint (sentiment analysis)
api_url = "https://api-inference.huggingface.co/models/distilbert-base-ucased"

# Your Hugging Face API token (replace with your actual token)
headers = {
    "Authorization": "Bearer YOUR_API_KEY_HERE"
}

# Text to class (example sentence)
text = "I like doing coding it so fascinating."

# Make a POST request to the Hugging Face API
response = requests.post(api_url, headers=headers, json={"inputs":text})

if response.status_code == 200:
    # Parse and print the results
    classification = response.json()
    print("Predicted label:", classification[0]['label'])
else:
    print(f"Error: {response.status_code}")