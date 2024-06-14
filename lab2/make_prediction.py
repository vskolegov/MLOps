import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def make_prediction():
    # Загрузка модели
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Загрузка тестовых данных
    data_test = pd.read_csv('data_test.csv')
    X_test = data_test[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']].values
    y_test = data_test['Survived'].values

    # Прогнозирование
    y_pred = model.predict(X_test)
    
    # Анализ качества модели
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f'Accuracy: {accuracy:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')
    
    # Прогноз для первого пассажира
    prediction = model.predict(X_test[0:1])
    print(f'Prediction for the first passenger: {prediction[0]}')

if __name__ == "__main__":
    make_prediction()
