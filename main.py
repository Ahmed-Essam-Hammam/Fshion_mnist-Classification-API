from fastapi import FastAPI, HTTPException, Depends, UploadFile
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from src.config import APP_NAME, VERSION, API_SECRET_KEY
from src.schemas import PredictionResponse
from src.inference import clasify_image


# Initialize an app
app = FastAPI(title=APP_NAME, version=VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


api_key_header = APIKeyHeader(name='X-API-Key')
async def verify_api_key(api_key: str=Depends(api_key_header)):
    if api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="You are not authorized to use this API")
    return api_key


@app.get('/', tags=['check'])
async def home(api_key: str=Depends(verify_api_key)):
    return {
        "app_name": APP_NAME,
        "version": VERSION,
        "status": "up & running"
    }


@app.post("/classify", tags=['NN'], response_model=PredictionResponse)
async def classify(file: UploadFile, api_key: str=Depends(verify_api_key)):
    try:
        
        # Read file
        contents = await file.read()
        response = clasify_image(image_bytes=contents)
        return response
        
    except Exception as e:
        raise HTTPException(500, f"Error making predictions: {str(e)}")
