#!/bin/bash

# Создание данных
python3 data_creation.py

# Предобработка данных
python3 model_preprocessing.py

# Обучение модели
python3 model_preparation.py

# Тестирование модели
python3 model_testing.py
