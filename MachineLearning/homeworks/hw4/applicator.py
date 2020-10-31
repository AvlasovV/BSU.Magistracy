#!/usr/bin/env python3
import numpy as np
import sys
import os
import cv2
from collections import defaultdict
import time

model = sys.argv[-2]
# model = sys.argv[-1]
fname = sys.argv[-1]


class PreProcessing:
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

    @staticmethod
    def get_strong_classifier(model):
        classifier = defaultdict(list)
        try:
            with open(model, "r") as f:
                for line in f:
                    objects = line.split()
                    if objects[0] == "!":
                        feature = objects[1]
                    else:
                        alfa_t, threshold = float(objects[0]), float(objects[1])
                        sign, l_x, l_y, height, width = [int(objects[x]) for x in range(2, 7)]
                        classifier[feature].append([alfa_t, threshold, sign, l_x, l_y, height, width])
            return classifier
        except ValueError as e:

            print("Error:", objects)
            raise e

    @staticmethod
    def use_classifier(integral_image, classifier):
        features = {feature_name: getattr(Features, feature_name) for feature_name in Features().features}
        result = 0
        for feat in classifier:
            for parameters in classifier[feat]:
                alfa, threshold, sign, *funct_params = parameters
                val = features[feat](integral_image, *funct_params)

                if (threshold - val) >= 0:
                    cls = sign
                else:
                    cls = -sign

                result += cls * alfa

        if result > 0:
            print(1)
            return 1
        else:
            print(0)
            return -1


class Features:

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


# img = PreProcessing.read_file(fname)
# integral_img = PreProcessing.get_integral_image(img)
#
classifier = PreProcessing.get_strong_classifier(model)
# PreProcessing.use_classifier(integral_img, classifier)

if __name__ == "__main__":

    classifier = PreProcessing.get_strong_classifier(model)

    img = PreProcessing.read_file(fname)
    integral_img = PreProcessing.get_integral_image(img)
    PreProcessing.use_classifier(integral_img, classifier)



    """Code for testing whole sample"""

    # start = time.perf_counter()
    # folder = "train"
    # integral_cars = [
    #     [PreProcessing.get_integral_image(PreProcessing.read_file(os.path.join(folder, 'cars', fname))), -1]
    #     for fname in
    #     os.listdir(os.path.join(folder, 'cars'))]
    # integral_faces = [
    #     [PreProcessing.get_integral_image(PreProcessing.read_file(os.path.join(folder, 'faces', fname))), 1]
    #     for fname in
    #     os.listdir(os.path.join(folder, 'faces'))]
    # integral_images = integral_cars + integral_faces
    #
    # tests_count = len(integral_images)
    # right_count = 0
    # for i in integral_images:
    #     cls = PreProcessing.use_classifier(i[0], classifier)
    #     if cls == i[1]:
    #         right_count += 1
    #
    # print(f"\nAlgo accuracy = {right_count / tests_count}")
    # print("\nTIME = ", time.perf_counter() - start)

    """================================"""
