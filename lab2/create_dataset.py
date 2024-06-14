import pandas as pd
import requests
from sklearn.preprocessing import StandardScaler
import io

def create_dataset():
    # URL для скачивания данных
    url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'

    # Загрузка данных
    response = requests.get(url)
    data = response.content.decode('utf-8')

    # Чтение данных в DataFrame
    df = pd.read_csv(io.StringIO(data))

    # Вывод заголовка DataFrame для проверки
    print(df.head())

    # Проверка наличия необходимых столбцов
    required_columns = ['Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Survived']
    for column in required_columns:
        if column not in df.columns:
            raise KeyError(f"Column '{column}' not found in data")

    # Обработка данных
    df['Sex'] = df['Sex'].apply(lambda x: 0 if x == 'male' else 1)
    df['Age'] = df['Age'].fillna(df['Age'].mean())

    # Нормализация и стандартизация данных
    features = ['Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard']
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])

    # Разделение на тренировочный и тестовый наборы данных
    train = df.sample(frac=0.8, random_state=42)
    test = df.drop(train.index)

    # Сохранение данных
    train[required_columns].to_csv('data_train.csv', index=False)
    test[required_columns].to_csv('data_test.csv', index=False)

if __name__ == "__main__":
    create_dataset()
