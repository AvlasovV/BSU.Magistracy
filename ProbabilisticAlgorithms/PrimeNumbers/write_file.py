length = 10 ** 6
start = 10 ** 14

with open("primality.in", "w") as f:
    print("Writing new input data")
    f.write(str(length) + "\n")
    for i in range(start, start + length):
        f.write(str(i) + "\n")
