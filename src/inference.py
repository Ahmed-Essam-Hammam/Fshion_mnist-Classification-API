from PIL import Image
import numpy as np
from io import BytesIO
from .config import MODEL, CLASS_NAMES
from .schemas import PredictionResponse

def clasify_image(image_bytes: bytes) -> PredictionResponse:
    
    try:
        img = Image.open(BytesIO(image_bytes))
        if img.mode != 'L':
            img = img.convert('L')
            
        # resize
        img = img.resize((28, 28))
        img_array = np.array(img)
        img_array = img_array.astype("float32") / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # to be 1x28x28
        
        # predict
        prediction = MODEL.predict(img_array, verbose=0)
        predicted_class = np.argmax(prediction, axis=-1)[0]
        predicted_name = CLASS_NAMES[predicted_class]
        predictions = {
                'class_index': int(predicted_class),
                'class_name': predicted_name,
                'confidence': float(prediction[0][predicted_class] * 100)
                }
        return PredictionResponse(**predictions)
    
    except Exception as e:
        raise ValueError(f"Image processing failed: {str(e)}")