# Dataset Analysis App

This is a simple and interactive Streamlit application that allows users to upload a CSV dataset and perform basic exploratory data analysis such as viewing head/tail, checking dataset dimensions, detecting missing values, removing duplicates, and visualizing null-value heatmaps.

Live App: https://dataset-analysis-app.streamlit.app/

--------------------------------------------

## Features

- Upload any CSV dataset
- Preview the first and last rows
- Check number of rows and columns
- Identify missing values
- View missing value heatmap
- Detect and optionally remove duplicate rows
- View statistical summary of the dataset
- Simple and clean Streamlit interface

--------------------------------------------

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn

--------------------------------------------

## How to Run Locally

1. Clone or download the project folder.

2. Create a virtual environment:
   python3 -m venv .venv

3. Activate the virtual environment:
   Linux/macOS:
   source .venv/bin/activate

   Windows:
   .venv\Scripts\activate

4. Install required libraries:
   pip install -r requirements.txt

5. Run the Streamlit app:
   streamlit run main.py

--------------------------------------------

## Project Structure

main.py
requirements.txt
README.md

--------------------------------------------

## Requirements file

streamlit
pandas
numpy
matplotlib
seaborn

--------------------------------------------

## About

A beginner-friendly exploratory data analysis tool built using Streamlit.
Created by: Amrit Singh

