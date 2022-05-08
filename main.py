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


   graph = Graph.generateRandomGraph(5,100/100)
   graph.printMatrix()
   matrix = 1
   while graph.isConnected() is False:
       graph = Graph.generateRandomGraph(5,20/100)
       graph.printMatrix()
       matrix+=1
   print(matrix)

   if graph.isConnected():
       A = graph.computeMSTWithKruskal()
       for edge in A:
          print("(",edge.u, ",", edge.v, ")")
   else:
       print("graph is not connected.")

   g1 = Graph(9)
   g1.setMatrix([])
   A = g1.computeMSTWithKruskal()
   for edge in A:
       print("(",edge.u, ",", edge.v, ")")

if __name__ == '__main__':
    main()

