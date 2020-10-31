"""If you want to some examples.
You need to download datasets from http://yann.lecun.com/exdb/mnist/ and put them into samples  folder"""

from mnist import MNIST

import sys, os
from contextlib import ExitStack

mndata = MNIST('samples')

images, labels = mndata.load_training()
# or
# images, labels = mndata.load_testing()
COUNT_OF_SAMPLES = 20
with ExitStack() as stack:
    files = [stack.enter_context(open(fname, "w")) for fname in "0123456789"]
    indexes = {i: 0 for i in range(10)}
    for i in range(len(images)):    # index = random.randrange(0, len(images))  # choose an index ;-)
        digit = labels[i]
        if indexes[digit] < COUNT_OF_SAMPLES:
            files[digit].write(mndata.display(images[i]))
            files[digit].write("\n")
            indexes[digit] += 1
