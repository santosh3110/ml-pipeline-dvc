import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import yaml


def load_data(data_url: str) -> pd.DataFrame:
    try:
        df=pd.read_csv(data_url)
        return df
    except Exception as e:
        print('An Unexpected Error occured while loading the data')
        print(e)

def preprocessing_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df.drop(columns="tweet_id", axis=1, inplace=True)
        final_df=df[df['sentiment'].isin(['happiness','sadness'])]
        final_df['sentiment'].replace({'happiness':1, 'sadness':0}, inplace=True)
        return final_df
    except KeyError as e:
        print(f"Error: Missing column {e} in the dataframe.")
        raise
    except Exception as e:
        print(f'Error: An unexpected error occured during data preprocessing.')
        print(e)
        raise

def save_data(train_data: pd.DataFrame, test_data: pd.DataFrame, data_path: str) -> None:
    try:
        data_path = os.path.join(data_path, 'raw')
        os.makedirs(data_path, exist_ok=True)
        train_data.to_csv(os.path.join(data_path, "train.csv"), index=False)
        test_data.to_csv(os.path.join(data_path, "test.csv"), index=False)
    except Exception as e:
        print(f"Error: An unexpected error occurred while saving the data.")
        print(e)
        raise


def main():
    try:
        df = load_data(data_url='https://raw.githubusercontent.com/entbappy/Branching-tutorial/refs/heads/master/tweet_emotions.csv')
        final_df = preprocessing_data(df)
        train_data, test_data = train_test_split(final_df, test_size=0.2, random_state=42)
        save_data(train_data, test_data, data_path='data')
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to complete the data ingestion process.")

if __name__ == '__main__':
    main()





