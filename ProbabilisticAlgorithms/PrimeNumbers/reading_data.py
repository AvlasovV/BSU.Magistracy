
file = "primes1.txt"
output_file = "primality.in"

b = []
with open(file) as f:
    a = f.read()
    b = list(map(int, a.split()))


start = 10000
length = 100

start, length = 900000, int(len(b) / 100)

with open(output_file, "w") as output:
    print("Writing prime numbers into input")
    output.write(str(length) + "\n")
    for i in range(start, start + length):
        output.write(str(b[i]) + "\n")
