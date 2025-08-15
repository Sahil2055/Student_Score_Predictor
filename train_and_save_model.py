import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

print("--- Starting Model Training ---")

# --- 1. Load and Prepare Data ---
# We load the dataset directly from the data folder.
df = pd.read_csv('../sample_dataset/student_performance_dataset.csv')

# We select only the columns we need for our model.
df_model = df[['study_hours_per_day', 'attendance_percentage', 'exam_score']].copy()
print("Data loaded and prepared successfully.")

# --- 2. Define Features (X) and Target (y) ---
X = df_model[['study_hours_per_day', 'attendance_percentage']]
y = df_model['exam_score']

# --- 3. Train the Model ---
# We create an instance of the Linear Regression model.
# We train it on the ENTIRE dataset to make it as accurate as possible.
model = LinearRegression()
model.fit(X, y)
print("Model has been trained on the full dataset.")

# --- 4. Save the Model to a File ---
# We use the 'pickle' library to save our trained model to a file.
# The 'wb' means we're writing to the file in binary mode.
with open('student_score_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("--- Model Saved ---")
print("The trained model has been saved as 'student_score_model.pkl'")