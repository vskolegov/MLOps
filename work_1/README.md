# Описание
Это простая демонстрация конвейера машинного обучения.
Он создает тестовые и тренировочные данные погоды, затем их обрабатывает и обучает модель.

# Запуск скрипта

bash pipeline.sh

# Pipeline 
```mermaid
graph TD
    A[Data Creation] --> B[Data Preprocessing]
    B --> C[Model Training]
    C --> D[Model Testing]

```