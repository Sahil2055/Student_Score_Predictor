# Project: Student Score Prediction

## 1. Project Overview
This project predicts a student's final exam score based on their study hours and attendance. It includes a full data analysis in a Jupyter Notebook and an interactive web app for making live predictions.

## 2. Project Structure
- **/data**: Contains the raw dataset.
- **/notebooks**: Holds the Jupyter Notebook with the exploratory data analysis.
- **/scripts**: Contains the Python script to train and save the final model.
- **/visualizations**: Stores the plots and graphs generated during analysis.
- **/webapp**: Contains the Streamlit interactive web application.
- **student_score_model.pkl**: The final, trained machine learning model.

## 3. How to Run This Project

### A. See the Analysis
1.  **Install dependencies:** `pip install -r requirements.txt`
2.  **Run Jupyter Lab:** `jupyter lab`
3.  Navigate to `notebooks/` and open `student_score_analysis.ipynb`.

### B. Run the Interactive Web App
1.  **First, train the model** by running the script from the main project folder:
    ```bash
    python scripts/train_model.py
    ```
2.  **Then, launch the web app:**
    ```bash
    streamlit run webapp/app.py
    ```
3.  A new tab will open in your browser with the interactive dashboard.