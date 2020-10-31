import numpy as np
import pandas as pd


classes = ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica')
dataset_name = "iris.data.csv"

###################    PREPROCESSING FUNCTIONS          ###############################################

def normalize(data):
    features = data[:, :-1].astype(float)
    features = (features - features.min(axis=0)) / features.ptp(axis=0)
    data[:, :-1] = features

    return data


def to_float(sample):
    labels_dict = dict(zip(classes, range(len(classes))))
    ys = [labels_dict[label] for label in sample[:, -1]]
    sample[:, -1] = np.array(ys)

    return sample.astype(float)


def preprocess_data(data_filename, split_ratio=0.1):
    data = pd.read_csv(data_filename, header=None).values
    data = to_float(data)
    data = normalize(data)
    np.random.shuffle(data)
    split_index = int(len(data) * split_ratio)

    return data[split_index:], data[:split_index]

######################################################################


####################        K-NN ALGO AND K-FOLD VALIDATION       ###############################

def knn(train_data, test_data, k=5):
    xs, ys = train_data[:, :-1], train_data[:, -1]
    xs_test, ys_test = test_data[:, :-1], test_data[:, -1]
    ys_pred = np.zeros(len(ys_test))

    for i, x_test in enumerate(xs_test):
        distances = np.linalg.norm(xs - x_test, axis=1)
        neighbours_indices = np.argpartition(distances, k)[:k]
        neighbours = ys[neighbours_indices].astype(int)
        ys_pred[i] = np.bincount(neighbours).argmax()

    error = 1 - np.sum(ys_pred == ys_test) / len(ys_test)
    return error


def kfold(train_data, k_param, n_folds=10):
    np.random.shuffle(train_data)
    parts = np.array_split(train_data, n_folds)
    sum_error = 0.0

    for i in range(n_folds):
        valid_sample = parts[i]
        train_sample = np.concatenate(np.delete(parts, i))
        sum_error += knn(train_sample, valid_sample, k_param)

    return sum_error / n_folds


def search_parameters(train_data, test_data, filename="errors." + dataset_name + ".txt"):
    k_range = list(range(1, 101))

    with open(filename, "w") as out:
        valid_errors = [kfold(train_data, k) for k in k_range]

        out.write("K-fold-validation errors:\n")
        for i in k_range:
            out.write(f"({i};{valid_errors[i-1]})\n")

        best_index = np.argmin(valid_errors)

        out.write(f"\nbest index = {best_index + 1}\n")

        test_errors = [knn(train_data, test_data, k) for k in k_range]

        out.write("Test errors:\n")
        for i in k_range:
            out.write(f"({i};{test_errors[i-1]})\n")

        valid_acc = 100 * (1 - valid_errors[best_index])
        test_acc = 100 * (1 - test_errors[best_index])
        print(f"Best result: k={best_index - 1}, CV accuracy = {valid_acc:0.2f}%, test accuracy = {test_acc:0.2f}%")
        out.write(f"\nBest result: k={best_index - 1}, CV accuracy = {valid_acc:0.2f}%, test accuracy = {test_acc:0.2f}%")


if __name__ == "__main__":
    train_data, test_data = preprocess_data(dataset_name)
    search_parameters(train_data, test_data)
