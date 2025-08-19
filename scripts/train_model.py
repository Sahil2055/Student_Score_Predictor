import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

print("Starting the model training script...")

# Load the dataset
df = pd.read_csv('../data/student_performance_dataset.csv')
print("Data loaded successfully.")

# Prepare the data for training
X = df[['study_hours_per_day', 'attendance_percentage']]
y = df['exam_score']
print("Data prepared for training.")

# Initialize and train the model on the full dataset
model = LinearRegression()
model.fit(X, y)
print("Model training complete.")

# Save the trained model to a file in the main project directory
joblib.dump(model, '../student_score_model.pkl')
print("Model saved as 'student_score_model.pkl'.")