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
#################################################################
# Institut Villebon, UE 5.i4                                    #
# UE 5i4 : TP_1  Graph Theory                                   #
# Version 1                                                     #
# Author : E.Albrand & C.Herat                                  #
# Creation :                                                    #
# Last modification :                                           #
#################################################################

class Graph():
    """ docstring """
    
    def __init__(self):
        """__init__ initialize the set self.nodes, the list self.edges and the dictionnary self.adjacency_list. Which respectively contains the nodes names, the edges (from node ,to node) and the adjacency list: [father]=[ childrens ] """
        
        self.nodes = set()
        self.edges = []
        self.adjacency_list = {}
                
        
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
            self.edges.append((from_node,to_node))
            self.adjacency_list[from_node].append(to_node)
        else:
            raise NameError("not possible. Node don't exist")
            
            
    
        
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
        """This function do the path width
            Args:      None 
            
            storage: parents {}: dictionnary wich contain the children for the key and the parents for value.
                     colors{}: dictionnary wich contain a color for value, for every node (the key)
                     fifo[]: list for scroll the node we browse
                     
            Returns: parents and colors.
            
            For the first step we initialize  all node colors to white.
            Next we begin with  the departure node, parents dictionnary  learn 'none',
            colors become grey and fifo append departure
            Father become the first node of fifo list.
            After we browse the list of edges in our graph.
            If there are an edges where father is the first in the list (the father),
            so the second node is the children.
            The  programms do this action:
                Colors[children]: become grey
                parents[children] become father
                and fifo append children
             When all the edges was seen, father is remove from fifo and his color become black
             the loop restar with a new node for father: the first one in fifo list.
             
             The colors allow to be sure the loop don't pass twice by the same node.
             while fifo is while fifo is not empty we stay in the loop
             """
        parents = dict ()
        colors = dict ()               # dico qui contient le sommet en cle et ca couleur
        fifo = []                     # list, j'ai pas tres bien compris comment elle marche
        
        for i in self.nodes:
            colors[i]="white"
            
        parents[departure] = None    
        fifo.append(departure)
        colors[departure]="grey"
        while (fifo != []):
            father = fifo[0]
            for num_edge in self.edges:  
                if (father in num_edge):
                    if((father == num_edge[0]) & (colors[num_edge[1]] == "white")):
                        parents[num_edge[1]] = father
                        fifo.append(num_edge[1])
                        colors[num_edge[1]] = "grey"
            fifo.remove(father)
            colors[father] = "black"
            
        return parents
        
    def depth_first_search(self,departure):
        """fdslkfkdsfjkldsfjkldsjfkldsjfkldsffszfds fdsfkldsj fdfs fdkfkdfkh dfhskjlhfkjdsfhkjdshfkj fsdhfkjhdskjfhdskj fdsjfkhdskjfhdsk"""
        parents = {}
        colors = {}

        for i in list(self.nodes):
            colors[i] = 'white'

        colors[departure] = 'grey'
        parents[departure]= None
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


        return parents
        
    def is_non_oriented(self):
        """ This function find if the graph is oriented or not.
        Args:   None
        
        Retunr: True of False
        
        We browse all the node (num_node) and the node in their adjacency list (next).
        We search if num_node is in the adjacency list of next. 
        If it's true we have A---> B and B--->A : it's a non oriented edges.
        the graph is oriented if there are only one edges oriented: the function return False
        But if there are no oriented edges, the function return :True. It's a non oriented graph
         """
        for num_node in self.nodes:
            for next in self.adjacency_list[num_node]:
                if ((num_node in self.adjacency_list[next]) == False):
                    print "le graph est oriente"
                    return False
        print "le graph est non-oriente"             
        return True
        
    #def connected_components(self):
    def is_connected (self):
        """This function find if the graph is connected.
            WARNING: Work only with non-oriented graph.
        Args: orientation
        
        Return :True or False.
            We browse all the node of the graph.
            'Connect' is a variable which count the connnection for a node.
            If a node don't have any connection, then  the graph is not connected.
            But if all the node have a connexion, even only one, the graph is connected:Return False
            And the function return True
            
            TypeError if the graph is non-oriented. """ 
        
        if (Graph().is_non_oriented() == True):
            for node in self.nodes:
                connect=0
                for num_edge in self.edges:
                    if ((node in num_edge[0]) & (node in num_edge[1])):
                        print node, num_edge
                        connect += 1
                if connect==0:
                    print "le graph est non connexe"
                    return False
            print  "le graph est connexe"
            return True
        else:
            raise TypeError, "Your Graph is oriented"   
                
        
        
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
    
