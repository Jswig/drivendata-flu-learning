import requests
import os

RAW_DATA_PATH = "../../data/raw/"

train_features_url = "https://s3.amazonaws.com/drivendata-prod/data/66/public/training_set_features.csv"

train_labels_url = "https://s3.amazonaws.com/drivendata-prod/data/66/public/training_set_labels.csv"

test_features_url = "https://s3.amazonaws.com/drivendata-prod/data/66/public/test_set_features.csv"

sample_sub_url = "https://s3.amazonaws.com/drivendata-prod/data/66/public/submission_format.csv"

if __name__ == "__main__":

    r = requests.get(train_features_url)
    with open(os.path.join(RAW_DATA_PATH, "train_features.csv"), 'wb') as f:
        f.write(r.content)

    r = requests.get(train_labels_url)
    with open(os.path.join(RAW_DATA_PATH, "train_labels.csv"), 'wb') as f:
        f.write(r.content)

    r = requests.get(test_features_url)
    with open(os.path.join(RAW_DATA_PATH, "test_features.csv"), 'wb') as f:
        f.write(r.content)

