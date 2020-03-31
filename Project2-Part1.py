import random

class Graph:
    def __init__(self):
        self.adjList = {}

    def addNode(self, nodeVal):
        self.adjList[nodeVal] = []
    
    def addUndirectedEdge(self, first, second):
        self.adjList[first].append(second)
        if first != second:
            self.adjList[second].append(first)