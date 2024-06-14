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

    # Обработка данных
    df['Sex'] = df['Sex'].apply(lambda x: 0 if x == 'male' else 1)
    df['Age'] = df['Age'].fillna(df['Age'].mean())

    # Нормализация и стандартизация данных
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])

    # Разделение на тренировочный и тестовый наборы данных
    train = df.sample(frac=0.8, random_state=42)
    test = df.drop(train.index)

    # Сохранение данных
    train[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Survived']].to_csv('data_train.csv', index=False)
    test[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']].to_csv('data_test.csv', index=False)

if __name__ == "__main__":
    create_dataset()
