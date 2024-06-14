from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Список классов
class_labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

# Загрузка модели
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None

# Создание приложения FastAPI
app = FastAPI()

# Определение модели данных для предсказаний с использованием ползунков
class IrisData(BaseModel):
    sepal_length: float = Field(..., ge=4.0, le=8.0, description="Длина чашелистика (4.0 - 8.0)")
    sepal_width: float = Field(..., ge=2.0, le=5.0, description="Ширина чашелистика (2.0 - 5.0)")
    petal_length: float = Field(..., ge=1.0, le=7.0, description="Длина лепестка (1.0 - 7.0)")
    petal_width: float = Field(..., ge=0.1, le=2.5, description="Ширина лепестка (0.1 - 2.5)")

@app.post("/predict")
def predict(data: IrisData):
    try:
        if model is None:
            raise HTTPException(status_code=500, detail="Model not loaded")
        # Подготовка данных для модели
        input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
        # Получение предсказания
        prediction = model.predict(input_data)
        # Получение названия класса
        class_name = class_labels[int(prediction[0])]
        return {"prediction": class_name}
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail=str(e))
