import unittest

from Graph import Graph
from Edge import Edge

class MyTestCase(unittest.TestCase):
    def testKruskal(self):
        matrix = [[0,10,12,0,0,0,0,0,0],[10,0,9,8,0,0,0,0,0],[12,9,0,0,3,1,0,0,0],[0,8,0,0,7,0,8,5,0],[0,0,3,7,0,3,0,0,0],[0,0,1,0,3,0,0,6,0],[0,0,0,8,0,0,0,9,2],[0,0,0,5,0,6,9,0,11],[0,0,0,0,0,0,2,11,0]]
        graph1 = Graph(9)
        graph1.setMatrix(matrix)
        A = graph1.computeMSTWithKruskal()

        expectedA = [2,5,1, 6,8,2, 2,4,3, 3,7,5, 5,7,6, 1,3,8, 3,6,8, 0,1,10]
        i = 0
        for node in A:
            self.assertEqual(node.u,expectedA[i])
            i +=1
            self.assertEqual(node.v,expectedA[i])
            i+=1
            self.assertEqual(node.weight,expectedA[i])
            i+=1   #questo test funziona

        #etc con altri test
if __name__ == '__main__':
    unittest.main()
