from features import *
import logging
import main
import sklearn.datasets
import sklearn.linear_model
import pickle


old_features = [('sum_feature', sum_feature),
                ('vertical_symmetry_feature', vertical_symmetry_feature),
                ('horisontal_symmetry_feature', horisontal_symmetry_feature),
                ('horisontal_weight_feature', horisontal_weight_feature),
                ('center_hole_feature', center_hole_feature),
                ('center_vertical_feature', center_vertical_feature),
                ('side_diagonal_feature', side_diagonal_feature),
                ('main_diagonal_feature', main_diagonal_feature),
                ("left_lower_center_feature", left_lower_center_feature),
                ("right_high_center_feature", right_high_center_feature),
                ("bottom_feature", bottom_feature),
                ("left_middle_part_feature", left_middle_part_feature),
                ("composed_center_feature", composed_center_feature),
                ]

new_features = [ ("another_center_feature", another_center_feature)]

best_features_pickle = "best_features.pickle"
best_features_txt = "best_features.txt"
# range_of_digits = (5)

def read_latest_best_features_pickle(file_name=best_features_pickle):
    with open(best_features_pickle, "rb") as f:
        return pickle.load(f)


def write_best_features_txt_pickle(results, cases, txt_f=best_features_txt, pickle_f=best_features_pickle):
    with open(txt_f, "w") as f:
        for i in results:
            # print(results[i]['features'][0].__name__)
            f.write(f"{i}: ({results[i]['features'][0].__name__},{results[i]['features'][1].__name__}),\n")
            f.write(f"{results[i]['accuracy']}\n")
        f.write(f"\nUnsolved cases:\n")
        for i in results:
            if results[i]["accuracy"] < 0.8:
                f.write(f"{i}")
            else:
                cases += 1
        f.write(f"\nSolved cases: {cases}")
    with open(pickle_f, "wb") as f:
        pickle.dump(results, f)


def searching_best_features(args):
    sklearn_home = args.datadir

    logging.info('Downloading MNIST data')
    mnist = sklearn.datasets.fetch_openml('mnist_784', data_home=sklearn_home)
    logging.info('Data is ready')

    cases = 0
    results = read_latest_best_features_pickle()
    for da in range(10):    #  for da in [5]:
        for db in range(da + 1, 10):   #  for db in [8]:
            X, Y = main._filter_data(mnist['data'], mnist['target'], [da, db])

            logging.info('\nCASE {} VS {}: '.format(da, db))
            for feat1 in range(len(new_features)):
                for feat2 in range(len(old_features)):

                    # fs = features.FEATURES[(da, db)]
                    fs = (new_features[feat1][1], old_features[feat2][1])
                    X2 = [(fs[0](x), fs[1](x)) for x in X]

                    cls = sklearn.linear_model.LogisticRegression(solver='liblinear')
                    cls.fit(X2, Y)

                    result = cls.score(X2, Y)
                    logging.info('{} and {}: {:.1f}%'.format(new_features[feat1][0], old_features[feat2][0], result * 100))
                    if result > results[(da, db)]["accuracy"]:
                        results[(da, db)]["accuracy"] = result
                        results[(da, db)]["features"] = (new_features[feat1][1], old_features[feat2][1])

    write_best_features_txt_pickle(results, cases)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    searching_best_features(main._parse_args())
    # a = read_latest_best_features_pickle()
    # print(a[(5,8)]["features"][0].__name__)

    # print(old_features)