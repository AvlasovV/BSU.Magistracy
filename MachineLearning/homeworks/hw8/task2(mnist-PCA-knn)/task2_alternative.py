import numpy as np

from mnist import MNIST
from sklearn import decomposition


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


if __name__ == "__main__":

    mndata = MNIST('.\\all_data', return_type="numpy", gz=True)
    mndata.gz = True

    x_train, y_train = mndata.load_training()
    print("loaded train")

    x_test, y_test = mndata.load_testing()
    print("loaded test")

    x_train = x_train[30000:40000]
    y_train = y_train[30000:40000]

    x_test = x_test[5000:7000]
    y_test = y_test[5000:7000]

    # x_train, x_test = np.array(x_train), np.array(x_test)
    # y_train, y_test = y_train[1], y_test[1]
    # init_acc = knn_sklearn(x_train, y_train, x_test, y_test)

    # init_acc = knn(x_train, y_train, x_test, y_test, 8)
    # print(f"Initial accuracy = {init_acc}")
    # exit()

    compressed_accs, recovered_accs = [], []
    dims_range = [5, 10, 20] + list(range(50, 500, 50))
    with open("accuracy_alternate.txt", "w") as out:
        for n_dims in dims_range:
            print("n_dims=", n_dims)

            # pca_train, U = pca_transform(x_train, n_dims)
            # pca_test = np.dot(x_test, U)
            pca = decomposition.PCA(n_components=n_dims)
            pca.fit(x_train)
            pca_train = pca.transform(x_train)
            pca_test = pca.transform(x_test)

            compressed_accs.append(knn(pca_train, y_train, pca_test, y_test, 10))
            print(f"n_dims = {n_dims}, compressed accuracy = {1-compressed_accs[-1]}\n")
            out.write(f"n_dims = {n_dims}, compressed accuracy = {1-compressed_accs[-1]}\n")


            # recovered_train = pca_recover(pca_train, U, np.mean(x_train, axis=0))
            # recovered_test = np.dot(pca_test, U.T)
            recovered_train = pca.inverse_transform(pca_train)
            recovered_test = pca.inverse_transform(pca_test)
            print(recovered_train.shape)

            # recovered_accs.append(knn(recovered_train, y_train, recovered_test, y_test, 10))
            # print(f"n_dims = {n_dims}, recovered accuracy = {recovered_accs[-1]}\n")
            # out.write(f"n_dims = {n_dims}, recovered accuracy = {recovered_accs[-1]}\n")
            out.write("\n")

        for i, n_dims in enumerate(dims_range):
            out.write(f"({n_dims};{1-compressed_accs[i]})")
