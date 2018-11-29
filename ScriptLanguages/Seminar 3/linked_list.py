class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next
        assert type(next) == Node or "NoneType", "Wrong type of next node"

    def __str__(self):
        return "Value {}, Next: {}".format(self._value, self._next)

    def __iter__(self):
        self = self._next
        return self

    def __next__(self):
        if self._next:
            return self._next
        else:
            raise StopIteration


if __name__ == "__main__":
    n1 = Node(7, Node(5, Node(4)))
    print(n1)
    # for i in n1:
    #     print(i)