import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib
import os
import numpy as np

def test_model():
    model = joblib.load('model.pkl')
    X_test = []
    y_test = []
    
    for filename in os.listdir('test_preprocessed'):
        if filename.endswith('.csv'):
            data = pd.read_csv(os.path.join('test_preprocessed', filename))
            X_test.append(data[['Day']].values)
            y_test.append(data['Temperature'].values)
    
    X_test = np.vstack(X_test)
    y_test = np.concatenate(y_test)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

if __name__ == "__main__":
    test_model()
