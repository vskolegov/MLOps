from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle

# Загрузка данных iris
iris = load_iris()
X, y = iris.data, iris.target

# Обучение модели логистической регрессии
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Сохранение модели в файл
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
