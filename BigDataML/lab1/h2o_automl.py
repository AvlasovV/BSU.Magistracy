import h2o
from h2o.automl import H2OAutoML

from prepare_data import prepare_adult_dataset,draw_plot
import matplotlib.pyplot as plt

from sklearn.metrics import roc_auc_score

def run_automl_h2o(max_models=10):
    """
    h2o instance should be running
    :return: the path of the best model
    """
    h2o.init()
    *_, train_data, test_data = prepare_adult_dataset()
    train_data = h2o.H2OFrame(train_data)
    test_data = h2o.H2OFrame(test_data)


    y_col = 'income'
    x_cols = train_data.columns.remove(y_col)
    train_data[y_col] = train_data[y_col].asfactor()
    test_data[y_col] = test_data[y_col].asfactor()

    aml = H2OAutoML(max_models=max_models, seed=1)
    aml.train(x=x_cols, y=y_col, training_frame=train_data)

    lead_board = aml.leaderboard
    print("\n*********************** H2O AUTOML LEADERBOARD *****************************")
    print(lead_board.head(rows=lead_board.nrows))

    # return h2o.save_model(aml.leader, path="h2o.leader.model")
    return aml.leader


if __name__ == "__main__":
    model = run_automl_h2o()

    x_train, y_train, x_test, y_test, category_col, numeric_col, train_data, test_data = prepare_adult_dataset()

    h2o_x_test = h2o.H2OFrame(x_test)
    h2o_test = h2o.H2OFrame(test_data)

    predictions = model.predict(h2o_x_test)
    y_predict = predictions[:, 0].as_data_frame().values

    # h2o_perf = model.model_performance(h2o_test)
    print(predictions.head())
    draw_plot(y_test, y_predict, f'Random Forest (AUC = {roc_auc_score(y_test, y_predict)}')
    plt.show()