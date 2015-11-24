#!/usr/bin/env python3

from tp1 import Graph


def Guido_s_graph():
    G = Graph()
    for i in range (ord("A"), ord("G")):
        G.add_a_node(chr(i))
    
    G.add_an_edge('A','B')
    G.add_an_edge('A','C')
    G.add_an_edge('B','D')
    G.add_an_edge('B','C')
    G.add_an_edge('C','D')
    G.add_an_edge('D','C')
    G.add_an_edge('E','F')
    G.add_an_edge('F','C')
    
    
    return G.__str__()
 

if __name__=='__main__':
    print(guido_s_graph)
