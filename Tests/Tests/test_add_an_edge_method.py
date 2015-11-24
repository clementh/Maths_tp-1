# -*- coding: utf-8 -*-

import unittest
import inspect

import sys
sys.path.append("..")

from Graph import *

#################################################################
# Institut Villebon, UE 5.i4                                    #
# Unitary tests for the add_an_edge method from the Graph class #
# Version 1                                                     #
# Author : O. Bouillot                                          #
# Creation : 22/11/15                                           #
# Last modification : 22/11/15                                  #
#################################################################


class TestAddAnEdge(unittest.TestCase):
    """ Class which is a set of unitary tests of the add_an_edge method from of the Graph class
    """

    def setUp(self):
        """ Method called to prepare the test fixture """
        self.__graph_1 = Graph()
        self.__graph_1.add_a_node('a')
        self.__graph_1.add_a_node('b')
        self.__graph_1.add_an_edge('a', 'b')
        self.__graph_2 = Graph()

    def test_1_on_the_contents_of_edges(self):
        """ Test how the attribute edges behaves after trying to add an edge in the graph """
        L = list()
        L.append(('a', 'b'))
        self.assertListEqual(self.__graph_1.edges, L,
                              msg = "La méthode add_an_edge ne rajoute pas d'arête " +  \
                                    "dans l'attribut edges de la classe Graph...")

    def test_2_on_the_contents_of_edges(self):
        """ Test how the attribute edges behaves after trying to add an edge in the graph """
        L = list()
        L.append(('a', 'b'))
        with self.assertRaises(NameError):
            self.__graph_2.add_an_edge('a', 'b')
#                          msg =  "La méthode add_an_edge ne doit pas ajouter d'arête " +  \
#                                 "dans l'attribut edges de la classe Graph lorsque " +  \
#                                 "les extrémités de l'arêtes sont des sommets qui " +  \
#                                 "n'ont pas encore été ajoutés..., mais doit lever une " +  \
#                                 "exception de type NameError")

    def test_the_content_of_the_adjacency_list(self):
        """ Test if the edge between 'a' and 'b' has already be added to the adjacency
        list of the graph.
        """
        self.assertListEqual(['b'], self.__graph_1.adjacency_list['a'],
                      msg = "La méthode add_an_edge ne met pas à jour la liste " +  \
                       "d'adjacence du graphe, pourtant lorsque l'on rajoute une arête " +  \
                       "entre deux sommets, un voisin doit être ajouté...")

    def test_if_there_is_a_docstring(self):
        """ Check if there is a doc string, which is not a so trivial one... """
        self.assertNotEqual(Graph.add_an_edge.__doc__, '',
                            msg = "La méthode add_an_edge de la classe Graph se devrait " +  \
                                  "de possèder une docstring....")
        self.assertGreater(len(Graph.add_an_edge.__doc__.replace(' ', '')), 15,
                            msg = "Je doute que l'on puisse décrire une méthode " + \
                                  "dans une docstring en utilisant aussi peu de " + \
                                  "caractères...")

    def test_the_parameters(self):
        """ Check if the parameters of the add_an_edge method are correct """
        self.assertEqual(inspect.getargspec(Graph.add_an_edge)[0],
                         ['self', 'from_node', 'to_node'],
                         msg = "La méthode add_an_edge ne possède pas la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.add_an_edge)[1], None,
                         msg = "La méthode add_an_edge ne possède pas la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.add_an_edge)[2], None,
                         msg = "La méthode add_an_edge ne possède pas la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.add_an_edge)[3], None,
                         msg = "La méthode add_an_edge ne possède pas la bonne signature...")

    def tearDown(self):
        """ Method called immediately after the test method has been called and
        the result recorded
        """
        self.__graph_1 = None
        self.__graph_2 = None

if __name__ == '__main__':
    unittest.main()
