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
        self.adjacency_list = {}
        self.parents = {}
                
        
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
            self.adjacency_list[node_name]= []
            self.parents[node_name]=[]
            
    def add_an_edge(self, from_node, to_node):
        """
        Method to create an edges between 2 nodes (from_node and to_node) on the graph
        
        Args :
            from_node(string): the name of the origin of the edge
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
            self.adjacency_list[from_node].append(to_node)
            
    
        
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
        heading = "**************************\n*  Display of the graph  *\n**************************\n"
        nodes = "Nodes:\n------\n\n"+', '.join(self.nodes)
        edges = "\n\nEdges:\n-------\n\n"
        for num_edge in self.edges:
            edges+=num_edge[0]+' ---> '+num_edge[1]+'\n'
        footer = "========================="
        return heading+nodes+edges+footer
        
    def breadth_first_search (self,departure) : # fonction pour parcourir le graphe en largeur
        """docstring"""
        parents={}
        colors= {}              # dico qui contient le sommet en cle et ca couleur
        fifo=[]                     # list, j'ai pas tres bien compris comment elle marche
        
        for i in self.nodes:
            colors[i]="white"
        parents[departure]='none'    
        fifo.append(departure)
        colors[departure]="grey"
        while (fifo != []):
            summit=fifo[0]
            for num_edge in self.edges:  
                if (summit in num_edge):
                    if((summit==num_edge[0]) & (colors[num_edge[1]]=="white")):
                        parents[num_edge[1]]=summit
                        fifo.append(num_edge[1])
                        colors[num_edge[1]] = "grey"
            fifo.remove(summit)
            colors[summit]="black"  
    
        
        
    def depth_first_search(self,departure):
        parents = {}
        colors = {}

        for i in list(self.nodes):
            colors[i] = 'white'

        colors[departure] = 'grey'
        parents[departure]='none'
        lifo = [departure]
        father = departure

        while lifo != [] :
            breaked = 0
            for child in self.adjacency_list[father]:
                if (colors[child]=='white'):
                    parents[child] = father
                    lifo.append(child)
                    colors[child] = 'grey'
                    father = lifo[-1]
                    breaked = 1
                    break

            if (breaked == 0):
                colors[father] = 'black'
                lifo.pop()
            if (lifo != []) :
                father = lifo[-1]


        return parents,colors

        
        
if __name__== '__main__': #permet de tester seulement si on l'appel en tant que programme
    G = Graph()

    #creation des sommets du graph
    for i in range (ord("A"), ord("G")): #ord("A") permet de prendre la valeur ascii du caractere
        G.add_a_node(chr(i)) #chr(i) permet de redonner le caractere correspondant a la valeur ascii

    #creation des aretes du graph
    G.add_an_edge('A','B')
    G.add_an_edge('A','C')
    G.add_an_edge('A','D')
    G.add_an_edge('B','C')
    G.add_an_edge('C','D')
    G.add_an_edge('D','C')
    G.add_an_edge('E','F')
    G.add_an_edge('F','C')



    departure='A'
    G.depth_first_search(departure)
    G.breadth_first_search(departure)
    
