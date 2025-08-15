# --- 1. Import Necessary Libraries ---
import streamlit as st
import pickle
import numpy as np

# --- 2. Load the Saved Model ---
# We open the 'student_score_model.pkl' file in 'read binary' mode ('rb').
# The 'pickle.load()' function reconstructs the model object from the file.
try:
    with open('student_score_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found! Please run 'train_and_save_model.py' first.")
    st.stop() # Stops the app from running further if the model isn't found

# --- 3. Create the Web App's Interface using Streamlit ---

# Set the title of the web page
st.title('🎓 Student Exam Score Predictor')

# Add some descriptive text
st.write("""
This interactive web app uses a Machine Learning model to predict a student's final exam score.
Provide the student's study habits below to get a prediction.
""")

# Create a separator
st.markdown("---")

# --- 4. Add Interactive Widgets for User Input ---
# We'll use Streamlit's sidebar for the input controls to keep the main page clean.
st.sidebar.header('Input Student Data Here:')

# Create a slider for 'Study Hours'
# The format is: st.slider('Label', min_value, max_value, default_value)
study_hours = st.sidebar.slider('Average Study Hours per Day', 0.0, 10.0, 4.0, 0.5)

# Create a slider for 'Attendance Percentage'
attendance = st.sidebar.slider('Class Attendance Percentage', 0, 100, 80, 1)

# --- 5. Make a Prediction and Display the Result ---

# Display a subheader on the main page
st.header('Prediction Result')

# Prepare the input data for the model
# The model expects a 2D array, so we wrap our inputs in np.array([[]])
input_data = np.array([[study_hours, attendance]])

# Use the loaded model to make a prediction
predicted_score = model.predict(input_data)

# Display the prediction in a visually appealing way using st.metric
st.metric(
    label="Predicted Exam Score",
    value=f"{predicted_score[0]:.2f}",
    delta=f"{predicted_score[0] - 70:.2f} points from a 70 (Pass)" # Shows how far the score is from a passing grade of 70
)

st.info("Note: This prediction is based on a machine learning model and should be used for informational purposes only.")

# Add a fun element!
if predicted_score[0] > 90:
    st.balloons()