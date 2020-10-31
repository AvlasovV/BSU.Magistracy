def z_function(s):
    z = [0] * len(s)
    l, r = 0, 0
    length = len(s)
    for i in range(1, length):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < length and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


if __name__ == "__main__":

    with open("input.txt") as input:
        s = input.readline().rstrip()
        k = 1
        for i in range(1, len(s)):
            k += i + 1 - max(z_function(s[i::-1]))

    with open("output.txt", "w") as out:
        out.write(str(k))
