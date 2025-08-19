# 🎓 Student Score Predictor 🚀

Welcome to the Student Score Predictor project! This repository contains everything you need to understand how I built a machine learning model to predict student exam scores. It also includes a fun, interactive web app to see the model in action.



---

## 📜 Project Overview

Have you ever wondered how much study time *really* affects exam results? This project dives into that question! I used a student performance dataset to uncover insights and build a predictive model that forecasts academic success based on student behavior.

The main goal is to create a simple yet effective tool that can estimate a student's final exam score based on two key factors:
* **Hours Studied per Day** 📚
* **Attendance Percentage** ✅

---

## 🎯 Problem Statement

The main challenge was to move beyond simple observation and provide data-driven answers to common academic questions. This project addresses the following:

* **Uncertainty in Impact:** Students and educators often guess which habits, like study hours versus attendance, have the biggest impact on grades. This project aims to provide a clear answer.
* **Lack of Predictive Insight:** It's hard to know if a student is on the right track. I wanted to build a tool that could forecast their potential exam score based on current habits, making it easier to make changes if needed.
* **Need for an Easy-to-Use Tool:** I wanted to turn the complex data into something simple and actionable. The goal was to create a tool that makes it easy to see how changing study habits could change results.

---

## ✨ Key Features

This project is a complete data science workflow with several key features:

* **📊 In-Depth Data Analysis:** I explored the data with clear and attractive visualizations to understand the relationships between study time, attendance, and scores.
* **🤖 Predictive Modeling:** I built a solid Linear Regression model using Scikit-learn to accurately forecast student exam scores.
* **🌐 Interactive Dashboard:** The best part! I created a user-friendly web app with Streamlit that allows anyone to get real-time score predictions by simply adjusting sliders.
* **📂 Clean & Organized:** The project is organized in a professional way, making it easy for anyone to run and understand.

---

## 📂 Project Structure

I organized the project in a clean and professional manner. Here’s a look at the file and folder structure:

student-score-prediction/
│
├── 📁 data/
│   └── student_performance_dataset.csv  (The raw data for my project)
│
├── 📁 notebooks/
│   └── student_score_analysis.ipynb     (My main analysis and model exploration)
│
├── 📁 presentations/
│   └── (My project presentation/PPT files go here)
│
├── 📁 scripts/
│   └── train_model.py                   (A script to train and save the final model)
│
├── 📁 visualizations/
│   ├── heatmap.png                      (Correlation heatmap)
│   ├── pairplot.png                     (Pairplot of key variables)
│   └── study_hours_vs_exam_score.png    (Scatter plot of study hours vs. score)
│
├── 📁 webapp/
│   └── app.py                           (The code for my interactive web dashboard)
│
├── 📄 .gitignore                        (Tells Git which files to ignore)
├── 📄 README.md                         (This file! My project's front page)
├── 📄 requirements.txt                  (All the Python libraries needed for this project)
└── 📄 student_score_model.pkl          (The final, saved machine learning model)



---


## ⚙️ How to Run This Project

You can explore my analysis or run the interactive web app by following these steps.

### Prerequisites
* Python 3.x
* A passion for data! ✨

### Step 1: Set Up the Environment
First, clone this repository and set up the Python environment.

```bash
# 1. Clone the repository to your computer
git clone <your-github-repo-link>

# 2. Navigate into the project directory
cd student-score-prediction

# 3. Create and activate a virtual environment
python -m venv .venv
# On Windows: .venv\Scripts\activate
# On macOS/Linux: source .venv/bin/activate

# 4. Install all the necessary libraries
pip install -r requirements.txt