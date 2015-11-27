# -*- coding: utf-8 -*-

import unittest
import inspect

import sys
sys.path.append("..")

from Graph import *

#####################################################################
# Institut Villebon, UE 5.i4                                        #
# Unitary tests for the is_non_oriented method from the Graph class #
# Version 1                                                         #
# Author : O. Bouillot                                              #
# Creation : 22/11/15                                               #
# Last modification : 22/11/1                                       #
#####################################################################


class TestIsNonOriented(unittest.TestCase):
    """ Class which is a set of unitary tests of the is_non_oriented method
    from of the Graph class
    """

    def setUp(self):
        """ Method called to prepare the test fixture """
        self.__graph_1 = Graph()
        self.__graph_1.add_a_node('a')
        self.__graph_1.add_a_node('b')
        self.__graph_1.add_a_node('c')
        self.__graph_1.add_a_node('d')
        self.__graph_1.add_a_node('e')
        self.__graph_1.add_a_node('f')
        self.__graph_1.add_a_node('g')
        self.__graph_1.add_a_node('h')
        self.__graph_1.add_a_node('i')
        self.__graph_1.add_a_node('j')
        self.__graph_1.add_a_node('k')
        self.__graph_1.add_a_node('l')
        self.__graph_1.add_a_node('m')
        self.__graph_1.add_a_node('n')
        self.__graph_1.add_an_edge('a', 'b')
        self.__graph_1.add_an_edge('b', 'e')
        self.__graph_1.add_an_edge('b', 'f')
        self.__graph_1.add_an_edge('f', 'k')
        self.__graph_1.add_an_edge('f', 'l')
        self.__graph_1.add_an_edge('a', 'c')
        self.__graph_1.add_an_edge('c', 'g')
        self.__graph_1.add_an_edge('c', 'h')
        self.__graph_1.add_an_edge('c', 'i')
        self.__graph_1.add_an_edge('a', 'd')
        self.__graph_1.add_an_edge('d', 'j')
        self.__graph_1.add_an_edge('j', 'm')
        self.__graph_1.add_an_edge('j', 'n')

        self.__graph_2 = Graph()
        self.__graph_2.add_a_node('a')
        self.__graph_2.add_a_node('b')
        self.__graph_2.add_a_node('c')
        self.__graph_2.add_a_node('d')
        self.__graph_2.add_a_node('e')
        self.__graph_2.add_a_node('f')
        self.__graph_2.add_an_edge('a', 'b')
        self.__graph_2.add_an_edge('a', 'c')
        self.__graph_2.add_an_edge('b', 'c')
        self.__graph_2.add_an_edge('b', 'd')
        self.__graph_2.add_an_edge('c', 'd')
        self.__graph_2.add_an_edge('d', 'c')
        self.__graph_2.add_an_edge('e', 'f')
        self.__graph_2.add_an_edge('f', 'c')

        self.__graph_3 = Graph()
        self.__graph_3.add_a_node('a')
        self.__graph_3.add_a_node('b')
        self.__graph_3.add_a_node('c')
        self.__graph_3.add_a_node('d')
        self.__graph_3.add_a_node('e')
        self.__graph_3.add_a_node('f')
        self.__graph_3.add_a_node('g')
        self.__graph_3.add_a_node('h')
        self.__graph_3.add_a_node('i')
        self.__graph_3.add_a_node('j')
        self.__graph_3.add_a_node('k')
        self.__graph_3.add_a_node('l')
        self.__graph_3.add_a_node('m')
        self.__graph_3.add_a_node('n')
        self.__graph_3.add_an_edge('a', 'b')
        self.__graph_3.add_an_edge('b', 'a')
        self.__graph_3.add_an_edge('b', 'e')
        self.__graph_3.add_an_edge('e', 'b')
        self.__graph_3.add_an_edge('b', 'f')
        self.__graph_3.add_an_edge('f', 'b')
        self.__graph_3.add_an_edge('f', 'k')
        self.__graph_3.add_an_edge('k', 'f')
        self.__graph_3.add_an_edge('f', 'l')
        self.__graph_3.add_an_edge('l', 'f')
        self.__graph_3.add_an_edge('a', 'c')
        self.__graph_3.add_an_edge('c', 'a')
        self.__graph_3.add_an_edge('c', 'g')
        self.__graph_3.add_an_edge('g', 'c')
        self.__graph_3.add_an_edge('c', 'h')
        self.__graph_3.add_an_edge('h', 'c')
        self.__graph_3.add_an_edge('c', 'i')
        self.__graph_3.add_an_edge('i', 'c')
        self.__graph_3.add_an_edge('a', 'd')
        self.__graph_3.add_an_edge('d', 'a')
        self.__graph_3.add_an_edge('d', 'j')
        self.__graph_3.add_an_edge('j', 'd')
        self.__graph_3.add_an_edge('j', 'm')
        self.__graph_3.add_an_edge('m', 'j')
        self.__graph_3.add_an_edge('j', 'n')
        self.__graph_3.add_an_edge('n', 'j')

        self.__graph_4 = Graph()
        self.__graph_4.add_a_node('a')
        self.__graph_4.add_a_node('b')
        self.__graph_4.add_a_node('c')
        self.__graph_4.add_a_node('d')
        self.__graph_4.add_a_node('e')
        self.__graph_4.add_a_node('f')
        self.__graph_4.add_a_node('g')
        self.__graph_4.add_a_node('h')
        self.__graph_4.add_an_edge('a', 'c')
        self.__graph_4.add_an_edge('c', 'a')
        self.__graph_4.add_an_edge('b', 'a')
        self.__graph_4.add_an_edge('a', 'b')
        self.__graph_4.add_an_edge('b', 'd')
        self.__graph_4.add_an_edge('d', 'b')
        self.__graph_4.add_an_edge('b', 'e')
        self.__graph_4.add_an_edge('e', 'b')
        self.__graph_4.add_an_edge('c', 'd')
        self.__graph_4.add_an_edge('d', 'c')
        self.__graph_4.add_an_edge('e', 'd')
        self.__graph_4.add_an_edge('d', 'e')
        self.__graph_4.add_an_edge('e', 'f')
        self.__graph_4.add_an_edge('f', 'e')
        self.__graph_4.add_an_edge('f', 'g')
        self.__graph_4.add_an_edge('g', 'f')
        self.__graph_4.add_an_edge('g', 'e')
        self.__graph_4.add_an_edge('e', 'g')
        self.__graph_4.add_an_edge('g', 'h')
        self.__graph_4.add_an_edge('h', 'g')

    def test_1_of_is_non_oriented(self):
        """ Test the return value of the  breadth_first_search_method from the Graph class """
        self.assertFalse(self.__graph_1.is_non_oriented(),
                         msg = "La méthode is_non_oriented ne renvois " + \
                               "pas le bon résultat...")

    def test_2_of_is_non_oriented(self):
        """ Test the return value of the depth_first_search_method from the Graph class """
        self.assertFalse(self.__graph_2.is_non_oriented(),
                         msg = "La méthode is_non_oriented ne renvois " + \
                               "pas le bon résultat...")

    def test_3_of_is_non_oriented(self):
        """ Test the return value of the depth_first_search_method from the Graph class """
        self.assertTrue(self.__graph_3.is_non_oriented(),
                         msg = "La méthode is_non_oriented ne renvois " + \
                               "pas le bon résultat...")

    def test_4_of_is_non_oriented(self):
        """ Test the return value of the depth_first_search_method from the Graph class """
        self.assertTrue(self.__graph_4.is_non_oriented(),
                         msg = "La méthode is_non_oriented ne renvois " + \
                               "pas le bon résultat...")

    def test_if_there_is_a_docstring(self):
        """ Check if there is a doc string, which is not a so trivial one... """
        self.assertNotEqual(Graph.is_non_oriented.__doc__, '',
                            msg = "La méthode is_non_oriented de la classe "+ \
                                  " Graph se devrait de possèder une docstring....")
        self.assertGreater(len(Graph.is_non_oriented.__doc__.replace(' ', '')), 15,
                            msg = "Je doute que l'on puisse décrire une méthode " + \
                                  "dans une docstring en utilisant aussi peu de " + \
                                  "caractères...")

    def test_the_parameters(self):
        """ Check if the parameters of the is_non_oriented method are correct """
        self.assertEqual(inspect.getargspec(Graph.is_non_oriented)[0],
                         ['self'],
                         msg = "La méthode is_non_oriented ne possède pas " + \
                               "la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.is_non_oriented)[1], None,
                         msg = "La méthode is_non_oriented ne possède pas " + \
                               "la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.is_non_oriented)[2], None,
                         msg = "La méthode is_non_oriented ne possède pas  " + \
                               "la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.is_non_oriented)[3], None,
                         msg = "La méthode is_non_oriented ne possède pas  " + \
                               "la bonne signature...")

    def tearDown(self):
        """ Method called immediately after the test method has been called and
        the result recorded
        """
        self.__graph_1 = None
        self.__graph_2 = None
        self.__graph_3 = None
        self.__graph_4 = None

if __name__ == '__main__':
    unittest.main()
