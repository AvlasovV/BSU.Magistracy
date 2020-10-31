def is_significant_bit_set(x):
    return (x >> 7) == 1


def get_7_least_bits(x):
    return x & 127


def set_significant_bit(x):
    return x | (1 << 7)


def reset_significant_bit(x):
    return x & (~(1 << 7))


import struct

class varint_coder:
    def write(out_stream, x_list):
        for x in x_list:
            num = x
            while True:
                block = get_7_least_bits(num)
                num = num >> 7
                if num > 0:
                print(f"Getting last 7 bits of {x} = {bin(block)}")


    def read(inp_stream):
        pass



import io
#
x_list = [1, 127, 128, 300]
output = io.BytesIO()
varint_coder.write(output, x_list)
print(output.getvalue())

# print(set_significant_bit(1))
# print(set_significant_bit(10))

