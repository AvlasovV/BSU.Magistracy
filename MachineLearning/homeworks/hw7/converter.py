import sys

input_name = sys.argv[-2]
output_name = sys.argv[-1]

with open(input_name, "r") as inp, open(output_name, "w") as out:
    for i in inp:
        params = i.split(",")

        if int(params[-1]) > 0:
            out.write("-1 ")
        else:
            out.write("+1 ")

        out.write("0:0 ")
        for ind in range(len(params) - 1):
            if float(params[ind]) != 0:
                out.write(f"{ind+1}:{params[ind]} ")
        out.write("\n")
