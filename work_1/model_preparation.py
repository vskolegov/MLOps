import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os
import numpy as np

def train_model():
    X_train = []
    y_train = []
    
    for filename in os.listdir('train_preprocessed'):
        if filename.endswith('.csv'):
            data = pd.read_csv(os.path.join('train_preprocessed', filename))
            X_train.append(data[['Day']].values)
            y_train.append(data['Temperature'].values)
    
    X_train = np.vstack(X_train)
    y_train = np.concatenate(y_train)

    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, 'model.pkl')

if __name__ == "__main__":
    train_model()
