# This is the main application file for the Streamlit web app
# It loads the trained model and provides a user interface for predicting student exam scores.



# Importing necessary libraries
import streamlit as st
import joblib
import numpy as np
import os



# --- 1. Build reliable paths for both the model and the images ---

# This creates paths that work on any computer or server.
APP_DIR = os.path.dirname(os.path.abspath(__file__))      # Directory of this app.py file
ROOT_DIR = os.path.join(APP_DIR, '..')                     # Moves one level up to the main project folder
MODEL_PATH = os.path.join(ROOT_DIR, 'student_score_model.pkl')    # Path to the model    

# Paths to all three visualization images
HEATMAP_PATH = os.path.join(ROOT_DIR, 'visualizations', 'heatmap.png')     # Path to the heatmap image
PAIRPLOT_PATH = os.path.join(ROOT_DIR, 'visualizations', 'pairplot.png')    # Path to the pairplot image
SCATTER_PLOT_PATH = os.path.join(ROOT_DIR, 'visualizations', 'study_hours_vs_exam_score.png')    # Path to the study_hours_vs_exam_score image



# --- 2. Load the saved model ---
# The model file is one level up from the 'webapp' folder
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error(f"Error: Model file not found at {MODEL_PATH}. Please ensure the model file exists and the path is correct.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()


# --- 3. Create the web page layout ---

# Set the title of the web app
st.title('🎓 Student Exam Score Predictor')

# Add some introductory text
st.write("""
This web app predicts a student's final exam score based on their study habits.
Adjust the sliders below to see the predicted score change.
""")



# --- 4. Create the user input elements in the sidebar ---
st.sidebar.header('Input Student Data')

# Create a slider for 'Hours Studied'
# Arguments: label, min_value, max_value, default_value
study_hours = st.sidebar.slider('Hours Studied per Day', 0.0, 10.0, 4.0)

# Create a slider for 'Attendance Percentage'
attendance = st.sidebar.slider('Attendance Percentage (%)', 0, 100, 80)



# --- 5. Make a prediction and display the result ---

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



# --- 6. Display the images using the reliable path ---
st.markdown("---") # Adds a horizontal line for separation
st.header("Exploratory Data Analysis Visualizations")
st.write("These charts from the analysis show the relationships in the data.")

# Display Heatmap
try:
    st.image(HEATMAP_PATH, caption='Correlation Matrix of Key Variables')
except Exception as e:
    st.warning(f"Could not load heatmap.")

# Display Pairplot
try:
    st.image(PAIRPLOT_PATH, caption='Pairplot of Key Variables')
except Exception as e:
    st.warning(f"Could not load pairplot.")

# Display Scatter Plot
try:
    st.image(SCATTER_PLOT_PATH, caption='Scatter Plot of Study Hours vs. Exam Score with Regression Line')
except Exception as e:
    st.warning(f"Could not load scatter plot.")



# --- 7. Add a footer with contact information ---
st.markdown("---") # Adds a horizontal line for separation
st.write("Created by Sahil Kesharwani")
st.write("For any questions or feedback, please contact: [sahil.kesharwani.927@gmail.com]")