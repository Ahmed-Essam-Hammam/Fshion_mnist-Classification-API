# Fashion MNIST Classification API

## Overview
This project provides a REST API for classifying images from the Fashion MNIST dataset. The API takes an image as input, processes it using a trained deep learning model, and returns the predicted class.

## Features
- Accepts image input for classification
- Uses a trained deep learning model for prediction
- Provides JSON responses with predicted class labels

## Requirements
Ensure you have the following installed:

- Python 3.8+
- Flask
- TensorFlow/Keras
- NumPy
- Pillow

Install dependencies using:
```sh
pip install -r requirements.txt
```

## API Endpoints

### 1. Predict Image Class
#### Endpoint:
```http
POST /predict
```
#### Request:
- Content-Type: `multipart/form-data`
- Parameter: `image` (Upload an image file in grayscale format)

#### Example Usage:
```sh
curl -X POST -F "image=@sample_image.png" http://localhost:5000/predict
```

#### Response:
```json
{
  "class": "T-shirt/top",
  "confidence": 0.98
}
```

## Running the API
1. Clone the repository:
```sh
git clone <repository_url>
```
2. Navigate to the project folder:
```sh
cd fashion-mnist-api
```
3. Run the API:
```sh
python app.py
```
4. Access the API at:
```http
http://localhost:5000
```

## Model Training
If you need to train or retrain the model, run:
```sh
python train.py
```
This will generate a new trained model that the API will use for classification.

## Deployment
For deploying on a production server, consider using Gunicorn:
```sh
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## License
This project is open-source and available under the MIT License.
