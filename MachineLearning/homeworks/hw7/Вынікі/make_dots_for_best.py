with open("results\\errors_for_best_c.txt", "r") as f:

    cur_d = 1.
    dots_valid = ""
    dots_test = ""
    for i, line in enumerate(f):
        l = line.split()
        d, valid, test = [float(x) for x in l]
        # if cur_d != d:
            # print(str(cur_d))
            # print("\n")
            # print(dots_valid)
            # print("\n")
            # print(dots_test)
            # print("\n")
            #
            #
            # cur_d = d
            # dots_valid = ""
            # dots_test = ""

        dots_valid += f"({d};{valid})"
        dots_test += f"({d};{test})"
    #
    # print(str(cur_d))
    # print("\n")
    print(dots_valid)
    print("\n")
    print(dots_test)
    print("\n")