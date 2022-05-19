import numpy as np

from UnionFindNode import UnionFindNode
from UnionFindSet import Set
from UnionFind import UnionFind
from Graph import Graph
from Edge import Edge
from MinHeapNode import MinHeapNode

def main():
   # graph = Graph.generateRandomGraph(10, 0/100)
   # graph.printMatrix()
   # print(graph.isConnected())
   # #g = Graph(10)
   # #g.setMatrix()
   # #print(g.isConnected())
   # #g.printMatrix()
   #
   # A = []
   # A.append(Edge(1,2,14))
   # A.append(Edge(3,2,1))
   # A.append(Edge(0,0,3))
   # for x in A:
   #     print(x.weight)
   # B = A
   # B.sort(key=lambda x: x.weight)
   # for x in B:
   #     print(x.weight)
   # for x in A:
   #     print(x.weight)
   #
   # mhn = MinHeapNode(3)
   # mhn2 = MinHeapNode(3,20)
   # print(mhn.key)
   # print(mhn2.key)
   # g = Graph(5)
   # g.setMatrix3()
   # print(g.isConnected())
   # A = g.computeMSTWithKruskal()
   # for edge in A:
   #     print("(",edge.u, ",", edge.v, ")")


   # graph = Graph.generateRandomGraph(5,100/100)
   # graph.printMatrix()
   # matrix = 1
   # while graph.isConnected() is False:
   #     graph = Graph.generateRandomGraph(5,20/100)
   #     graph.printMatrix()
   #     matrix+=1
   # print(matrix)
   #
   # if graph.isConnected():
   #     A = graph.computeMSTWithKruskal()
   #     for edge in A:
   #        print("(",edge.u, ",", edge.v, ")")
   # else:
   #     print("graph is not connected.")

   # g1 = Graph(5)
   # matrix = [[0,10,12,0,0,0,0,0,0],[10,0,9,8,0,0,0,0,0],[12,9,0,0,3,1,0,0,0],[0,8,0,0,7,0,8,5,0],[0,0,3,7,0,3,0,0,0],[0,0,1,0,3,0,0,6,0],[0,0,0,8,0,0,0,9,2],[0,0,0,5,0,6,9,0,11],[0,0,0,0,0,0,2,11,0]]
   # matrix1 = [[0,24,13,13,22],[24,0,22,13,13],[13,22,0,19,14],[13,13,19,0,19],[22,13,14,19,0]]
   # matrix3 = [[0,9,75,0,0],[9,0,95,19,42],[75,95,0,51,0],[0,19,51,0,31],[0,42,0,31,0]]
   # g1.setMatrix(matrix3)
   # A = g1.computeMSTWithPrim(3)
   # for edge in A:
   #     print("(",edge.u.value, ",", edge.v.value, ", ", edge.weight, ")")

   V = np.arange(0,10,1)
   print(V)
   index = np.where(V == 3)[0][0]
   print(index)

if __name__ == '__main__':
    main()

