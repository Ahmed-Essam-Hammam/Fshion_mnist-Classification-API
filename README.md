# Fashion MNIST Classification API

This project provides a RESTful API for classifying images from the Fashion MNIST dataset using a pre-trained deep learning model. The API is built using FastAPI, and the model is trained using TensorFlow.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Training](#model-training)
- [License](#license)

## Overview
The Fashion MNIST dataset consists of 70,000 grayscale images of 10 different categories of clothing items. Each image is 28x28 pixels. This project trains a neural network to classify these images and provides an API to make predictions on new images.

The API allows users to upload an image, and it returns the predicted class along with the confidence score.

## Installation
### Clone the repository:
```bash
git clone https://github.com/yourusername/fashion-mnist-classification-api.git
cd fashion-mnist-classification-api
```

### Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the API:
```bash
uvicorn main:app --reload
```
The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage
### Making a Prediction
To classify an image, send a POST request to the `/classify` endpoint with the image file.

#### Example using curl:
```bash
curl -X POST "http://127.0.0.1:8000/classify" \
     -H "X-API-Key: your_api_key" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path_to_your_image.png"
```

#### Example using Python:
```python
import requests

url = "http://127.0.0.1:8000/classify"
headers = {
    "X-API-Key": "your_api_key",
    "accept": "application/json",
}
files = {"file": open("path_to_your_image.png", "rb")}

response = requests.post(url, headers=headers, files=files)
print(response.json())
```

### Response Format
The API will return a JSON response with the following format:
```json
{
    "class_index": 9,
    "class_name": "Ankle_Boot",
    "confidence": 95.67
}
```

## API Endpoints
### `GET /`
Check if the API is running.
```json
{
    "app_name": "Fashion MNIST Classification API",
    "version": "1.0.0",
    "status": "up & running"
}
```

### `POST /classify`
Classify an uploaded image.

#### Headers:
- `X-API-Key`: Your API key.

#### Body:
- `file`: The image file to classify.

#### Response:
```json
{
    "class_index": 9,
    "class_name": "Ankle_Boot",
    "confidence": 95.67
}
```

## Model Training
The model is trained using TensorFlow on the Fashion MNIST dataset. The training process involves the following steps:

1. **Data Loading**: The Fashion MNIST dataset is loaded using TensorFlow's built-in dataset.
2. **Data Preprocessing**: The images are normalized to the range `[0, 1]` and converted to `float32`.
3. **Model Building**: A simple feedforward neural network is built using TensorFlow's Keras API.
4. **Training**: The model is trained for 20 epochs with early stopping to prevent overfitting.
5. **Evaluation**: The model is evaluated on the test set, and predictions are made on new images.

The trained model is saved as `model.keras` and loaded in the API for inference.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
