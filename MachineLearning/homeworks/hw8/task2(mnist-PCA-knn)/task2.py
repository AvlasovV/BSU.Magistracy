import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.manifold import TSNE
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import fetch_mldata

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from mnist import MNIST



# def knn_sklearn(x_train, y_train, x_test, y_test):
#     classifier = KNeighborsClassifier(n_neighbors=3)
#     classifier.fit(x_train, y_train)
#     return metrics.accuracy_score(y_test, classifier.predict(x_test))


def knn(xs, ys, xs_test, ys_test, k=5):
    # xs, ys = train_data[:, :-1], train_data[:, -1]
    # xs_test, ys_test = test_data[:, :-1], test_data[:, -1]
    ys_pred = np.zeros(len(ys_test))

    for i, x_test in enumerate(xs_test):
        distances = np.linalg.norm(xs - x_test, axis=1)
        neighbours_indices = np.argpartition(distances, k)[:k]
        neighbours = ys[neighbours_indices].astype(int)
        ys_pred[i] = np.bincount(neighbours).argmax()

    error = 1 - np.sum(ys_pred == ys_test) / len(ys_test)
    return error



def pca_transform(data, n_dims):
    data -= np.mean(data, axis=0)
    U, s, _ = np.linalg.svd(data.T, full_matrices=False)
    U = U[:, :n_dims]
    return np.dot(data, U), U


def pca_recover(pca_data, U, mean):
    data = np.dot(pca_data, U.T)
    data += mean
    return data


if __name__ == "__main__":


    mndata = MNIST('.\\all_data', return_type="numpy", gz=True)
    mndata.gz = True

    x_train, y_train = mndata.load_training()
    print("loaded train")

    x_test, y_test = mndata.load_testing()
    print("loaded test")


    # x_train, x_test = np.array(x_train), np.array(x_test)
    # y_train, y_test = y_train[1], y_test[1]
    # init_acc = knn_sklearn(x_train, y_train, x_test, y_test)

    init_acc = knn(x_train, y_train, x_test, y_test, 3)
    print(f"Initial accuracy = {init_acc:.3f}")

    compressed_accs, recovered_accs = [], []
    dims_range = [5, 10, 20, 50, 100]
    with open("accuracy.txt", "w") as out:
        for n_dims in dims_range:
            print("n_dims=", n_dims)
            pca_train, U = pca_transform(x_train, n_dims)
            pca_test = np.dot(x_test, U)
            compressed_accs.append(knn(pca_train, y_train, pca_test, y_test, 3))
            out.write(f"n_dims = {n_dims}, compressed accuracy = {compressed_accs[-1]}\n")

            recovered_train = pca_recover(pca_train, U, np.mean(x_train, axis=0))
            recovered_test = np.dot(pca_test, U.T)
            recovered_accs.append(knn(recovered_train, y_train, recovered_test, y_test, 3))
            out.write(f"n_dims = {n_dims}, recovered accuracy = {recovered_accs[-1]}\n")
            out.write("\n")
