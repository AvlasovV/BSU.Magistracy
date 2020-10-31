from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import random as rd


K = 3
ITERATIONS = 80
D = 6
N = 1000
S = np.arange(1, 10, 0.5)


def generate_item(s, i, d):
    mean = np.zeros(d)
    mean[i] = s
    cov = np.identity(d)
    return np.random.multivariate_normal(mean, cov, 1)[0]
    # return np.random.normal(size=(n, d))


def generate_data(s, n=N, k=K, d=D):
    labels = np.random.choice(k, n)
    return labels, np.array([generate_item(s, i, d) for i in labels])


def initialize_centroids(data, k=K):
    centr = np.array([]).reshape(data.shape[1], 0)
    for k in range(K):
        rand = rd.randint(0, N - 1)
        centr = np.c_[centr, X[rand]]
    return centr


def get_distance(data, centroids,  k=K):
    euclid_dist = np.array([]).reshape(data.shape[0], 0)
    for l in range(k):
        temp_dist = np.sum((X - centroids[:, l]) ** 2, axis=1)
        euclid_dist = np.c_[euclid_dist, temp_dist]

    cluster_vals = np.argmin(euclid_dist, axis=1) + 1
    # print(cluster_vals)
    return cluster_vals


def k_means(data, labels, centroids=None, n_iter=ITERATIONS, k=K):
    if not centroids:
        centroids = initialize_centroids(data, k)

    data_len = data.shape[0]
    data_dim = data.shape[1]
    # print(data_dim)
    output = {}

    for iter in range(n_iter):

        cluster_vals = get_distance(data, centroids, k)
        curr_classes = {}

        for i in range(k):
            curr_classes[i + 1] = np.array([]).reshape(data_dim, 0)

        for i in range(data_len):
            curr_classes[cluster_vals[i]] = np.c_[curr_classes[cluster_vals[i]], data[i]]

        for i in range(k):
            curr_classes[i + 1] = curr_classes[i + 1].T

        for i in range(k):
            centroids[:, i] = np.mean(curr_classes[i + 1], axis=0)
        output = curr_classes

    ## Real govnokode
    variants = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    temp_labels = labels
    max_accuracy = 0
    for var in variants:
        for l in range(len(labels)):
            temp_labels[l] = var[labels[l]-1]
        acc = sum([1 if cluster_vals[i] == temp_labels[i] else 0 for i in range(data_len)]) / data_len
        if max_accuracy < acc:
            max_accuracy = acc

    print(f"Accuracy = {max_accuracy}")

    return output, centroids, max_accuracy


def draw_unclustered(data):
    """For d=2"""
    plt.scatter(data[:, 0], data[:, 1], c='black', label='unclustered data')
    plt.title('Plot of data points')
    plt.show()


def draw_clustered(data, centroids):
    """For d = 2, k = 3"""
    color = ['red', 'blue', 'green']
    labels = ['cluster1', 'cluster2', 'cluster3']
    for k in range(K):
        plt.scatter(data[k + 1][:, 0], data[k + 1][:, 1], c=color[k], label=labels[k])
    plt.scatter(centroids[0, :], centroids[1, :], s=300, c='yellow', label='Centroids')
    plt.legend()
    plt.show()


def acc_plot(x, y):
    plt.rcParams["figure.figsize"] = (20,17)
    plt.plot(x, y)
    plt.xlabel('S')
    plt.ylabel('accuracy')
    plt.show()
    # plt.imsave("figure", format="png")
    plt.savefig("figure.png")

if __name__ == "__main__":

    Y, X = generate_data(1, N)


    # draw_unclustered(X)

    # clustered_data, centroids, acc = k_means(X, Y)
    print()
    print(Y)
    # draw_clustered(clustered_data, centroids)
    accuracy = []

    with open("acc_res_best.txt", "w") as f:
        for s in S:
            max_acc = 0
            for _ in range(10):
                Y, X = generate_data(s, N)
                clustered_data, centroids, acc = k_means(X, Y)
                if max_acc < acc:
                    max_acc = acc
            accuracy.append(max_acc)
            f.write(f"s={s}, acc = {max_acc}")
    acc_plot(S, accuracy)

