import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

def draw_plot(y_test, predictions, label):
    fpr, tpr, thresholds = metrics.roc_curve(y_test, predictions)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.plot(fpr, tpr, label=(label + ' ()'))
    plt.title("ROC curve")
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.legend(loc='best')


def make_no_categorical(data):
    dtypes = data.dtypes
    cats = dtypes[dtypes == "object"].index.tolist()  # Getting list of column names with object dtype

    lb_make = LabelEncoder()
    for i in cats:
        data[i] = lb_make.fit_transform(data[i])

    return data


def prepare_adult_dataset():
    columns = ["age", "workClass", "fnlwgt", "education", "education-num", "marital-status", "occupation",
               "relationship",
               "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"]
    train_data = pd.read_csv('data/adult.data', names=columns, sep=' *, *', na_values='?')
    test_data = pd.read_csv('data/adult.test', names=columns, sep=' *, *', skiprows=1, na_values='?')
    test_data['income'] = test_data['income'].str[:-1]              # Remove strange '.' symbol in the 'income' column

    train_data = train_data.dropna()  # Remove entries with missing values
    test_data = test_data.dropna()

    train_data.drop(['fnlwgt', 'education'], axis=1, inplace=True)  # Don't need these columns
    test_data.drop(['fnlwgt', 'education'], axis=1, inplace=True)

    train_data = make_no_categorical(train_data)
    test_data = make_no_categorical(test_data)

    x_train, y_train = train_data.iloc[:, :-1], train_data.iloc[:, [-1]]
    x_test, y_test = test_data.iloc[:, :-1], test_data.iloc[:, [-1]]
    # x_test, y_test = test_data.iloc[:, :-1], test_data.iloc[:, [-1]]

    category_col = train_data.select_dtypes(include=['object'])
    numeric_col = train_data.select_dtypes(include=['int64'])

    return x_train, y_train.values.ravel(), x_test, y_test.values.ravel(), category_col, numeric_col, train_data, test_data


if __name__ == "__main__":
    pd.set_option('display.width', 1000)  # Just for printing whole table in PyCharm
    pd.set_option('display.max_columns', 100)
    x_train, y_train, x_test, y_test, category_col, numeric_col, train_data, test_data = prepare_adult_dataset()
    # print("type ", type(test_data))

    # print('\nInfo\n')
    # test_data.info()
    #
    # print(test_data.head(3))

    print(test_data)


    # cat_cols = test_data.select_dtypes(include='object').columns
    # print(cat_cols)
    # for k, i in enumerate(cat_cols):
    #     print('iteration ', k)
    #     print(i)
    #
    # print(type(cat_cols))
    # cat_cols = cat_cols.tolist()
    # print(type(cat_cols))
    #
    #
    # print([test_data[i] for i in cat_cols])
    # # test_data[cat_cols] = test_data[cat_cols].cat.codes
    # # *[test_data[i] for i in cat_cols] = map(lambda x: x.cat.codes, [test_data[i] for i in cat_cols])
    # # map(lambda x: x.cat.codes, [test_data[i] for i in cat_cols])
    # for i in cat_cols:
    #     print(i)
    #     test_data[i] = test_data[i].cat.codes
    #
    # print(test_data.head())