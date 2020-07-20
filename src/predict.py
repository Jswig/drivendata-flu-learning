import pandas as pd
import os
from models import get_lr_model


DATA_PATH = '../../data/raw'
PRED_PATH = '../output/'

if __name__ == "__main__":

    X_train = pd.read_csv(
        os.path.join(DATA_PATH, 'training_set_features.csv')
    ).drop('respondent_id',axis =1)

    X_test = pd.read_csv(
        os.path.join(DATA_PATH, 'test_set_features.csv')
    ).drop('respondent_id',axis =1)

    y_train = pd.read_csv(
        os.path.join(DATA_PATH, 'training_set_labels.csv')
    ).drop('respondent_id',axis =1)

    sub = pd.read_csv(os.path.join(DATA_PATH, 'submission_format.csv'))

    model = get_lr_model(1)
    model.fit(X_train, y_train)
    preds = model.predict_proba(X_test)

    sub['h1n1_vaccine'] = preds[0][:,1]
    sub['seasonal_vaccine'] = preds[1][:,1]
    sub.to_csv(os.path.join(PRED_PATH, 'baseline_pred.csv'), index = False)