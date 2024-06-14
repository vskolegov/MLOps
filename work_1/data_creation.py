import numpy as np
import pandas as pd
import os

# Функция для создания линейного тренда температуры
def create_linear_temperature_data(num_days=100, noise_factor=2, anomaly_factor=0.05):
    np.random.seed(42)
    days = np.arange(num_days)
    temperatures = 15 + 0.1 * days + noise_factor * np.random.randn(num_days)
    add_anomalies(temperatures, anomaly_factor)
    return pd.DataFrame({'Day': days, 'Temperature': temperatures})

# Функция для создания синусоидального тренда температуры
def create_sinusoidal_temperature_data(num_days=100, noise_factor=2, anomaly_factor=0.05):
    np.random.seed(42)
    days = np.arange(num_days)
    temperatures = 10 + 10 * np.sin(days / 365 * 2 * np.pi) + noise_factor * np.random.randn(num_days)
    add_anomalies(temperatures, anomaly_factor)
    return pd.DataFrame({'Day': days, 'Temperature': temperatures})

# Функция для создания случайного тренда температуры
def create_random_temperature_data(num_days=100, noise_factor=2, anomaly_factor=0.05):
    np.random.seed(42)
    days = np.arange(num_days)
    temperatures = 20 + noise_factor * np.random.randn(num_days)
    add_anomalies(temperatures, anomaly_factor)
    return pd.DataFrame({'Day': days, 'Temperature': temperatures})

# Функция для добавления аномалий
def add_anomalies(temperatures, anomaly_factor):
    num_days = len(temperatures)
    anomalies = int(anomaly_factor * num_days)
    anomaly_indices = np.random.choice(num_days, anomalies, replace=False)
    temperatures[anomaly_indices] += 20  # Резкие скачки температуры

# Создание обучающих и тестовых данных
def save_data():
    os.makedirs('train', exist_ok=True)
    os.makedirs('test', exist_ok=True)
    
    train_data = [
        create_linear_temperature_data(num_days=100, noise_factor=2, anomaly_factor=0.05),
        create_sinusoidal_temperature_data(num_days=100, noise_factor=2, anomaly_factor=0.1),
        create_random_temperature_data(num_days=100, noise_factor=2, anomaly_factor=0.05)
    ]
    
    test_data = [
        create_linear_temperature_data(num_days=50, noise_factor=2, anomaly_factor=0.1),
        create_sinusoidal_temperature_data(num_days=50, noise_factor=2, anomaly_factor=0.05),
        create_random_temperature_data(num_days=50, noise_factor=2, anomaly_factor=0.05)
    ]
    
    for i, data in enumerate(train_data):
        data.to_csv(f'train/train_data_{i}.csv', index=False)
    
    for i, data in enumerate(test_data):
        data.to_csv(f'test/test_data_{i}.csv', index=False)

if __name__ == "__main__":
    save_data()
