from prepare_data import draw_plot, prepare_adult_dataset
from my_model import run_random_forest
from TPOT_automl import run_automl_tpot
from h2o_automl import run_automl_h2o
from sklearn.metrics import roc_auc_score

import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import h2o


"""Our data frames"""

x_train, y_train, x_test, y_test, category_col, numeric_col, train_data, test_data = prepare_adult_dataset()


print("\n**************** TPOT AUTO ML **********************\n")
tpot_clf = run_automl_tpot(x_train, y_train)
tpot_predictions = tpot_clf.predict(x_test)

draw_plot(y_test, tpot_predictions, f'TPOT (AUC = {roc_auc_score(y_test, tpot_predictions)}')


print("\n**************** H2O AUTO ML **********************\n")
model = run_automl_h2o()
h2o_x_test = h2o.H2OFrame(x_test)
predictions = model.predict(h2o_x_test)
y_predict = predictions[:, 0].as_data_frame().values

draw_plot(y_test, y_predict, f'H2O (AUC = {roc_auc_score(y_test, y_predict)}')


print("\n**************** RandomForest Grid **********************\n")
forest_predictions = run_random_forest(x_train, y_train).predict(x_test)

draw_plot(y_test, forest_predictions, f'Random Forest (AUC = {roc_auc_score(y_test, forest_predictions)}')

plt.show()
