import random, string
X = 10000
strng = ''.join(random.choice(string.ascii_lowercase) for _ in range(X))
with open("input.txt", "w") as f:
    f.write(strng)