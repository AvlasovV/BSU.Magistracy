#!/usr/bin/env python3
import cv2
import numpy as np
import sys
import os
import math
import time

folder = sys.argv[-2]
model = sys.argv[-1]


class PreProcessing:
    """Class for some image preprocessing"""
    @staticmethod
    def read_file(fname):
        image = cv2.imread(fname)
        # print("Image:\n", image, "\n")
        assert image.shape == (26, 40, 3)
        return image[:, :, 0]

    @staticmethod
    def get_integral_image(image, ):
        rows, cols = image.shape
        sum = np.zeros((rows, cols), np.int32)
        image_integral = cv2.integral(image, sum, -1)
        return image_integral[1:, 1:]


class Features:
    """Class with all features"""
    def __init__(self):
        self.features = [func for func in dir(Features) if
                         callable(getattr(Features, func)) and not func.startswith(
                             "__") and func != "get_rectangle_sum"]

    @staticmethod
    def get_rectangle_sum(image, lu_x, lu_y, height, width):
        try:
            rect_sum = image[lu_y][lu_x] + image[lu_y + height - 1][lu_x + width - 1] \
                       - image[lu_y + height - 1][lu_x] - image[lu_y][lu_x + width - 1]
            return rect_sum
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            print(f"If no args, {lu_x, lu_y, height, width}")

    @staticmethod
    def two_rectangles_horizontal_split(image, lu_x, lu_y, height, width):
        assert lu_x + width <= 40 and lu_y + height <= 26, f"Wrong offset or size, {lu_x, lu_y, height, width}"
        height //= 2
        upper_rect_sum = Features.get_rectangle_sum(image, lu_x, lu_y, height, width)
        lower_rect_sum = Features.get_rectangle_sum(image, lu_x, lu_y + height, height, width)
        return upper_rect_sum - lower_rect_sum

    @staticmethod
    def two_rectangles_vertical_split(image, lu_x, lu_y, height, width):
        assert lu_x + width <= 40 and lu_y + height <= 26, f"Wrong offset or size, {lu_x, lu_y, height, width}"
        width //= 2
        left_rect_sum = Features.get_rectangle_sum(image, lu_x, lu_y, height, width)
        right_rect_sum = Features.get_rectangle_sum(image, lu_x + width, lu_y, height, width)
        return left_rect_sum - right_rect_sum

    @staticmethod
    def three_rectangles_horizontal_split(image, lu_x, lu_y, height, width):
        assert lu_x + width <= 40 and lu_y + height <= 26, f"Wrong offset or size, {lu_x, lu_y, height, width}"
        height //= 3
        upper_sum = Features.get_rectangle_sum(image, lu_x, lu_y, height, width)
        middle_sum = Features.get_rectangle_sum(image, lu_x, lu_y + height, height, width)
        lower_sum = Features.get_rectangle_sum(image, lu_x, lu_y + 2 * height, height, width)
        return upper_sum - middle_sum + lower_sum

    @staticmethod
    def three_rectangles_vertical_split(image, lu_x, lu_y, height, width):
        assert lu_x + width <= 40 and lu_y + height <= 26, f"Wrong offset or size, {lu_x, lu_y, height, width}"
        width //= 3
        left_sum = Features.get_rectangle_sum(image, lu_x, lu_y, height, width)
        middle_sum = Features.get_rectangle_sum(image, lu_x + width, lu_y, height, width)
        right_sum = Features.get_rectangle_sum(image, lu_x + 2 * width, lu_y, height, width)
        return left_sum - middle_sum + right_sum

    @staticmethod
    def four_rectangles(image, lu_x, lu_y, height, width):
        assert lu_x + width <= 40 and lu_y + height <= 26, f"Wrong offset or size, {lu_x, lu_y, height, width}"
        upper_sum = Features.two_rectangles_horizontal_split(image, lu_x, lu_y, height // 2, width)
        lower_sum = Features.two_rectangles_horizontal_split(image, lu_x, lu_y + height // 2, height // 2, width)
        return upper_sum - lower_sum


if __name__ == "__main__":
    """Preprocessing images into integral images"""
    integral_cars = [[PreProcessing.get_integral_image(PreProcessing.read_file(os.path.join(folder, 'cars', fname))), -1]
                     for fname in
                     os.listdir(os.path.join(folder, 'cars'))]
    integral_faces = [[PreProcessing.get_integral_image(PreProcessing.read_file(os.path.join(folder, 'faces', fname))), 1]
                      for fname in
                      os.listdir(os.path.join(folder, 'faces'))]
    integral_images = integral_cars + integral_faces


    """============== ADABOOST ===================================================="""
    features = [[feature_name, getattr(Features, feature_name)] for feature_name in Features().features]
    len_cars = len(os.listdir(os.path.join(folder, 'cars')))
    len_faces = len(os.listdir(os.path.join(folder, 'faces')))
    assert len_cars + len_faces == len(integral_images)
    sample_length = len_faces + len_cars

    weights = [1 / sample_length] * sample_length
    weight_sum = 1.
    face_class, not_face_class = 1, -1

    feature_parameters = {feature[0]:[] for feature in features}

    """Time management"""
    start = time.perf_counter()
    iter = 0

    """Choosing feature"""

    for feature_name, feature in features:
        # print(f"\n\nFeature: {feature_name}\n")
        # fmodel.write(f"! {feature_name}\n")

        """Choosing mask size and offset"""
        for height in range(6, 24, 6):
            for width in range(6, 41, 6):
                for l_x in range(0, 41 - width, 3):
                    for l_y in range(0, 27 - height, 4):

                        iter += 1
                        err_t = 0
                        current_values = []
                        best_threshold = 0
                        correct = 0

                        for i, (img, cls) in enumerate(integral_images):
                            # weights[i] /= prev_weight_sum
                            current_values.append([feature(img, l_x, l_y, height, width), cls, weights[i]])

                        """Fast algo for searching min_error, working for N*logN"""
                        # print("iteration = ", iter)
                        sorted_values = sorted(current_values, key=lambda x: x[0])


                        """=================== Working variant ==============================="""
                        min_error = 1
                        max_error = 0
                        min_error_threshold = -1
                        max_error_threshold = -1

                        # current_error = sum(-1 * [obj[2] * obj[1]  for obj in sorted_values])
                        current_error = sum([obj[2] * obj[1] for obj in sorted_values])

                        for i, (threshold, img_class, weight) in enumerate(sorted_values):

                            current_error -= weight * img_class

                            if (i + 1 < sample_length) and threshold == sorted_values[i + 1][0]:
                                continue

                            if min_error > current_error:
                                min_error = current_error
                                min_error_threshold = threshold

                            if current_error > max_error:
                                max_error = current_error
                                max_error_threshold = threshold

                        min_error = (min_error + 1) / 2
                        max_error = (max_error + 1) / 2

                        sign = 1
                        best_threshold = min_error_threshold
                        err_t = min_error

                        if min_error > 1 - max_error:
                            sign = -1
                            best_threshold = max_error_threshold
                            err_t = 1 - max_error

                        # print(f"Error = {err_t}, iteration = {iter}")
                        """================================================================"""


                        """Still not working variant, just for history"""
                        # error = sum([obj[2] if obj[1] == not_face_class else 0 for obj in sorted_values])
                        # # error = sum([obj[2] if obj[1] == not_face_class else -obj[2] for obj in sorted_values])
                        #
                        # min_error = 1
                        # not_face_counter = 0
                        #
                        # sign = face_class if error > 0.5 else not_face_class
                        #
                        # for i, (threshold, img_class, weight) in enumerate(sorted_values):
                        #
                        #     if img_class == not_face_class:
                        #         error -= weight
                        #         not_face_counter += 1
                        #     elif img_class == face_class:
                        #         error += weight
                        #
                        #     if error < min_error:
                        #         min_error = error
                        #         best_threshold = threshold
                        #         sign = not_face_class if not_face_counter > (
                        #                     i - not_face_counter) else face_class
                        #
                        # err_t = min_error
                        # if min_error > 0.5:
                        #     err_t = 1 - min_error
                        #     sign *= -1
                        #
                        # if err_t < 0.15:
                        #     print(f"\nError for {feature_name} and {l_x, l_y, height, width}: %.20f" % err_t)
                        #     print(f"Prev weight = {weight_sum}")
                        """==========================================="""


                        alfa_t = math.log((1 - err_t) / err_t) / 2
                        z_t = 2 * math.sqrt(err_t * (1 - err_t))
                        for i in range(sample_length):
                            if (best_threshold - current_values[i][0]) >= 0:
                                res = sign
                            else:
                                res = -sign
                            weights[i] = weights[i] * math.exp(-alfa_t * integral_images[i][1] * res)  # / z_t
                            # weights[i] = weights[i] * math.exp(-alfa_t * integral_images[i][1] * res)
                            # weight_sum += weights[i]

                        weight_sum = sum(weights)

                        for i in range(len(weights)):
                            weights[i] /= weight_sum

                        if alfa_t > 0:
                            feature_parameters[feature_name].append(f"{alfa_t} {best_threshold} {sign} {l_x} {l_y} {height} {width} \n")

    with open(model, "w") as fmodel:
        for feature in feature_parameters:
            fmodel.write(f"! {feature}\n")
            # fmodel.write("\n".join(line for line in [" ".join([str(x) for x in params]) for params in feature_parameters[feature]]))
            fmodel.writelines(feature_parameters[feature])
            # fmodel.write("\n")

    print("\nTIME = ", time.perf_counter() - start)
