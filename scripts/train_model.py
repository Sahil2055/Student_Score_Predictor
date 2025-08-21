# This script trains a machine learning model to predict student exam scores based on study hours and attendance.
# It uses a linear regression model and saves the trained model to a file.


# Importing necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os


# Print a message indicating the start of the script
print("Starting the model training script...")


# --- 1. Build reliable paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))          # Get the directory of the current script
ROOT_DIR = os.path.join(SCRIPT_DIR, '..')          # Move one level up to the main project folder
DATA_PATH = os.path.join(ROOT_DIR, 'sample_dataset', 'student_performance_dataset.csv')          # Path to the dataset
MODEL_PATH = os.path.join(ROOT_DIR, 'student_score_model.pkl')          # Path to save the trained model


# --- 2. Load the data ---
try:
    df = pd.read_csv(DATA_PATH)
    print("Data loaded successfully.")
except FileNotFoundError:
    print(f"Error: Could not find the dataset at {DATA_PATH}")
    exit()


# --- 3. Prepare the data for training ---
X = df[['study_hours_per_day', 'attendance_percentage']]
y = df['exam_score']
print("Data prepared for training.")


# --- 4. Initialize and train the model on the full dataset ---
model = LinearRegression()
model.fit(X, y)
print("Model training complete.")


# --- 5. Save the trained model to a file in the main project directory ---
joblib.dump(model, MODEL_PATH)
print(f"Model saved successfully to: {MODEL_PATH}")