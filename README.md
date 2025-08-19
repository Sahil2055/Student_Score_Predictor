# Student Score Predictor

**Welcome to the Student Score Predictor project! This repository contains a complete data analysis project that builds a machine learning model to predict student exam scores based on their study habits. It also includes a fun, interactive web app to see the model in action.**

---

## 📜 Project Overview

Have you ever wondered how much study time **really** affects exam results? This project dives into that question! I used a student performance dataset to uncover insights and build a predictive model that forecasts academic success based on student behavior.

The main goal is to create a simple yet effective tool that can estimate a student's final exam score based on two key factors:
- **Hours Studied per Day** 📚
- **Attendance Percentage** ✅

---

## Deployed Version Of Project

**https://sk-student-score-predictor.streamlit.app/**

---

## 🎯 Problem Statement

The main challenge was to move beyond simple observation and provide data-driven answers to common academic questions. This project addresses the following:

- **Uncertainty in Impact:** Students and educators often guess which habits, like study hours versus attendance, have the biggest impact on grades. This project aims to provide a clear answer.
- **Lack of Predictive Insight:** It's hard to know if a student is on the right track. I wanted to build a tool that could forecast their potential exam score based on current habits, making it easier to make changes if needed.
- **Need for an Easy-to-Use Tool:** I wanted to turn the complex data into something simple and actionable. The goal was to create a tool that makes it easy to see how changing study habits could change results.

---

## ✨ Key Features

- **📊 In-Depth Data Analysis:** I explored the data with clear and attractive visualizations to understand the relationships between study time, attendance, and scores.
- **🤖 Predictive Modeling:** I built a solid Linear Regression model using Scikit-learn to accurately predict student exam scores.
- **🌐 Interactive Dashboard:** The best part! I created a user-friendly web app with Streamlit that allows anyone to get real-time score predictions by simply adjusting sliders.
- **📂 Clean & Organized:** The project is organized in a professional way, making it easy for anyone to run and understand.

---

## 📂 Project Structure

I organized the project in a clean and professional manner. Here’s a look at the file and folder structure:

**`📂student-score-prediction/`**
-   `📄 README.md`: This file, which provides a detailed overview of the project.
-   `📁 sample_dataset/`
    -   `student_performance_dataset.csv`: The raw data for our project.
-   `📁 notebooks/`
    -   `student_score_analysis.ipynb`: The main Jupyter notebook having analysis and model exploration.
-   `📁 presentations/`
    -   `.pdf`: The presentation file that explains the project's goals, methods, and results.
-   `📁 scripts/`
    -   `train_model.py`: The python file that contains a script to train and save the final model.
-   `📁 visualizations/`
    -   `heatmap.png`: Correlation Heatmap of Key Factors
    -   `pairplot.png`: Pairplot of key variables (Study Hours, Attendance, and Exam Score).
    -   `study_hours_vs_exam_score.png`: Scatter Plot with Regression Line of Study Hours vs Exam Score.
-   `📁 webapp/`
    -   `app.py`: This python file contains the code for our interactive web dashboard.
-   `📄 .gitignore`: The technical file that tells Git which files to ignore and helps GitHub manage the repository correctly.
-   `📄 requirements.txt`: The file containing all the Python libraries needed for this project.
-   `📄 student_score_model.pkl`: The final, saved machine learning model.

---

## ⚙️ How to Run This Project

You can explore my analysis or run the interactive web app by following these steps.

### Prerequisites
- Python 3.x
- A passion for data! ✨


### Step 1: Set Up the Environment

First, clone this repository and set up the Python environment.

-   Clone the repository to your computer: `git clone <your-github-repo-link>`
-   Navigate into the project directory: `cd student-score-prediction`
-   Create and activate a virtual environment:
    -   On Windows: `.venv\Scripts\activate`
    -   On macOS/Linux: `source .venv/bin/activate`
-   Install all the necessary libraries: `pip install -r requirements.txt`


### Step 2: Explore the Analysis 📊

-   Start Jupyter Lab using this `jupyter lab` and then, navigate to the `notebooks/` folder and open `student_score_analysis.ipynb`.
    -   (Either do this orr directly navigate to the `notebooks/` folder and open `student_score_analysis.ipynb`.)


### Step 3: Launch the Interactive Web App! 🚀

-   First, train and save the model: `python scripts/train_model.py`
-   Now, launch the Streamlit web app: `streamlit run webapp/app.py`

**A new tab will open in your web browser with the interactive dashboard!**

---

## 🛠️ Technology Stack

I built this project using these awesome open-source tools and libraries:

-   **Python:** The core programming language.
-   **Pandas:** For handling and analyzing the data.
-   **Matplotlib & Seaborn:** For creating the beautiful visualizations(charts and graphs).
-   **Scikit-learn:** For building and evaluating the machine learning model.
-   **Streamlit:** For creating and deploying the interactive web app.
-   **Jupyter Notebook:** For exploratory data analysis and documentation.

---

## 👨‍💻 Author

-   **Name:** Sahil Kesharwani

---