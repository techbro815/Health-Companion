from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
db = client["Health_Companion"]

# Save a mood to the database
def save_mood(user_text, mood):
    db.moods.insert_one({"text": user_text, "mood": mood, "date": "2025-01-11"})
    print("Mood saved to database!")

# Retrieve mood counts
def get_mood_counts():
    moods = db.moods.aggregate([
        {"$group": {"_id": "$mood", "count": {"$sum": 1}}}
    ])
    return {doc["_id"]: doc["count"] for doc in moods}

# Save a calorie log
def save_calorie_log(user_id, meal, calories):
    db.calorie_logs.insert_one({"user_id": user_id, "meal": meal, "calories": calories, "date": "2025-01-11"})
    print("Calorie log saved to database!")

# Save goal progress
def save_goal_progress(user_id, goal_type, progress):
    db.goals.insert_one({"user_id": user_id, "goal_type": goal_type, "progress": progress, "date": "2025-01-11"})
    print("Goal progress saved to database!")