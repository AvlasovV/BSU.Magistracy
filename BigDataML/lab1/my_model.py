from prepare_data import prepare_adult_dataset, draw_plot
import matplotlib.pyplot as plt
import pandas

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

import numpy as np

def run_random_forest(x_train, y_train):
    rand_forest = RandomForestClassifier(criterion='entropy', max_depth=20, max_features='auto', min_samples_leaf=2, bootstrap=True)
    param_grid = {
        'n_estimators': [50, 100, 200],
        'min_samples_split': [2, 5, 10],
        'bootstrap': [True, False]
    }

    cv_rfc = GridSearchCV(estimator=rand_forest, verbose=1, param_grid=param_grid, cv=5)
    cv_rfc.fit(x_train, y_train)
    return cv_rfc

if __name__ == "__main__":
    x_train, y_train, x_test, y_test, category_col, numeric_col, train_data, test_data = prepare_adult_dataset()
    forest_predictions = run_random_forest(x_train, y_train).predict(x_test)
    draw_plot(y_test, forest_predictions, f'Logistic Regression (AUC = {roc_auc_score(y_test, forest_predictions)}')
    plt.show()



