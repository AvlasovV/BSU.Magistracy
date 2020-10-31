# from features import *
# best_features = {(0, 1): {
#     'features': (center_hole_feature, left_middle_part_feature),
#     'accuracy': 0.9805142083897158
#     }, (0, 2): {
#     'features': (center_hole_feature, left_middle_part_feature),
#     'accuracy': 0.9473835744619593
#     }, (0, 3): {'features': (composed_center_feature, center_hole_feature),
#                 'accuracy': 0.9235972657362574
#                 }, (0, 4): {'features': (
#    horisontal_symmetry_feature , center_hole_feature ),
#                             'accuracy': 0.9859401180155897
#                             }, (0, 5): {
#     'features': (center_hole_feature , right_high_center_feature ),
#     'accuracy': 0.8616071428571429
#     }, (0, 6): {'features': (
#     side_diagonal_feature , right_high_center_feature ),
#                 'accuracy': 0.9483997387328543
#                 }, (0, 7): {'features': (composed_center_feature, center_hole_feature),
#                             'accuracy': 0.9454775993237532
#                             }, (0, 8): {
#     'features': (sum_feature , center_hole_feature ),
#     'accuracy': 0.9291229603729604
#     }, (0, 9): {'features': (
#     horisontal_symmetry_feature , center_hole_feature ),
#                 'accuracy': 0.9675348098982758
#                 }, (1, 2): {
#     'features': (sum_feature , left_middle_part_feature ),
#     'accuracy': 0.9046209726239322
#     }, (1, 3): {
#     'features': (main_diagonal_feature ,bottom_feature ),
#     'accuracy': 0.9357437741377014
#     }, (1, 4): {
#     'features': (bottom_feature, left_middle_part_feature ),
#     'accuracy': 0.9846949187130127
#     }, (1, 5): {
#     'features': (center_hole_feature , left_middle_part_feature ),
#     'accuracy': 0.9266384778012685
#     }, (1, 6): {'features': (
#     horisontal_weight_feature ,left_middle_part_feature ),
#                 'accuracy': 0.9458415237578798
#                 }, (1, 7): {
#     'features': (sum_feature ,left_lower_center_feature ),
#     'accuracy': 0.8571522742254449
#     }, (1, 8): {
#     'features': (bottom_feature, left_middle_part_feature),
#     'accuracy': 0.9182424159978234
#     }, (1, 9): {'features': (
#     horisontal_weight_feature ,left_middle_part_feature ),
#                 'accuracy': 0.9574654533198517
#                 }, (2, 3): {'features': (
#     left_lower_center_feature ,left_middle_part_feature ),
#                             'accuracy': 0.8818201118109121
#                             }, (2, 4): {
#     'features': (sum_feature, left_middle_part_feature ),
#     'accuracy': 0.9320254813956855
#     }, (2, 5): {'features': (
#     left_lower_center_feature ,left_middle_part_feature ),
#                 'accuracy': 0.8989701571074193
#                 }, (2, 6): {
#     'features': (sum_feature, left_middle_part_feature ),
#     'accuracy': 0.9035049762007789
#     }, (2, 7): {'features': (
#     left_lower_center_feature , left_middle_part_feature ),
#                 'accuracy': 0.8746061751732829
#                 }, (2, 8): {'features': (
#     left_lower_center_feature , left_middle_part_feature ),
#                             'accuracy': 0.8295331161780674
#                             }, (2, 9): {
#     'features': (sum_feature , left_middle_part_feature ),
#     'accuracy': 0.8989819328936048
#     }, (3, 4): {
#     'features': (bottom_feature , left_middle_part_feature ),
#     'accuracy': 0.9767991407089152
#     }, (3, 5): {
#     'features': (center_vertical_feature ,main_diagonal_feature ),
#     'accuracy': 0.8107625984837223
#     }, (3, 6): {
#     'features': (left_lower_center_feature , bottom_feature ),
#     'accuracy': 0.9144610116287365
#     }, (3, 7): {
#     'features': (right_high_center_feature , bottom_feature ),
#     'accuracy': 0.8493141194402106
#     }, (3, 8): {'features': (
#     main_diagonal_feature , left_lower_center_feature ),
#                 'accuracy': 0.8088930259200916
#                 }, (3, 9): {
#     'features': (horisontal_symmetry_feature ,bottom_feature ),
#     'accuracy': 0.9248173629335413
#     }, (4, 5): {'features': (center_hole_feature , bottom_feature ),
#                 'accuracy': 0.9435944279515871
#                 }, (4, 6): {'features': (
#     horisontal_weight_feature ,right_high_center_feature ),
#                             'accuracy': 0.852043795620438
#                             }, (4, 7): {'features': (
#     main_diagonal_feature , left_lower_center_feature ),
#                                         'accuracy': 0.9421265141318977
#                                         }, (4, 8): {
#     'features': (bottom_feature ,left_middle_part_feature ),
#     'accuracy': 0.9660781009597773
#     }, (4, 9): {
#     'features': (bottom_feature , left_middle_part_feature ),
#     'accuracy': 0.8093890581918445
#     }, (5, 6): {'features': (sum_feature , bottom_feature ),
#                 'accuracy': 0.8463113200394268
#                 }, (5, 7): {'features': (
#     side_diagonal_feature , left_lower_center_feature ),
#                             'accuracy': 0.8471262678230193
#                             }, (5, 8): {
#     'features': (center_vertical_feature , side_diagonal_feature ),
#     'accuracy': 0.7989800578474654
#     }, (5, 9): {'features': (center_hole_feature , bottom_feature ),
#                 'accuracy': 0.8897596262527315
#                 }, (6, 7): {'features': (
#     center_vertical_feature , left_lower_center_feature ),
#                             'accuracy': 0.9344343284635471
#                             }, (6, 8): {
#     'features': (sum_feature , bottom_feature ),
#     'accuracy': 0.8611780162031969
#     }, (6, 9): {'features': (
#     horisontal_weight_feature , right_high_center_feature ),
#                 'accuracy': 0.8221772444701461
#                 }, (7, 8): {
#     'features': (left_lower_center_feature , bottom_feature ),
#     'accuracy': 0.8959484346224678
#     }, (7, 9): {'features': (
#     left_lower_center_feature ,right_high_center_feature ),
#                 'accuracy': 0.88106097817697
#                 }, (8, 9): {
#     'features': (bottom_feature , left_middle_part_feature ),
#     'accuracy': 0.9044475077994631
#     }, }
# import pickle
#
# with open(r"D:\1UNIVERSITY\BSU.Magistracy\MachineLearning\homeworks\2\feature_selection\best_features.pickle", "wb") as f:
#     pickle.dump(best_features, f)

a = """(0, 1): (center_hole_feature,left_middle_part_feature),
0.9805142083897158
(0, 2): (center_hole_feature,left_middle_part_feature),
0.9473835744619593
(0, 3): (composed_center_feature,center_hole_feature),
0.9235972657362574
(0, 4): (horisontal_symmetry_feature,center_hole_feature),
0.9859401180155897
(0, 5): (center_hole_feature,right_high_center_feature),
0.8616071428571429
(0, 6): (side_diagonal_feature,right_high_center_feature),
0.9483997387328543
(0, 7): (composed_center_feature,center_hole_feature),
0.9454775993237532
(0, 8): (sum_feature,center_hole_feature),
0.9291229603729604
(0, 9): (horisontal_symmetry_feature,center_hole_feature),
0.9675348098982758
(1, 2): (sum_feature,left_middle_part_feature),
0.9046209726239322
(1, 3): (main_diagonal_feature,bottom_feature),
0.9357437741377014
(1, 4): (bottom_feature,left_middle_part_feature),
0.9846949187130127
(1, 5): (center_hole_feature,left_middle_part_feature),
0.9266384778012685
(1, 6): (horisontal_weight_feature,left_middle_part_feature),
0.9458415237578798
(1, 7): (sum_feature,left_lower_center_feature),
0.8571522742254449
(1, 8): (bottom_feature,left_middle_part_feature),
0.9182424159978234
(1, 9): (horisontal_weight_feature,left_middle_part_feature),
0.9574654533198517
(2, 3): (left_lower_center_feature,left_middle_part_feature),
0.8818201118109121
(2, 4): (sum_feature,left_middle_part_feature),
0.9320254813956855
(2, 5): (left_lower_center_feature,left_middle_part_feature),
0.8989701571074193
(2, 6): (sum_feature,left_middle_part_feature),
0.9035049762007789
(2, 7): (left_lower_center_feature,left_middle_part_feature),
0.8746061751732829
(2, 8): (left_lower_center_feature,left_middle_part_feature),
0.8295331161780674
(2, 9): (sum_feature,left_middle_part_feature),
0.8989819328936048
(3, 4): (bottom_feature,left_middle_part_feature),
0.9767991407089152
(3, 5): (center_vertical_feature,main_diagonal_feature),
0.8107625984837223
(3, 6): (left_lower_center_feature,bottom_feature),
0.9144610116287365
(3, 7): (right_high_center_feature,bottom_feature),
0.8493141194402106
(3, 8): (main_diagonal_feature,left_lower_center_feature),
0.8088930259200916
(3, 9): (horisontal_symmetry_feature,bottom_feature),
0.9248173629335413
(4, 5): (center_hole_feature,bottom_feature),
0.9435944279515871
(4, 6): (horisontal_weight_feature,right_high_center_feature),
0.852043795620438
(4, 7): (main_diagonal_feature,left_lower_center_feature),
0.9421265141318977
(4, 8): (bottom_feature,left_middle_part_feature),
0.9660781009597773
(4, 9): (bottom_feature,left_middle_part_feature),
0.8093890581918445
(5, 6): (sum_feature,bottom_feature),
0.8463113200394268
(5, 7): (side_diagonal_feature,left_lower_center_feature),
0.8471262678230193
(5, 8): (another_center_feature,side_diagonal_feature),
0.8056020703303395
(5, 9): (center_hole_feature,bottom_feature),
0.8897596262527315
(6, 7): (center_vertical_feature,left_lower_center_feature),
0.9344343284635471
(6, 8): (sum_feature,bottom_feature),
0.8611780162031969
(6, 9): (horisontal_weight_feature,right_high_center_feature),
0.8221772444701461
(7, 8): (left_lower_center_feature,bottom_feature),
0.8959484346224678
(7, 9): (left_lower_center_feature,right_high_center_feature),
0.88106097817697
(8, 9): (bottom_feature,left_middle_part_feature),
0.9044475077994631"""

import io
buf = io.StringIO(a)
for i, j in enumerate(buf, 0):
    if i % 2 == 0:
        print(j, end="")
