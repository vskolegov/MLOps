import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model():
    # Загрузка тренировочных данных
    data_train = pd.read_csv('data_train.csv')
    X_train = data_train[['Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard']].values
    y_train = data_train['Survived'].values

    # Обучение модели
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Сохранение модели
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model()
