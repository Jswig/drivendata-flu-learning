import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

import pandas as pd
import os
import numpy as np

from sklearn.model_selection import cross_validate
from models import get_lr_model

DATA_PATH = '../data/raw'
FIG_PATH = '../paper/figures'

if __name__ == "__main__":
    mpl.rcParams.update({
        'figure.autolayout': True,
        'figure.dpi': 150
    })
    sns.set()

    X_train = pd.read_csv(
        os.path.join(DATA_PATH, 'training_set_features.csv')
    ).drop('respondent_id',axis =1)
    y_train = pd.read_csv(
        os.path.join(DATA_PATH, 'training_set_labels.csv')
    ).drop('respondent_id',axis =1)

    Cs = np.logspace(-2, 1, num = 10, base = 10)
    means = []
    stds = []
    best_auc = 0
    for C in Cs:
        cv = cross_validate(
            estimator = get_model(C),
            X = X_train,
            y = y_train,
            cv = 5,
            n_jobs = -1,
            scoring = 'roc_auc',
        )
        means.append(np.mean(cv['test_score']))
        stds.append(np.std(cv['test_score']))
        if means[-1] > best_auc:
            best_C = C
            best_auc = means[-1]    

    fig, ax = plt.subplots()
    ax.plot(Cs, means)
    ax.vlines(best_C, ymin = 0.82, ymax = 0.86,  colors = 'r', linestyle = 'dotted')
    ax.annotate("$C = 0.464$ \n ROC AUC = 0.843", xy = (0.5, 0.835))
    ax.set_xscale('log')
    ax.set_xlabel('$C$')
    ax.grid(axis = 'x')
    ax.legend(['AUC', 'best $C$'])
    ax.set_title('AUC for different values of $C$')
    fig.savefig(os.path.join(FIG_PATH, 'lr_reg_performance.png')