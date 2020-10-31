import sys
import numpy as np
import scipy
import svmutil
import svm
from math import sqrt
import pandas as pd
from collections import namedtuple


def split(index, arr, part_size):
    if not isinstance(arr, np.ndarray):
        arr = arr.toarray()
    # print("Shape", arr.shape())
    # print(arr)
    validation_part = arr[index: (index + 1) * part_size]
    # print("VALIDATION PART=",validation_part)
    a1 = arr[ : index * part_size]
    # print(a1, type(a1))
    a2 = arr[(index + 1) * part_size : ]

    # train_part = a1 + a2
    train_part = np.concatenate((a1,a2))
    return train_part, validation_part


def kfold(x, y, parameters, train_func, predict_func, K_fold=10):
    part_size = len(y) // K_fold
    errors = []
    for i in range(1, K_fold):
        x_trn, x_valid = split(i, x, part_size)
        y_trn, y_valid = split(i, y, part_size)

        model = train_func(y_trn, x_trn, parameters)
        _, results, _ = predict_func(y_valid, x_valid, model, '-q')
        errors.append(1 - results[0] / 100)
    return np.mean(errors), np.std(errors)


input_name = sys.argv[-1]

y, x = svmutil.svm_read_problem(input_name, return_scipy=True)

y_train, y_test = y[:3451], y[3451:]
x_train, x_test = x[:3451], x[3451:]

# print(x_train)
# print(y_train)

param = svmutil.csr_find_scale_param(x_train, lower=0)
x_train = svmutil.csr_scale(x_train, param)

x_test = svmutil.csr_scale(x_test, param)


best_err_cross = 1.
best_params_cross = None
# best_acc_predict = 0
# best_params_predict = None

prob = svmutil.svm_problem(y_train, x_train)

K = 8
error_values = {}



with open("results\\10_fold_valid.txt", "w") as out_res:
    for d in [1, 2, 3, 4]:
    # for d in [1, 2]:
        error_values[d] = {}

        # for k in range(4, K+1):
        for k in range(-K, K+1):
            print(f"K = {k}, d = {d}")
            out_res.write(f"K = {k}, d = {d}")

            params = f'-t 1 -d {d} -c {2**k} -r 1 -q'

            param = svmutil.svm_parameter(params)
            # prob = svmutil.svm_problem(y_train, x_train)

            err, std = kfold(x_train, y_train, params, svmutil.svm_train, svmutil.svm_predict)
            error_values[d][k] = (err, std)
            print(err, std)

            if best_err_cross > err:
                best_err_cross = err
                best_params_cross = (d, k)

            print(f"K = {k}, d = {d}, cross-validation {err, std}\n")
            out_res.write(f"K = {k}, d = {d}, cross-validation {err, std}\n")

    out_res.write(f"\nBest accuracy on cross validation = {1-best_err_cross}, parameters d, k = {best_params_cross}")


print(error_values)

with open("results\\8_errors.txt", "w") as f:
    for d in error_values:
        for k in error_values[d]:
            f.write(str(d) + " " + str(k) + " " + " ".join(str(m) for m in error_values[d][k]) + "\n")


print(f"Best accuracy on cross validation = {1-best_err_cross}, parameters d, k = {best_params_cross}")


# print(f"x_train_len = {x_train.shape}\n", x_train)
# print(f"x_test_len = {x_test.shape}\n", x_test)

# data = np.loadtxt(input_name, delimiter=",")
#
# train_set = data[:3451]
# test_set = data[3451:]
#
# train_csr = scipy.sparse.csr_matrix(train_set)
# test_csr = scipy.sparse.csr_matrix(test_set)
#
# param = svmutil.csr_find_scale_param(train_csr)
# scaled_train = svmutil.csr_scale(train_csr, param)
# scaled_test = svmutil.csr_scale(test_csr, param)


# with open(input_name, "r") as f, open(output_name, "w") as out:
#     for i in f:
#         features = i.split(",")
#
#         if features[-1] == 1:
