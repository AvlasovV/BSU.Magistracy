with open("small_model", "r") as f:
    for line in f:
        objects = line.split()
        if objects[0] == "!":
            feature = objects[1]
        else:
            alfa_t = float(objects[0])
            l_x, l_y, height, width = [int(objects[x]) for x in range(1, 5)]
            print(alfa_t, l_x, l_y, height, width)