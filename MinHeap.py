from MinHeapNode import MinHeapNode

class MinHeap:
    def __init__(self):
        self.A = []
        self.A.insert(0,MinHeapNode(None))
        self.size = 0

    def getParent(self, keyIndex):
        return int(keyIndex/2)

    def getLeftChild(self, keyIndex):
        return 2*keyIndex

    def getRightChild(self, keyIndex):
        return 2*keyIndex+1

    def getMinimum(self):
        return self.A[1]

    def decreaseKey(self, i, newKeyValue):
        if newKeyValue > self.A[i].key:
            print("error: new key bigger than the current one")
        else:
            self.A[i].key = newKeyValue
            while i > 1 and self.A[self.getParent(i)].key > self.A[i].key:
                tmp = self.A[self.getParent(i)]
                self.A[self.getParent(i)] = self.A[i]
                self.A[i] = tmp

                i = self.getParent(i)

    def insert(self, node):
        self.size +=1
        self.A.append(node)
        self.decreaseKey(self.size, node.key)

    def minHeapify(self, i):
        l = self.getLeftChild(i)
        r = self.getRightChild(i)

        if l <= self.size and self.A[l].key < self.A[i].key:
            minimum = l
        else:
            minimum = i
        if r <= self.size and self.A[r].key < self.A[minimum].key:
            minimum = r
        if minimum is not i:
            tmp = self.A[i]
            self.A[i] = self.A[minimum]
            self.A[minimum] = tmp

            self.minHeapify(minimum)

    def extractMin(self):
        if self.size < 1:
            print("error: heap underflow")

        minimum = self.A[1]
        self.A[1] = self.A[self.size]
        self.A.pop(self.size)
        self.size -=1

        self.minHeapify(1)

        return minimum

    def stillContains(self, nodeValue):
        found = False
        v = None
        for node in self.A:
            if node.value == nodeValue:
                found = True
                v = node
                break
        return found, v

    def getIndex(self, nodeValue):
        index = 0
        for node in self.A:
            if node.value == nodeValue:
                index = self.A.index(node)
        return index
