FROM python:3.9

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

RUN python train_model.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
