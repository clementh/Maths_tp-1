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
        Method to create the graph
        
        no args
        
        Returns
            heading(string) : just a tittle
            nodes(string): just to put the nodes name in a single variable
            egdes(string): similar to nodes 
            footer(string): end of the pages
            
        """
        heading = "∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗\n Affichage d'un graphe \n∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗\n"
        nodes = "Nodes:\n−−−−−−\n\n"+', '.join(self.nodes)
        edges = "\n\nEdges:\n−−−−−−\n\n"
        for num_edge in self.edges:
            edges+=num_edge[0]+' −−−> '+num_edge[1]+'\n'
        footer = "========================="
        return heading+nodes+edges+footer
        
    def breadth_first_search (self) : # fonction pour parcourir le graphe en largeur
        """docstring"""
        
        parents=dict()          # dictionnaire contenant l'enfant en clé et le parents en valeurs
        colors= dict()              # dico qui contient le sommet en clé et ca couleur
        fifo=[]                     # list, j'ai pas très bien compris comment elle marche
        S=0
        for S in self.nodes:            # permet de mettre tous les noeud en blanc
            colors[S]="White"
            
        for S in self.nodes:        # S parcours les noeud
            fifo.append(S)          # ajout de S dans la list
            colors[S]="black"           # S est observer il devient noir
            #print "parents: ",S
            if self.adjacency_list[S] != []:        # on vérifie que le sommet S à des voisin (enfants) si oui on continue
                for E in self.adjacency_list[S]:    # on parcours les voisin de S appelé E(enfant)
                   # print "enfant :", E            
                    colors[E]="grey"                # les enfants observer devienne gris
                    parents[E]=[S]                  # mise a jours du dictionnaire
                  
                    #print parents       
            else:
                colors[S]="black"
    
        
if __name__== '__main__': #permet de tester seulement si on l'appel en tant que programme
    G = Graph()
    
    #creation du graph avec une boucle pour entrer les sommets de A to F
    for i in range (ord("A"), ord("G")): #ord("A") permet de prendre la valeur ascii du caractere
        G.add_a_node(chr(i)) #chr(i) permet de redonner le caractere correspondant a la valeur ascii
    
    G.add_an_edge('A','B')
    G.add_an_edge('A','C')
    G.add_an_edge('B','D')
    G.add_an_edge('B','C')
    G.add_an_edge('C','D')
    G.add_an_edge('D','C')
    G.add_an_edge('E','F')
    G.add_an_edge('F','C')
    guido_s_graph = G.__str__()
    print (guido_s_graph)
    
    
