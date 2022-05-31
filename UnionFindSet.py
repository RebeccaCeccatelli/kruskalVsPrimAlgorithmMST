
class Set:
    def __init__(self, firstElement):       #each element of the set is a UnionFindNode
        self.list = [firstElement]
        self.representative = firstElement
        self.size = 1

    def addElement(self, element):
        self.list.append(element)
        element.setRepresentative(self.representative)
        self.size +=1
