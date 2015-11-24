# -*- coding: utf-8 -*-

import unittest
import inspect

import sys
sys.path.append("..")

from Graph import *

################################################################
# Institut Villebon, UE 5.i4                                   #
# Unitary tests for the add_a_node method from the Graph class #
# Version 1                                                    #
# Author : O. Bouillot                                         #
# Creation : 22/11/15                                          #
# Last modification : 22/11/15                                 #
################################################################


class TestAddANode(unittest.TestCase):
    """ Class which is a set of unitary tests of the add_a_node method from of the Graph class
    """

    def setUp(self):
        """ Method called to prepare the test fixture """
        self.__graph = Graph()
        self.__graph.add_a_node('a')

    def test_the_contents_of_nodes(self):
        """ Test if the node 'a' is now present in the set of all the nodes of the graph """
        S = set()
        S.add('a')
        self.assertSetEqual(self.__graph.nodes, S,
                              msg = "La méthode add_a_node ne rajoute pas de sommet " +  \
                                    "dans l'attribut nodes de la classe Graph...")

    def test_the_content_of_the_adjacency_list(self):
        """ Test if the node 'a' has already be added to the adjacency list of the graph,
        without neighbor.
        """
        self.assertIn('a', self.__graph.adjacency_list,
                      msg = "La méthode add_a_node ne met pas à jour la liste " +  \
                       "d'adjacence du graphe, pourtant lorsque l'on rajoute un sommet, " +  \
                       "la liste d'adjacence se trouve allongée...")
        self.assertListEqual(self.__graph.adjacency_list['a'], [],
                             msg = "La méthode add_a_node met bien à jour la liste " + \
                             "d'adjacence, mais la liste des voisins du sommet ajouté " + \
                              "devrait être vide : en effet, aucune arête arrivant " + \
                              "ou partant de celui-ci n'a encore été ajouté au graphe...")

    def test_if_there_is_a_docstring(self):
        """ Check if there is a doc string, which is not a so trivial one... """
        self.assertNotEqual(Graph.add_a_node.__doc__, '',
                            msg = "La méthode add_a_node de la classe Graph se devrait " +  \
                                  "de possèder une docstring....")
        self.assertGreater(len(Graph.add_a_node.__doc__.replace(' ', '')), 15,
                            msg = "Je doute que l'on puisse décrire une méthode " + \
                                  "dans une docstring en utilisant aussi peu de " + \
                                  "caractères...")

    def test_the_parameters(self):
        """ Check if the parameters of the add_a_node method are correct """
        self.assertEqual(inspect.getargspec(Graph.add_a_node)[0], ['self', 'node_name'],
                         msg = "La méthode add_a_node ne possède pas la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.add_a_node)[1], None,
                         msg = "La méthode add_a_node ne possède pas la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.add_a_node)[2], None,
                         msg = "La méthode add_a_node ne possède pas la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.add_a_node)[3], None,
                         msg = "La méthode add_a_node ne possède pas la bonne signature...")

    def tearDown(self):
        """ Method called immediately after the test method has been called and
        the result recorded
        """
        self.__graph = None

if __name__ == '__main__':
    unittest.main()
