import random as rd
import numpy as np
from numpy.linalg import norm


class NeldelMeadSolver:
    def __init__(self, dim=3, max_iter=1000, distance_f=0.000001, distance_x=0.000001, alpha=1, beta=0.5, gamma=2):
        self.dim = dim
        self.max_iter = max_iter
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.dist_f = distance_f
        self.dist_x = distance_x


    def solve(self, func):
        n = self.dim
        # initialization
        x_arr = np.random.uniform(-4, 4, size=(n + 1, n))

        f_values = [func(x) for x in x_arr]
        x_f_arr = [[x_arr[i], f_values[i]] for i in range(len(f_values))]
        x_f_arr.sort(key=lambda x: x[1])

        for it in range(self.max_iter):
            if abs(x_f_arr[0][1] - x_f_arr[-1][1]) < self.dist_f:
                print(f'Iteration = {it}, FUNCTION VALUES CLOSE')
                break

            too_close = False
            for i in range(1, n + 1):
                if norm(x_f_arr[0][0] - x_f_arr[i][0]) < self.dist_x:
                    too_close = True
                    break
            if too_close:
                print(f'Iteration = {it}, VECTORS TOO CLOSE')
                break

            x_f_arr.sort(key=lambda x: x[1])

            x_h = x_f_arr[-1]
            x_g = x_f_arr[-2]
            x_l = x_f_arr[0]

            mid = []
            for i in range(n):
                mid.append(sum([x_f_arr[k][0][i] for k in range(n)]) / n)
            mid = np.array(mid)

            x_r = mid + self.alpha * (mid - x_h[0])
            f_r = func(x_r)
            x_r = [x_r, f_r]

            if f_r < x_l[1]:
                x_e = (1 - self.gamma) * mid + self.gamma * x_r[0]
                f_e = func(x_e)
                x_e = [x_e, f_e]
                if f_e < f_r:
                    x_f_arr[-1] = x_e
                    continue
                else:
                    x_f_arr[-1] = x_r
                    continue
            elif x_l[1] < f_r <= x_g[1]:
                x_f_arr[-1] = x_r
                continue
            elif x_g[1] < f_r < x_h[1]:
                x_r, x_h = x_h, x_r
                f_r = x_r[1]
                # x_f_arr[-1] =
            elif f_r > x_h[1]:
                pass

            x_s = self.beta * x_h[0] + (1 - self.beta) * mid
            f_s = func(x_s)
            x_s = [x_s, f_s]

            if f_s < x_h[1]:
                x_f_arr[-1] = x_s
            elif f_s >= x_h[1]:
                for i in range(1, n + 1):
                    x_f_arr[i][0] = x_f_arr[0][0] + (x_f_arr[i][0] - x_f_arr[0][0]) / 2
                    x_f_arr[i][1] = func(x_f_arr[i][0])


        return x_f_arr[0][0], x_f_arr[0][1]


if __name__ == "__main__":
    def func(a):
        res = 0
        for i in a:
            res += i * i
        return res

    def func2(a):
        return a[0]**4 + a[1]**2 + 12

    nms = NeldelMeadSolver()

    res = nms.solve(func2)
    print(res)
