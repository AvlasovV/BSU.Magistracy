with open("results\\8_errors.txt", "r") as f, open("results\\out", "w") as ou:

    cur_d = 1.
    dots = ""
    dots_plus = ""
    dots_min = ""
    for i, line in enumerate(f):
        l = line.split()
        d, k, err, std = [float(x) for x in l]
        if cur_d != d:
            ou.write(str(cur_d))
            ou.write("\n")
            ou.write(dots)
            ou.write("\n")
            ou.write(dots_plus)
            ou.write("\n")
            ou.write(dots_min)
            ou.write("\n")

            cur_d = d

            dots = ""
            dots_plus = ""
            dots_min = ""

        dots += f"({k};{err})"
        dots_plus += f"({k};{err + std})"
        dots_min += f"({k};{err - std})"


    ou.write(str(cur_d))
    ou.write("\n")
    ou.write(dots)
    ou.write("\n")
    ou.write(dots_plus)
    ou.write("\n")
    ou.write(dots_min)
