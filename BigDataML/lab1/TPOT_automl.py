from tpot import TPOTClassifier
from prepare_data import prepare_adult_dataset
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

def run_automl_tpot(x_train, y_train, gener=3, verb=2, popul=8, cv=None):

    clf = TPOTClassifier(generations=gener, verbosity=verb, population_size=popul, scoring='roc_auc', cv=cv,
                         random_state=23)
    clf.fit(x_train.values, y_train)
    return clf


if __name__ == "__main__":
    x_train, y_train, x_test, y_test, category_col, numeric_col, train_data, test_data = prepare_adult_dataset()
    clf = run_automl_tpot(x_train, y_train)

    predictions = clf.predict(x_test)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, predictions)

    plt.plot([0, 1], [0, 1], 'k--')
    plt.plot(fpr, tpr, label=('TPOT'))
    plt.title("ROC curve")
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')

    plt.show()
    # print(score)
