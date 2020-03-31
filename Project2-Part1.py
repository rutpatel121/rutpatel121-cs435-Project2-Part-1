import random
import time

class Graph():

    def __init__(self):
        #""" initializes a graph object and create a dictionary"""
        self.graph_dict = {}

        #"""This adds a new node to the graph"""
    def addNode(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

        #"""This function adds an undirected edge"""
    def addUndirectedEdge(self,vert1,vert2):
        if vert2 not in self.graph_dict[vert1]:
            self.graph_dict[vert1].append(vert2)
        if vert1 not in self.graph_dict[vert2]:
            self.graph_dict[vert2].append(vert1)


        #"""This function removes an undirected edge"""
    def removeUndirectedEdge(self,vert1,vert2):
        if vert2 in self.graph_dict[vert1]:
            self.graph_dict[vert1].remove(vert2)
        if vert1 in self.graph_dict[vert1]:
            self.graph_dict[vert2].remove(vert1)

        #"""This returns a set of all Nodes in the graph"""
    def getAllNodes(self):
        return list(self.graph_dict.keys())


class GraphSearch():

    def dfsrec(self,graph, start, goal, path=None):
        if path is None:
            path = [start]
        if start == goal:
            yield path
        for next in graph[start] - set(path):
            yield from DFSRec(graph, next, goal, path + [next])


    #"""Iteratively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order."""
    def dfsiter(self,graph, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))



    # """Recursively returns an List of the Nodes in the Graph in a valid Breadth-First Traversal order."""
    def bbftrec(self,node):
        output_list.append(node)
    def bftrec(self,graph,start,end):
        i=1
        while i<=int(end):
            self.bbftrec(str(i))
            i=i+1

    #""" Iteratively returns an List of all of the Nodes in the Graph in a valid Breadth-First Traversal."""
    def bftiter(self,graph, start):
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)
        return visited


if __name__ == "__main__":
    output_list=[]
    graph = Graph()
    linked_list = Graph()
    search=GraphSearch()
    #"""Creates n random nodes with randomly assigned unweighted, bidirectional edges."""
    def createRandomUnweightedGraphIter(n):

        i=1
        while i<=n:
            k=random.randrange(1, 5, 1)
            graph.addNode(str(i))
            if i>=5:
                l=0
                while l<k:
                    rand_node=random.randrange(1, i, 1)
                    graph.addUndirectedEdge(str(rand_node),str(i))
                    l=l+1
            i=i+1
    #"""Creates a Graph with n nodes where each node only has an edge to the next node created."""
    def createLinkedList(n):
        if n>0:
            linked_list.addNode("1")
            i=2
            while i<=n:
                linked_list.addNode(str(i))
                linked_list.addUndirectedEdge(str(i-1),str(i))
                i=i+1
    createLinkedList(1000)
    #"""Run a BFT recursively on a LinkedList"""
    def BFTRecLinkedList(link_list):
        search.bftrec(link_list.keys(),"1","10000")
    #run a BFT iteratively on a LinkedList
    BFTRecLinkedList(linked_list.graph_dict)
    print(output_list)
    def BFTIterLinkedList(link_list):
        return search.bftiter(linked_list,"1")
