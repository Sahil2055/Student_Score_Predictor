# This is the main application file for the Streamlit web app
# It loads the trained model and provides a user interface for predicting student exam scores.


# Importing necessary libraries
import streamlit as st
import joblib
import numpy as np


# --- 1. Load the saved model ---
# The model file is one level up from the 'webapp' folder
try:
    model = joblib.load('../Student_Score_Predictor/student_score_model.pkl')
except FileNotFoundError:
    st.error("Model file not found! Please run the training script first from your terminal: python scripts/train_model.py")
    st.stop()



# --- 2. Create the web page layout ---

# Set the title of the web app
st.title('🎓 Student Exam Score Predictor')

# Add some introductory text
st.write("""
This web app predicts a student's final exam score based on their study habits.
Adjust the sliders below to see the predicted score change.
""")



# --- 3. Create the user input elements in the sidebar ---
st.sidebar.header('Input Student Data')

# Create a slider for 'Hours Studied'
# Arguments: label, min_value, max_value, default_value
study_hours = st.sidebar.slider('Hours Studied per Day', 0.0, 10.0, 4.0)

# Create a slider for 'Attendance Percentage'
attendance = st.sidebar.slider('Attendance Percentage (%)', 0, 100, 80)



# --- 4. Make a prediction and display the result ---

# When the user clicks the 'Predict' button
if st.sidebar.button('Predict Score'):

    # Prepare the input data for the model
    # The model expects a 2D array, so we use np.array([[...]])
    input_data = np.array([[study_hours, attendance]])

    # Make the prediction
    predicted_score = model.predict(input_data)

    # Display the result in a nice, big font
    st.header(f'Predicted Exam Score: {predicted_score[0]:.2f}')

    # Provide some context or interpretation
    if predicted_score[0] >= 90:
        st.success("Excellent performance! This student is on track for a top grade. 🎉")
    elif predicted_score[0] >= 75:
        st.info("Good performance. Keep up the consistent effort. 👍")
    elif predicted_score[0] >= 50:
        st.warning("This is a passing score, but there is room for improvement. 📚")
    else:
        st.error("This score is below the passing threshold. Intervention may be needed. 😟")



# Optional: Add an image from project to make it more attractive
# Make sure the path is correct relative to the 'app.py' file
st.image('../Student_Score_Predictor/visualizations/pairplot.png', caption='Pairplot of Study Hours, Attendance, and Exam Score')
st.image('../Student_Score_Predictor/visualizations/heatmap.png', caption='Correlation Heatmap of Key Factors')
st.image('../Student_Score_Predictor/visualizations/study_hours_vs_exam_score.png', caption='Scatter Plot with Regression Line of Study Hours vs Exam Score')