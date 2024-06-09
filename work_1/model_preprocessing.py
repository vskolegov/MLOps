import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def preprocess_data(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            data = pd.read_csv(os.path.join(input_folder, filename))
            scaler = StandardScaler()
            scaled_data = scaler.fit_transform(data[['Day', 'Temperature']])
            scaled_df = pd.DataFrame(scaled_data, columns=['Day', 'Temperature'])
            scaled_df.to_csv(os.path.join(output_folder, filename), index=False)

if __name__ == "__main__":
    preprocess_data('train', 'train_preprocessed')
    preprocess_data('test', 'test_preprocessed')
