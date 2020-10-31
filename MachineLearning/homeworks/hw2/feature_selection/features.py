import numpy as np


def sum_feature(a):
    """Sum of intensities of all pixels: digits with more used pixels will have higher value."""
    return np.sum(a)


def vertical_symmetry_feature(a):
    """Subtract right part of image from the left part and sum absolute differencies.
    More symmetrical digits will have lower value."""
    a = np.reshape(a, (28, 28))
    # print(a)
    b = np.abs(a[:14, :] - a[14:, :])
    return np.sum(b)


def horisontal_symmetry_feature(a):
    """Similar to feature above"""
    a = np.reshape(a, (28, 28))
    # print(a)
    b = np.abs(a[:, :14] - a[:, 14:])
    return np.sum(b)


def horisontal_weight_feature(a):
    """compare high and low parts of image"""
    a = np.reshape(a, (28, 28))
    b = np.sum(a[:, :15]) - np.sum(a[:, 15:])
    return b


def center_hole_feature(a):
    """Digits with hole in the center should give lower value"""
    a = np.reshape(a, (28, 28))
    # b = np.abs(a[13:19, 13:19])
    b = a[13:19, 13:19]
    return np.sum(b)


def center_vertical_feature(a):
    """looking at central segment fullness in comparison with another parts"""
    a = np.reshape(a, (28, 28))
    left = a[:, :12]
    center = a[:, 12:20]
    right = a[:, 20:]
    return np.sum(np.sum(center) - np.sum(right) - np.sum(left))


def side_diagonal_feature(a):
    """Compare upper left and lower right parts. More symmetrical digits will have lower value."""
    a = np.reshape(a, (28, 28))
    left_upper = np.triu(np.fliplr(a))
    right_lower = np.tril(np.fliplr(a))
    # b = np.abs(left_upper - right_lower)
    return np.abs(np.sum(left_upper) - np.sum(right_lower))
    # return np.sum(left_upper) - np.sum(right_lower)
    # return np.sum(b)


def main_diagonal_feature(a):
    """same as the above"""
    a = np.reshape(a, (28, 28))
    left_lower = np.tril(a)
    right_upper = np.triu(a)
    # print(left_lower)
    # print(right_upper)
    return np.sum(left_lower) - np.sum(right_upper)


def left_lower_center_feature(a):
    """checking the closing arc, for cases like 5 vs 6"""
    a = np.reshape(a, (28, 28))
    b = a[13:19, 9:13]
    return np.sum(b)


def right_high_center_feature(a):
    """checking right high center quarter, for cases like 6 vs 8"""
    a = np.reshape(a, (28, 28))
    b = a[7:12, 19:23]
    return np.sum(b)


def bottom_feature(a):
    """checking 'weight' of bottom picture part, for cases like 3 vs 7"""
    a = np.reshape(a, (28, 28))
    b = a[20:, :]
    return np.sum(b)


def left_middle_part_feature(a):
    """we divide the picture into 6 partsб 3*2 and getting left_middle_part
     for cases like 2 vs 6"""
    a = np.reshape(a, (28, 28))
    b = a[11:16, :14]
    return np.sum(b)


def composed_center_feature(a):
    """just trying this"""
    # a = np.reshape(a, (28, 28))
    result = right_high_center_feature(a) + left_lower_center_feature(a)
    return result


def another_center_feature(a):
    """for case 5 vs 8"""
    a = np.reshape(a, (28, 28))
    left = a[:, :11]
    center = a[:, 11:21]
    right = a[:, 21:]
    return np.sum(np.sum(center) - np.sum(right) - np.sum(left))


# start sample was: (0, 1) : (sum_feature, vertical_symmetry_feature),
FEATURES = {
    (0, 1): (center_hole_feature, left_middle_part_feature),
    (0, 2): (center_hole_feature, left_middle_part_feature),
    (0, 3): (composed_center_feature, center_hole_feature),
    (0, 4): (horisontal_symmetry_feature, center_hole_feature),
    (0, 5): (center_hole_feature, right_high_center_feature),
    (0, 6): (side_diagonal_feature, right_high_center_feature),
    (0, 7): (composed_center_feature, center_hole_feature),
    (0, 8): (sum_feature, center_hole_feature),
    (0, 9): (horisontal_symmetry_feature, center_hole_feature),
    (1, 2): (sum_feature, left_middle_part_feature),
    (1, 3): (main_diagonal_feature, bottom_feature),
    (1, 4): (bottom_feature, left_middle_part_feature),
    (1, 5): (center_hole_feature, left_middle_part_feature),
    (1, 6): (horisontal_weight_feature, left_middle_part_feature),
    (1, 7): (sum_feature, left_lower_center_feature),
    (1, 8): (bottom_feature, left_middle_part_feature),
    (1, 9): (horisontal_weight_feature, left_middle_part_feature),
    (2, 3): (left_lower_center_feature, left_middle_part_feature),
    (2, 4): (sum_feature, left_middle_part_feature),
    (2, 5): (left_lower_center_feature, left_middle_part_feature),
    (2, 6): (sum_feature, left_middle_part_feature),
    (2, 7): (left_lower_center_feature, left_middle_part_feature),
    (2, 8): (left_lower_center_feature, left_middle_part_feature),
    (2, 9): (sum_feature, left_middle_part_feature),
    (3, 4): (bottom_feature, left_middle_part_feature),
    (3, 5): (center_vertical_feature, main_diagonal_feature),
    (3, 6): (left_lower_center_feature, bottom_feature),
    (3, 7): (right_high_center_feature, bottom_feature),
    (3, 8): (main_diagonal_feature, left_lower_center_feature),
    (3, 9): (horisontal_symmetry_feature, bottom_feature),
    (4, 5): (center_hole_feature, bottom_feature),
    (4, 6): (horisontal_weight_feature, right_high_center_feature),
    (4, 7): (main_diagonal_feature, left_lower_center_feature),
    (4, 8): (bottom_feature, left_middle_part_feature),
    (4, 9): (bottom_feature, left_middle_part_feature),
    (5, 6): (sum_feature, bottom_feature),
    (5, 7): (side_diagonal_feature, left_lower_center_feature),
    (5, 8): (another_center_feature, side_diagonal_feature),
    (5, 9): (center_hole_feature, bottom_feature),
    (6, 7): (center_vertical_feature, left_lower_center_feature),
    (6, 8): (sum_feature, bottom_feature),
    (6, 9): (horisontal_weight_feature, right_high_center_feature),
    (7, 8): (another_center_feature , left_lower_center_feature),
    (7, 9): (left_lower_center_feature, right_high_center_feature),
    (8, 9): (bottom_feature, left_middle_part_feature),
}

