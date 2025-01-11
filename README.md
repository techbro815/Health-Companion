# AI Health Companion

This is a Streamlit-based app that integrates WorqHat APIs and MongoDB to help manage mental and physical health.

## Features

1. Generate motivational quotes.
2. Analyze user mood.
3. Store mood data in MongoDB.
4. Visualize mood trends with bar charts.

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/ai_health_companion.git
   ```
2. Navigate to the project directory:

cd ai_health_companion

3. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Update the following placeholders in utils/apis.py and utils/db.py:

Replace your_api_key with your actual WorqHat API key.
Replace your_connection_string with your MongoDB connection string.

6. Run the app:
   streamlit run main.py

7. Open the app in your browser at http://localhost:8501.
