from matplot import *

errors = {}
with open("results\\errors_for_plots.txt", "r") as f:
    for line in f:
        if line != "":
            d, k, err, std = [float(x) for x in line.split()]
            print(d, k, err, std)