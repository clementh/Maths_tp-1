# -*- coding: utf-8 -*-

import unittest
import inspect

import sys
sys.path.append("..")
from Graph import *

##################################################################
# Institut Villebon, UE 5.i4                                     #
# Unitary tests for the is_connected method from the Graph class #
# Version 1                                                      #
# Author : O. Bouillot                                           #
# Creation : 22/11/15                                            #
# Last modification : 22/11/1                                    #
##################################################################


class TestConnectedComponents(unittest.TestCase):
    """ Class which is a set of unitary tests of the is_connected
    method from of the Graph class
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
        self.__graph_2.add_an_edge('b', 'a')
        self.__graph_2.add_an_edge('a', 'c')
        self.__graph_2.add_an_edge('c', 'a')
        self.__graph_2.add_an_edge('b', 'c')
        self.__graph_2.add_an_edge('c', 'b')
        self.__graph_2.add_an_edge('b', 'd')
        self.__graph_2.add_an_edge('d', 'b')
        self.__graph_2.add_an_edge('c', 'd')
        self.__graph_2.add_an_edge('d', 'c')
        self.__graph_2.add_an_edge('e', 'f')
        self.__graph_2.add_an_edge('f', 'e')
        self.__graph_2.add_an_edge('f', 'c')
        self.__graph_2.add_an_edge('c', 'f')

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

        self.__graph_5 = Graph()
        self.__graph_5.add_a_node('a1')
        self.__graph_5.add_a_node('b1')
        self.__graph_5.add_a_node('c1')
        self.__graph_5.add_a_node('d1')
        self.__graph_5.add_a_node('e1')
        self.__graph_5.add_a_node('f1')
        self.__graph_5.add_a_node('a2')
        self.__graph_5.add_a_node('b2')
        self.__graph_5.add_a_node('c2')
        self.__graph_5.add_a_node('d2')
        self.__graph_5.add_a_node('e2')
        self.__graph_5.add_a_node('f2')
        self.__graph_5.add_a_node('g2')
        self.__graph_5.add_a_node('h2')
        self.__graph_5.add_a_node('i2')
        self.__graph_5.add_a_node('j2')
        self.__graph_5.add_a_node('k2')
        self.__graph_5.add_a_node('l2')
        self.__graph_5.add_a_node('m2')
        self.__graph_5.add_a_node('n2')
        self.__graph_5.add_a_node('a3')
        self.__graph_5.add_a_node('b3')
        self.__graph_5.add_a_node('c3')
        self.__graph_5.add_a_node('d3')
        self.__graph_5.add_a_node('e3')
        self.__graph_5.add_a_node('f3')
        self.__graph_5.add_a_node('g3')
        self.__graph_5.add_a_node('h3')
        self.__graph_5.add_an_edge('a1', 'b1')
        self.__graph_5.add_an_edge('b1', 'a1')
        self.__graph_5.add_an_edge('a1', 'c1')
        self.__graph_5.add_an_edge('c1', 'a1')
        self.__graph_5.add_an_edge('b1', 'c1')
        self.__graph_5.add_an_edge('c1', 'b1')
        self.__graph_5.add_an_edge('b1', 'd1')
        self.__graph_5.add_an_edge('d1', 'b1')
        self.__graph_5.add_an_edge('c1', 'd1')
        self.__graph_5.add_an_edge('d1', 'c1')
        self.__graph_5.add_an_edge('e1', 'f1')
        self.__graph_5.add_an_edge('f1', 'e1')
        self.__graph_5.add_an_edge('f1', 'c1')
        self.__graph_5.add_an_edge('c1', 'f1')
        self.__graph_5.add_an_edge('a2', 'b2')
        self.__graph_5.add_an_edge('b2', 'a2')
        self.__graph_5.add_an_edge('b2', 'e2')
        self.__graph_5.add_an_edge('e2', 'b2')
        self.__graph_5.add_an_edge('b2', 'f2')
        self.__graph_5.add_an_edge('f2', 'b2')
        self.__graph_5.add_an_edge('f2', 'k2')
        self.__graph_5.add_an_edge('k2', 'f2')
        self.__graph_5.add_an_edge('f2', 'l2')
        self.__graph_5.add_an_edge('l2', 'f2')
        self.__graph_5.add_an_edge('a2', 'c2')
        self.__graph_5.add_an_edge('c2', 'a2')
        self.__graph_5.add_an_edge('c2', 'g2')
        self.__graph_5.add_an_edge('g2', 'c2')
        self.__graph_5.add_an_edge('c2', 'h2')
        self.__graph_5.add_an_edge('h2', 'c2')
        self.__graph_5.add_an_edge('c2', 'i2')
        self.__graph_5.add_an_edge('i2', 'c2')
        self.__graph_5.add_an_edge('a2', 'd2')
        self.__graph_5.add_an_edge('d2', 'a2')
        self.__graph_5.add_an_edge('d2', 'j2')
        self.__graph_5.add_an_edge('j2', 'd2')
        self.__graph_5.add_an_edge('j2', 'm2')
        self.__graph_5.add_an_edge('m2', 'j2')
        self.__graph_5.add_an_edge('j2', 'n2')
        self.__graph_5.add_an_edge('n2', 'j2')
        self.__graph_5.add_an_edge('a3', 'c3')
        self.__graph_5.add_an_edge('c3', 'a3')
        self.__graph_5.add_an_edge('b3', 'a3')
        self.__graph_5.add_an_edge('a3', 'b3')
        self.__graph_5.add_an_edge('b3', 'd3')
        self.__graph_5.add_an_edge('d3', 'b3')
        self.__graph_5.add_an_edge('b3', 'e3')
        self.__graph_5.add_an_edge('e3', 'b3')
        self.__graph_5.add_an_edge('c3', 'd3')
        self.__graph_5.add_an_edge('d3', 'c3')
        self.__graph_5.add_an_edge('e3', 'd3')
        self.__graph_5.add_an_edge('d3', 'e3')
        self.__graph_5.add_an_edge('e3', 'f3')
        self.__graph_5.add_an_edge('f3', 'e3')
        self.__graph_5.add_an_edge('f3', 'g3')
        self.__graph_5.add_an_edge('g3', 'f3')
        self.__graph_5.add_an_edge('g3', 'e3')
        self.__graph_5.add_an_edge('e3', 'g3')
        self.__graph_5.add_an_edge('g3', 'h3')
        self.__graph_5.add_an_edge('h3', 'g3')

    def test_1_of_is_connected(self):
        """ Test the return value of the is_connected method from the Graph class """
        self.assertTrue(self.__graph_2.is_connected(),
                        msg = "La méthode is_connected ne renvois " + \
                              "pas le bon résultat...")

    def test_2_of_is_connected(self):
        """ Test the return value of the is_connected  method from the Graph class """
        self.assertTrue(self.__graph_3.is_connected(),
                        msg = "La méthode is_connected ne renvois " + \
                              "pas le bon résultat...")

    def test_3_of_is_connected(self):
        """ Test the return value of the is_connected method from the Graph class """
        self.assertTrue(self.__graph_4.is_connected(),
                        msg = "La méthode is_connected ne renvois " + \
                              "pas le bon résultat...")

    def test_4_of_is_connected(self):
        """ Test the return value of the is_connected method from the Graph class """
        self.assertFalse(self.__graph_5.is_connected(),
                         msg = "La méthode is_connected ne renvois " + \
                               "pas le bon résultat...")

    def test_5_of_connected_components(self):
        """ Test connected_components method from the Graph class on a oriented graph"""
        with self.assertRaises(TypeError):
            self.__graph_1.connected_components()

    def test_if_there_is_a_docstring(self):
        """ Check if there is a doc string, which is not a so trivial one... """
        self.assertNotEqual(Graph.is_connected.__doc__, '',
                            msg = "La méthode is_connected de la classe "+ \
                                  " Graph se devrait de possèder une docstring....")
        self.assertGreater(len(Graph.is_connected.__doc__.replace(' ', '')), 15,
                            msg = "Je doute que l'on puisse décrire une méthode " + \
                                  "dans une docstring en utilisant aussi peu de " + \
                                  "caractères...")

    def test_the_parameters(self):
        """ Check if the parameters of the is_non_oriented method are correct """
        self.assertEqual(inspect.getargspec(Graph.is_non_oriented)[0],
                         ['self'],
                         msg = "La méthode is_connected ne possède pas " + \
                               "la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.is_non_oriented)[1], None,
                         msg = "La méthode is_connected ne possède pas " + \
                               "la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.is_non_oriented)[2], None,
                         msg = "La méthode is_connected ne possède pas  " + \
                               "la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.is_non_oriented)[3], None,
                         msg = "La méthode is_connected ne possède pas  " + \
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
