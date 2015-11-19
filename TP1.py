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
        """
        Method to create an edges between 2 nodes (from_node and to_node) on the graph
        
        Args :
            from_node(string): the name of the origine of the edge
                for example $ from_node = 'Orsay' $ if the edge is from Orsay to Paris
            to_node(string): the name of the end of the edge
                for example $ to_node = 'Paris' $ if the edge is from Orsay to Paris
        
        Returns :
            None
            
        Example of calling
            $ add_an_edge('Orsay', 'Paris')
        """
        
        if((((from_node and to_node) in self.nodes) == True) and (((from_node+to_node) in self.edges)==False)): #on test tout d'abord si les nodes de depart et d'arrives sont bien dans l'ensemble et si l'arete n'est pas deja existante
            self.edges.append([from_node,to_node])
            self.adjency_list[from_node].append(to_node)
    
        
    def __str__(self):
        """
        Method to show the graph in the terminal
        
        no args
        
        no returns
        """
        
        print("∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗")
        print("∗ Affichage d'un graphe ∗")
        print("∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗")
        
        print("Nodes:")
        print("−−−−−−\n")
        t = 0
        for node in sorted(self.nodes): #on realise un tri de l'ensemble pour l'afficher dans un ordre croissant
            t+=1                        #iterateur pour savoir quand nous aurons traites tout les element de l'ensemble afin de ne pas afficher de virgule inutile
            if (t == len(self.nodes)):  #on test si on a parcouru tout les element de l'ensemble
                print (node)            #si oui, on affiche seulement l'element et on passe a la ligne
            else :
                print (node,end=', ')   #sinon on affiche l'element avec un virgule, puis un espace sans passer a la ligne
        print ()
                
        print("Edges:")
        print("−−−−−−\n")
        for edge in self.edges:
            print(str(edge[0])+str(' −−−> ')+str(edge[1])) #on utilise str() pour ne pas avoir les '' encadrant le caractere et le + afin de tout mettre ensemble comme une seule chaine de caractere
        
        print('=========================')
        
        
if __name__== '__main__': #permet de tester seulement si on l'appel en tant que programme
    guido_s_graph = Graph()
    
    #creation du graph avec une boucle pour entrer les sommets de A to F
    for i in range (ord("A"), ord("G")): #ord("A") permet de prendre la valeur ascii du caractere
        guido_s_graph.add_a_node(chr(i)) #chr(i) permet de redonner le caractere correspondant a la valeur ascii
    
    guido_s_graph.add_an_edge('A','B')
    guido_s_graph.add_an_edge('A','C')
    guido_s_graph.add_an_edge('B','D')
    guido_s_graph.add_an_edge('B','C')
    guido_s_graph.add_an_edge('C','D')
    guido_s_graph.add_an_edge('D','C')
    guido_s_graph.add_an_edge('E','F')
    guido_s_graph.add_an_edge('F','C')
    
    guido_s_graph.__str__()
