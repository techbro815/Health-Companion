def suggest_activities(user_input, activity_type="Physical"):
    physical_activities = {
        "cardio": ["Jogging", "Cycling", "Swimming"],
        "weights": ["Deadlifts", "Bench Press", "Squats"],
        "yoga": ["Hatha Yoga", "Vinyasa Flow"],
    }
    mental_activities = {
        "reading": ["Meditation books", "Fiction novels"],
        "puzzles": ["Crossword puzzles", "Sudoku"],
        "meditation": ["Guided meditation", "Mindfulness breathing"],
    }

    suggestions = []
    if activity_type == "Physical":
        for key, activities in physical_activities.items():
            if key in user_input.lower():
                suggestions.extend(activities)
    elif activity_type == "Mental":
        for key, activities in mental_activities.items():
            if key in user_input.lower():
                suggestions.extend(activities)
    return suggestions if suggestions else ["Try exploring something new today!"]