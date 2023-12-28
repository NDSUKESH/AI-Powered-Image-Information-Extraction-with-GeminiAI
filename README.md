# AI-Powered-Image-Information-Extraction-with-GeminiAI

## Overview

This project utilizes the GeminiAI Generative Model by GOOGLE to extract information from images based on user input. The code is designed to take an image and a user prompt, then generate relevant information using the GeminiAI API.

## Getting Started

### Prerequisites

Before running the code, ensure you have the required libraries installed. You can install them using:

```bash
pip install -r requirements.txt
```

### Setting up Environment Variables

Create a `.env` file in the project directory and add your Google API key:

```dotenv
GOOGLE_API_KEY=your_api_key_here
```

### Running the Application
Run the main.py file:
```run
streamlit run app.py
```

### Usage
- Enter a prompt in the provided text input.
- Upload an image (supported formats: jpg, jpeg, png).
- Click the "RUN" button to generate information based on the input and image.

### Model Information
The code uses the GeminiAI Generative Model named 'gemini-pro-vision' for image analysis.

### Dependencies
- Python 3.10
- Streamlit
- Pillow (PIL)
- GeminiAI

