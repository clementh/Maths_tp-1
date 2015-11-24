# -*- coding: utf-8 -*-

import unittest

import sys
sys.path.append("..")

from Graph import *

########################################################
# Institut Villebon, UE 5.i4                           #
# Unitary tests for the constructor of the Graph class #
# Version 1                                            #
# Author : O. Bouillot                                 #
# Creation : 22/11/15                                  #
# Last modification : 22/11/15                         #
########################################################



class TestGraphConstructor(unittest.TestCase):
    """ Class which is a set of unitary tests of the constructor of the Graph class """

    def setUp(self):
        """ Method called to prepare the test fixture """
        self.__graph = Graph()

    def test_constructor(self):
        """ Test the initialization of a Graph object """
        self.assertIsInstance(self.__graph, Graph,
                              msg = "Problème d'initialisation d'un objet Graph")

    def test_if_there_is_a_docstring(self):
        """ Check if there is a doc string, which is not a so trivial one... """
        self.assertNotEqual(Graph.__init__.__doc__, '',
                            msg = "Le constructeur de la classe Graph se devrait " +  \
                                  "de possèder une docstring....")
        self.assertGreater(len(Graph.__init__.__doc__.replace(' ', '')), 15,
                            msg = "Je doute que l'on puisse décrire une méthode " + \
                                  "dans une docstring en utilisant aussi peu de " + \
                                  "caractères...")

    def test_number_of_attribute(self):
        """ Check if the Graph class has eactly three attibutes """
        self.assertEqual(len(self.__graph.__dict__.keys()), 3,
                         msg = "La classe Graph doit posséder exactement trois " + \
                               ", mais en possède actuellement " +  \
                               str(len(self.__graph.__dict__.keys())) + "...")

    def test_nodes_initialisation(self):
        """ Check if the attribute 'nodes' is present and well initialized """
        try:
            nodes = getattr(self.__graph, "nodes")
        except AttributeError:
            self.fail("La classe Graph doit posseder un attribut nommé 'nodes'")
        self.assertSetEqual(nodes, set(),
                            msg = "Lors de l'initialisation, l'attribut nodes doit" + \
                                  " être initialisé à l'ensemble vide")

    def test_edges_initialisation(self):
        """ Check if the attribute 'edges' is present and well initialized """
        try:
            edges = getattr(self.__graph, "edges")
        except AttributeError:
            self.fail("La classe Graph doit posseder un attribut nommé 'edges'")
        self.assertListEqual(edges, list(),
                            msg = "Lors de l'initialisation, l'attribut edges doit" + \
                                  " être initialisé à la liste vide")

    def test_adjacency_list_initialisation(self):
        """ Check if the attribute 'adjacency_list' is present and well initialized """
        try:
            adjacency_list = getattr(self.__graph, "adjacency_list")
        except AttributeError:
            self.fail("La classe Graph doit posseder un attribut nommé 'adjacency_list'")
        self.assertDictEqual(adjacency_list, dict(),
                             msg = "Lors de l'initialisation, l'attribut " + \
                                   "adjacency_list doit être initialisé comme " + \
                                   "étant un dictionnaire vide")

    def tearDown(self):
        """ Method called immediately after the test method has been called and
        the result recorded
        """
        self.__graph = None

if __name__ == '__main__':
    unittest.main()
