import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API Configuration
WORQHAT_API_URL = "https://api.worqhat.com/v1"
API_KEY = os.getenv("WORQHAT_API_KEY")  # Securely load the API Key from .env
MODEL_ID = "aicon-v4-large-160824"  # Change to "aicon-v4-nano-160824" if you prefer the Nano model

def generate_quote():
    """Fetch a motivational quote using the AiCon V4 API."""
    try:
        # Endpoint URL for text generation
        endpoint_url = f"{WORQHAT_API_URL}/{MODEL_ID}/text-generation"

        # Request payload
        payload = {
            "prompt": "Generate a motivational quote.",  # Prompt for the API
            "max_tokens": 50,  # Limit on the length of the generated quote
        }

        # API request
        response = requests.post(
            endpoint_url,
            headers={"Authorization": f"Bearer {API_KEY}"},
            json=payload
        )
        response.raise_for_status()

        # Return the generated quote
        return response.json()
    except requests.exceptions.RequestException as e:
        # Error handling
        error_details = response.text if 'response' in locals() and response else str(e)
        return {"error": "Failed to fetch quote.", "details": error_details}

def analyze_mood(user_text):
    """Analyze the mood from user text."""
    try:
        # Endpoint URL for mood analysis
        endpoint_url = f"{WORQHAT_API_URL}/mood-analysis"

        # Request payload
        payload = {"text": user_text}

        # API request
        response = requests.post(
            endpoint_url,
            headers={"Authorization": f"Bearer {API_KEY}"},
            json=payload
        )
        response.raise_for_status()

        # Return the mood analysis
        return response.json()
    except requests.exceptions.RequestException as e:
        # Error handling
        error_details = response.text if 'response' in locals() and response else str(e)
        return {"error": "Failed to analyze mood.", "details": error_details}

def estimate_calories(image):
    """Estimate calories from an image."""
    try:
        # Endpoint URL for calorie estimation
        endpoint_url = f"{WORQHAT_API_URL}/calorie-estimation"

        # File upload
        files = {"image": image}

        # API request
        response = requests.post(
            endpoint_url,
            headers={"Authorization": f"Bearer {API_KEY}"},
            files=files,
        )
        response.raise_for_status()

        # Return the calorie estimation
        return response.json()
    except requests.exceptions.RequestException as e:
        # Error handling
        error_details = response.text if 'response' in locals() and response else str(e)
        return {"error": "Failed to estimate calories.", "details": error_details}