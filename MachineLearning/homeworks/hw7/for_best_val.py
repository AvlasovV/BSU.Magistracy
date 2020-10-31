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
    return np.mean(errors), np.std(errors), model


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

C = 2 ** 8
error_values = {}

with open("results\\error_for_best_values.txt", "w") as out_res:
    for d in range(1, 10):

        error_values[d] = []

        print(f"d = {d}")
        out_res.write(f"d = {d}")

        params = f'-t 1 -d {d} -c {C} -r 1 -q'

        param = svmutil.svm_parameter(params)

        err, std, model = kfold(x_train, y_train, params, svmutil.svm_train, svmutil.svm_predict)
        error_values[d].append(err)
        print("Err on validation: ", err, std)

        if best_err_cross > err:
            best_err_cross = err
            best_params_cross = d

        _, results, _ = svmutil.svm_predict(y_test, x_test, model, "-q")
        err_test = (1 - results[0] / 100)
        error_values[d].append(err_test)



        print(f"d = {d}, cross-validation {err}, test_error {err_test}\n")
        out_res.write(f"d = {d}, cross-validation {err}, test_error {err_test}\n")

    out_res.write(f"\nBest accuracy on cross validation = {1-best_err_cross}, parameter d = {best_params_cross}")


print(error_values)

with open("results\\errors_for_best_c.txt", "w") as f:
    for d in error_values:
            f.write(str(d) + " " + " ".join(str(m) for m in error_values[d]) + "\n")


print(f"Best accuracy on cross validation = {1-best_err_cross}, parameters d, k = {best_params_cross}")


vectors = {}
for d in range(1, 10):
    params = f'-t 1 -d {d} -c {C} -r 1 -q'
    model = svmutil.svm_train(y_train, x_train, params)
    vectors[d] = model.get_nr_sv()

for v in vectors:
    print(f"({v};{vectors[v]})")


