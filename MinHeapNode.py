from UnionFindNode import UnionFindNode

class MinHeapNode(UnionFindNode):
    def __init__(self, value, key=10000):
        super().__init__(value)
        self.key = key
        self.pigreco = None

