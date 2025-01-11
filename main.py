import streamlit as st
from utils.apis import generate_quote, analyze_mood, estimate_calories
from utils.db import save_mood, save_calorie_log
from utils.goal_tracker import calculate_progress, calculate_streaks
from utils.health_analyser import suggest_activities
from dotenv import load_dotenv
import os
import plotly.graph_objects as go

# Load environment variables
load_dotenv()

# Set Page Config
st.set_page_config(
    page_title="AI Health Companion",
    page_icon=":sparkles:",
    layout="wide",
)

# API Key Debug (Optional)
API_KEY = os.getenv("WORQHAT_API_KEY")
if not API_KEY:
    st.sidebar.error("API Key not found! Make sure the .env file is set up correctly.")

# Dark/Light Mode Toggle
theme_toggle = st.sidebar.radio("Theme", ["Light", "Dark"])

# Apply CSS for Styling
if theme_toggle == "Dark":
    st.markdown(
        """
        <link rel="stylesheet" href="static/style.css">
        <style>
        body {
            background-color: #2C3E50;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <link rel="stylesheet" href="static/style.css">
        <style>
        body {
            background-color: #FAFAFA;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to", ["Home", "Daily Log", "Goal Tracker", "Motivational Quotes", "Activity Suggestions", "Calorie Estimation"]
)

if page == "Home":
    st.title("AI Health Companion")
    st.image("static/home_banner.png", use_container_width=True, caption="Your Wellness Partner")
    st.write(
        """
        Welcome to AI Health Companion — Your personal AI assistant to track health, motivate, 
        and provide actionable insights for your physical and mental wellness goals.
        """
    )

elif page == "Daily Log":
    st.title("Daily Log")
    user_text = st.text_area("How was your day?", placeholder="Write about your day...")
    if st.button("Analyze Day"):
        if user_text.strip():
            mood = analyze_mood(user_text)
            if "error" not in mood:
                st.success(f"Mood detected: {mood['data']['mood']}")
                save_mood(user_text, mood['data']['mood'])
                suggestions = suggest_activities(user_text)
                st.write("Here are some tips for you:")
                for suggestion in suggestions:
                    st.write(f"- {suggestion}")
            else:
                st.error(f"Failed to analyze mood. Details: {mood.get('details', 'No additional info')}")
        else:
            st.warning("Please enter your daily log.")

elif page == "Goal Tracker":
    st.title("Goal Tracker")
    progress = calculate_progress()
    streak = calculate_streaks()

    # Display streak information
    st.write(f"You've been consistent for {streak} days in a row! Keep it up!")

    # Dynamic Progress Graph with Plotly
    fig = go.Figure(
        go.Bar(
            x=list(progress.keys()),
            y=list(progress.values()),
            text=[f"{v}%" for v in progress.values()],
            textposition="outside",
        )
    )
    fig.update_layout(
        title="Your Goal Progress",
        xaxis_title="Timeframe",
        yaxis_title="Completion %",
        template="plotly_dark" if theme_toggle == "Dark" else "plotly_white",
    )
    st.plotly_chart(fig, use_container_width=True)

elif page == "Motivational Quotes":
    st.title("Motivational Quotes")
    if st.button("Get Motivational Quote"):
        quote = generate_quote()
        if "error" not in quote:
            st.success(f'"{quote["data"]["text"]}"')
        else:
            st.error(f"Failed to fetch quote. Details: {quote.get('details', 'No additional info')}")

elif page == "Activity Suggestions":
    st.title("Activity Suggestions")
    activity_type = st.selectbox("Choose activity type", ["Physical", "Mental"])
    user_interest = st.text_input("What do you enjoy?", placeholder="e.g., running, yoga, reading...")
    if st.button("Get Suggestions"):
        if user_interest.strip():
            activities = suggest_activities(user_interest, activity_type)
            st.write("Here are some suggestions:")
            for activity in activities:
                st.write(f"- {activity}")
        else:
            st.warning("Please enter an interest!")

elif page == "Calorie Estimation":
    st.title("Calorie Estimation")
    uploaded_image = st.file_uploader("Upload an image of your meal", type=["jpg", "png", "jpeg"])
    if st.button("Estimate Calories"):
        if uploaded_image:
            calorie_data = estimate_calories(uploaded_image)
            if "error" not in calorie_data:
                st.success(f"Estimated Calories: {calorie_data['calories']} kcal")
                save_calorie_log("user_id_placeholder", "Meal Name", calorie_data['calories'])
            else:
                st.error(f"Failed to estimate calories. Details: {calorie_data.get('details', 'No additional info')}")
        else:
            st.warning("Please upload an image.")