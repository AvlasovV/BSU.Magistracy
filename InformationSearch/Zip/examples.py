# # example coder 1
# class simple_text_coder:
#     def write(out_stream, x_list):
#         for x in x_list:
#             out_stream.write(str(x).encode('utf8'))
#             out_stream.write(b'\t')
#
#     def read(inp_stream):
#         return list(map(int, inp_stream.read().split()))
#
#
# import io
#
# output = io.BytesIO()
# simple_text_coder.write(output, [1, 2, 3, 300])
# print(output.getvalue())

# example coder 2
import struct

class simple_4byte_coder:
    def write(out_stream, x_list):
        for x in x_list:
            out_stream.write(struct.pack('I', x))

    def read(inp_stream):
        res = []
        while True:
            data = inp_stream.read(struct.calcsize('I'))
            if len(data) == 0:
                break
            res.append(struct.unpack('I', data)[0])
        return res

import io
output = io.BytesIO()
simple_4byte_coder.write(output, [1, 2, 3, 300])
print(output.getvalue())