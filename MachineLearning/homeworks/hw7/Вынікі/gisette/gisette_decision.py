import os
import numpy as np
import pandas as pd
from collections import namedtuple
from subprocess import call
from svmutil import *
from liblinear_.python import liblinearutil

def save_libsvm(raw_data, filename):
    x = raw_data[:, :-1]
    y = raw_data[:, -1].astype(int)
    lines = []
    for features, label in zip(x, y):
        sparse_features = [f"{i + 1}:{value}" for i, value in enumerate(features) if value != 0]
        line = ' '.join([str(label)] + sparse_features) + '\n'
        lines.append(line)
    with open(filename, 'w') as f:
        f.writelines(lines)


def transform_gisette_data(data_dir, save_dir, base_name):
    os.makedirs(save_dir, exist_ok=True)
    data_path = os.path.join(data_dir, base_name)
    x = pd.read_csv(data_path + '.data', delim_whitespace=True, header=None).values
    y = pd.read_csv(data_path + '.labels', delim_whitespace=True, header=None).values
    save_libsvm(np.hstack((x, y)), os.path.join(save_dir, base_name))


def liblinear_options(svm_type=1, cost=1.0, eps=0.0001):
    return f"-s {svm_type} -c {cost} -e {eps} -q"


def split(index, arr, part_size):
    validation_part = arr[index: (index + 1) * part_size]
    train_part = arr[:index * part_size] + arr[(index + 1) * part_size:]
    return train_part, validation_part


def kfold(x, y, parameters, train_func, predict_func, k=10):
    part_size = len(y) // k
    errors = []
    for i in range(k):
        x_train, x_valid = split(i, x, part_size)
        y_train, y_valid = split(i, y, part_size)

        model = train_func(y_train, x_train, parameters)
        _, results, _ = predict_func(y_valid, x_valid, model, '-q')
        errors.append(1 - results[0] / 100)
    return np.mean(errors), np.std(errors)


GisetteResult = namedtuple('GisetteResult', ['cost', 'error'])


def search_gisette_parameters(x, y):
    best_result = GisetteResult(None, error=1.0)
    log_costs = list(range(-15, 3))
    errors_stdevs = []

    for cost in map(lambda a: 2 ** a, log_costs):
        print(cost)
        error, std = kfold(x, y, liblinear_options(cost=cost), liblinearutil.train, liblinearutil.predict, k=5)
        if error < best_result.error:
            best_result = GisetteResult(cost, error)
        errors_stdevs.append((cost, error, std))

    return best_result, errors_stdevs



if __name__ == "__main__":
    ############ Code just for 1st run #####################
    data_dir = 'GISETTE'
    gisette_save_dir = 'gisette_tmp'
    # transform_gisette_data(data_dir, gisette_save_dir, 'gisette_train')
    # transform_gisette_data(data_dir, gisette_save_dir, 'gisette_valid')

    # here we use some bash command for scaling
    # ..\..\libsvm-3.24\windows\svm-scale.exe -l 0 -s scaling_params gisette_train > train_scaled
    # ..\..\libsvm-3.24\windows\svm-scale.exe -r scaling_params gisette_valid 1> valid_scaled
    #################################################################

    ################### Searching for best parameters #######################
    y_train, x_train = svm_read_problem(os.path.join(gisette_save_dir, 'train_scaled'))
    # best, all_errors = search_gisette_parameters(x_train, y_train)
    # print("all errors:" + "\n".join([str(er) for er in all_errors]))
    # print("BEST:", best)
    # print(f"Validation accuracy: {100 * (1 - best.error)}%")
    #################################################################

    y_valid, x_valid = svm_read_problem(os.path.join(gisette_save_dir, 'valid_scaled'))

    for log_c in [-8, -7]:
        model = liblinearutil.train(y_train, x_train, liblinear_options(cost=2 ** log_c))
        _, results, _ = liblinearutil.predict(y_valid, x_valid, model, '-q')
        print(f"log2(C) = {log_c}: Test accuracy = {results[0]}%, error = {1 - results[0] / 100}")
