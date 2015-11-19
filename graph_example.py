#!/usr/bin/env python3

"""
    Institut Villebon
    UE 5i4 : TP_1  Graph Theory
    Authors : E.Albrand & C.Herat
    Objectif of the program :
        - To know various form of representation of graphs
        - To implement a structure of graphs in Python
        - I.e make a graph path
        - Read implement the algorithm associated components
"""


class Graph():
    """ docstring """
    
    def __init__(self):
        """docstring"""
        
        self.nodes = set()
        self.edges = []
        self.adjency_list = {}
                
        
    def add_a_node(self, node_name):
        """
            This method is for add a node to the Graph
            
            Args :
                node_name (string): the name of the node. 
                    For example $ node_name = 'Orsay' $ if the name of the node is Orsay
            
            Returns :
                None
            
            Example of calling:
                $ add_a_node('Orsay')
        """
        
        if ((node_name in self.nodes) == False):
            self.nodes.add(node_name)
            self.adjency_list[node_name]= []
            
    def add_an_edge(self, from_node, to_node):
        """docstring"""
        
        if((((from_node and to_node) in self.nodes) == True) and (((from_node+to_node) in self.edges)==False)):
            self.edges.append([from_node,to_node])
            self.adjency_list[from_node].append(to_node)
    
    

    def voir(self):
        print ('Nodes :', self.nodes)
        print ('Edges : ', self.edges)
        print ('Adjency list : ', self.adjency_list)
        
    def __str__(self):
        print("*************************")
        print("* Affichage d'un graphe *")
        print("*************************")
        print("Nodes:")
        print("------\n")
        for i in self.nodes():
            print ("i")
        
        
if __name__== '__main__': #permet de tester seulement si on l'appel en tant que programme
    guido_s_graph = Graph()
    
    for i in range (ord("A"), ord("G")):
        guido_s_graph.add_a_node(chr(i))
    
    guido_s_graph.add_an_edge('A','B')
    guido_s_graph.add_an_edge('A','C')
    guido_s_graph.add_an_edge('B','D')
    guido_s_graph.add_an_edge('B','C')
    guido_s_graph.add_an_edge('C','D')
    guido_s_graph.add_an_edge('D','C')
    guido_s_graph.add_an_edge('E','F')
    guido_s_graph.add_an_edge('F','C')
    
    guido_s_graph.voir()
    guido_s_graph.__str__()
