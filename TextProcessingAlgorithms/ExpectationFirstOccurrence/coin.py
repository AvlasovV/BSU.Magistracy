def prefix_function(s):
    pi = [0]
    for i in range(1, len(s)):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi.append(j)
    return pi


if __name__ == "__main__":
    with open('coin.in') as input:
        s = input.readline().rstrip()

    n = len(s)
    pi = prefix_function(s)

    # sum = pow(2, len(s))

    degrees_of_two = [1]
    for i in range(1, n + 1):
        degrees_of_two.append(degrees_of_two[i - 1] * 2)

    i = n
    sum = 0
    while i > 0:
        # sum += pow(2, i)
        sum += degrees_of_two[i]
        i = pi[i-1]

    with open('coin.out', 'w') as output:
        output.write(str(sum))
