# AI Health Companion

## 🌟 Overview

AI Health Companion is a user-friendly platform designed to help users track and improve their physical and mental health. The app combines powerful AI tools, including mood analysis, calorie estimation, and motivational quotes, to provide a holistic approach to health and wellness. By gamifying health goals with streaks and rewards, it keeps users engaged and motivated.

---

## 🎯 Problem Statement

1. Lack of integrated solutions for physical and mental health tracking.
2. No easy way to visualize and track daily progress toward health goals.
3. Absence of personalized and real-time suggestions to keep users motivated.

---

## 🚀 Features

1. **Daily Logs**:
   - Log your mood using pre-defined filters or conversational input.
   - Analyze mood trends and receive improvement suggestions.
2. **Goal Tracker**:

   - Set and track daily, weekly, and monthly health goals.
   - Visualize your progress with dynamic graphs.

3. **Activity Suggestions**:

   - AI-driven suggestions tailored to your preferences.
   - Categorized into physical (e.g., yoga, cardio) and mental health options.

4. **Calorie Estimation**:

   - Upload food images for real-time calorie estimation.
   - View calorie trends over time using visualizations.

5. **Motivational Messages**:

   - Receive AI-generated affirmations personalized for your journey.

6. **Gamification**:
   - Earn points and rewards by maintaining daily streaks.
   - Visualize streaks and points in a dedicated dashboard.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit for an interactive and user-friendly UI.
- **Backend**: WorqHat APIs for AI functionalities.
- **Database**: MongoDB (Atlas) for storing user data and streaks.
- **Visualization**: Plotly for creating dynamic graphs and charts.
- **Libraries**: `pymongo`, `requests`, `matplotlib`.

---

## 🤖 WorqHat API Models Used

1. **Text Generation API**:
   - Generates motivational quotes.
   - Provides conversational insights for daily logs.
2. **Mood Analysis API**:
   - Analyzes user mood from text input.
   - Tracks mental health trends.
3. **Calorie Estimation API**:
   - Estimates calories from food images.
4. **Image Analysis API**:

   - Identifies activities or meals from user-uploaded images.
   - Provides relevant suggestions.

5. **Content Moderation API**:

   - Ensures user inputs are safe and appropriate.

6. **Model Training API**:
   - Customizes activity suggestions for recurring users.

---

## 📊 Workflow Diagram

1. **Input**: User logs mood, activities, or uploads food images.
2. **Processing**: APIs analyze inputs for mood, calories, or activities.
3. **Storage**: MongoDB stores user logs, streaks, and progress.
4. **Output**: Personalized suggestions, motivational quotes, and health insights.

![Workflow Diagram](path/to/diagram.png)

---

## 📋 Setup Instructions

Follow these steps to set up and run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/techbro815/Health-Companion.git
   ```
2. Navigate to the project directory:
   cd Health-Companion

3. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate # For Linux/Mac
   venv\Scripts\activate # For Windows

4. Install dependencies:  
   pip install -r requirements.txt

5. Add a .env file with your API keys and configurations:
   WORQHAT_API_KEY=your_api_key
   MONGO_URI=your_mongo_connection_string

6. Run the application:
   streamlit run main.py

⚙️ Current Status

Implemented: 1. Daily mood tracking with suggestions. 2. Goal tracking and progress visualization. 3. Calorie estimation from uploaded images. 4. Motivational quotes for daily encouragement.

In Progress: 1. Advanced activity suggestions based on user habits and preferences. 2. User-specific model training with WorqHat APIs.

🏆 Future Enhancements
• Advanced image analysis to identify exercises and meals.
• AI-powered chatbot for personalized health advice.
• Integration of wearable device data (e.g., Fitbit, Apple Watch).

🙋‍♂️ Authors
• Sujal Thakur - Developer
• Advika Khorgade - Developer and Consultant

🌟 Acknowledgments
• WorqHat API for providing robust AI functionalities.
