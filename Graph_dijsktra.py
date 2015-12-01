#!/usr/bin/env python3



#################################################################
# Institut Villebon, UE 5.i4                                    #
# UE 5i4 : TP_2  Graph class ammelioration & Dijsktra algorithme#
# Version 1                                                     #
# Author : E.Albrand & C.Herat                                  #
# Creation : 01/12/2016                                         #
# Last modification :                                           #
#################################################################

class Graph():
    """This class aims to create graph and methods for analyzing
    ============================================================
    
    This class contains the following methods  :
    """


    def __init__(self):
        """Constructor of the class Graph. Initialize the graph's objects
        =================================================================
        Objects :
        ---------
            self.nodes : set() contains nodes names
            self.edges : list() : contains edges (from node, to node)
            self.adjacency_list : dict() : {summit: [list of successors]}"""
        
        self.nodes = set()
        self.edges = []
        self.adjacency_list = {}




if __name__== '__main__': #permet de tester seulement si on l'appel en tant que programme
    print ('Hello world')

