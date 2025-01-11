import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

WORQHAT_API_URL = "https://api.worqhat.com"
API_KEY = os.getenv("WORQHAT_API_KEY")  # Securely load the API Key from .env

def generate_quote():
    try:
        response = requests.post(
            f"{WORQHAT_API_URL}/text-generation",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        error_details = response.text if 'response' in locals() else str(e)
        return {"error": "Failed to connect to API.", "details": error_details}

def analyze_mood(user_text):
    try:
        response = requests.post(
            f"{WORQHAT_API_URL}/mood-analysis",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"text": user_text}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        error_details = response.text if 'response' in locals() else str(e)
        return {"error": "Failed to connect to API.", "details": error_details}

def estimate_calories(image):
    try:
        files = {"image": image}
        response = requests.post(
            f"{WORQHAT_API_URL}/calorie-estimation",
            headers={"Authorization": f"Bearer {API_KEY}"},
            files=files,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        error_details = response.text if 'response' in locals() else str(e)
        return {"error": "Failed to estimate calories.", "details": error_details}