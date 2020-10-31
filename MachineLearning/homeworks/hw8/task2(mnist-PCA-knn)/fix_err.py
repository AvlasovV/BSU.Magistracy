with open("accuracy_alternate.txt", "r") as f:
    for line in f:
        if line != "\n" or line != "":
            nums = line.replace(',',' ').split()

            print("(", end="")
            for i in nums:
                try:
                    n = int(i)
                    print(f"{n};", end="")
                except ValueError:
                    try:
                        n = float(i)
                        print(f"{n}", end="")
                    except ValueError:
                        pass
            print(")\n")
