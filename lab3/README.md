# Iris Prediction API

This project implements a simple API for predicting Iris species based on the famous Iris dataset using a machine learning model. The API is built with FastAPI and deployed using Docker.

## Getting Started


   ```sh
   git clone https://github.com/vskolegov/MLOps.git
   cd MLOps/lab2
```

```sh
docker build -t iris_model_api .
```

```sh
docker run -d -p 8000:8000 iris_model_api
```

## Using the API

Open your browser and go to http://localhost:8000/docs

Input sample
```json
{
  "sepal_length": 5.0,
  "sepal_width": 3.5,
  "petal_length": 1.5,
  "petal_width": 0.2
}
```
Output sample
```json
{
  "prediction": "Iris-setosa"
}
```
<img width="414" alt="image" src="https://github.com/vskolegov/MLOps/assets/76074529/9d84b066-57da-4286-8906-78d03533181d">
<img width="416" alt="image" src="https://github.com/vskolegov/MLOps/assets/76074529/de17b436-8e46-44c4-88f6-db0b410b61c9">
