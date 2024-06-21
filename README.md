# GENOVA-AI. Flask Website for Brain Tumor Identification.

![Screenshot from 2024-06-19 20-18-11](https://github.com/SupraSantoso/GENOVA-AI/assets/160683548/5a6661bc-d7ea-4369-8c17-85ce8bb3f2c1)

# Table of Contents

- [Introduction]
- [Features]
- [Installation]
- [Usage]
- [Project Structure]
- [Contact]

## Introduction

This project demonstrates how to serve static files using Flask. It includes HTML, CSS, and JavaScript files to create a basic static website with a responsive design.

## Features

- Simple Flask setup
- Serving static HTML, CSS, and JavaScript files
- Responsive design using Bootstrap
- Basic routing for home page and additional static pages
- User interactive chat with GENOVA-AI bot

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/SupraSantoso/GENOVA-AI.git
    cd repository
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Extract .zip keras model:**
    ```bash
    cd model
    unzip CNN_MODEL_KERAS.h5
    ```
    
5. **Run the Flask application:**
    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

- **Navigating to the Home Page:**
  Open your web browser and go to `http://127.0.0.1:5000/`. This page includes a home page and navbar for navigation to other sections of the website.

- **Accessing the About Us Page:**
  To learn more about the website or organization, go to `http://127.0.0.1:5000/about`. This page contains detailed information about the mission, team members and job desk.

- **Accessing to the FAQ Page:**
  To learn more about the website or FAQ go to `http://127.0.0.1:5000/faq`. This page several question for use this website basically.

- **Accessing the AI Prediction Page:**
  To learn more about the website or organization, go to `http://127.0.0.1:5000/predict` or push the button on the home page 'Prediksi AI'. This page contains to predict your image for brain tumor. After the result show on this page, you can chat with GENOVA-AI chatbot for deep question about brain tumor.

- **Accessing the Brain Tumor Article:**
  To learn more about the brain tumor definition, go to `http://127.0.0.1:5000/more`. This page explain what is brain tumor definition and several type indetification with the galery example each class.

  ## Project Structure
![image](https://github.com/SupraSantoso/GENOVA-AI/assets/160683548/b4b24bd8-588a-4ac6-920d-0ba03027575e)

![image](https://github.com/SupraSantoso/GENOVA-AI/assets/160683548/a7b25b73-34bf-4e7b-adaf-9fc3315d10ca)

 ## Contact

If you have any questions or suggestions, feel free to reach out:

- **Name:** Suprapto Santoso
- **Email:** supra.jgu@gmail.com
- **GitHub:** [SupraSantoso](https://github.com/SupraSantoso)
