# -*- coding: utf-8 -*-

import unittest
import inspect

import sys
sys.path.append("..")

from Graph import *

#############################################################
# Institut Villebon, UE 5.i4                                #
# Unitary tests for the __str__ method from the Graph class #
# Version 1                                                 #
# Author : O. Bouillot                                      #
# Creation : 22/11/15                                       #
# Last modification : 22/11/15                              #
#############################################################


class TestStr(unittest.TestCase):
    """ Class which is a set of unitary tests of the __str__ method from of the Graph class
    """

    def setUp(self):
        """ Method called to prepare the test fixture """
        self.__graph_1 = Graph()
        self.__graph_1.add_a_node('a')
        self.__graph_1.add_a_node('b')
        self.__graph_1.add_an_edge('a', 'b')

    def test_on_the_result_of___str__(self):
        """ Test if the result of the __str__ method is of type String """
        self.assertEqual(type(self.__graph_1.__str__()), type(' '),
                         msg = "La méthode __str__ doit renvoyer une  " +  \
                               "chaine de caractère, et non pas utiliser des prints....")

    def test_if_there_is_a_docstring(self):
        """ Check if there is a doc string, which is not a so trivial one... """
        self.assertNotEqual(Graph.__str__.__doc__, '',
                            msg = "La méthode __str__ de la classe Graph se devrait " +  \
                                  "de possèder une docstring....")
        self.assertGreater(len(Graph.__str__.__doc__.replace(' ', '')), 15,
                            msg = "Je doute que l'on puisse décrire une méthode " + \
                                  "dans une docstring en utilisant aussi peu de " + \
                                  "caractères...")

    def test_the_parameters(self):
        """ Check if the parameters of the add_an_edge method are correct """
        self.assertEqual(inspect.getargspec(Graph.__str__)[0],
                         ['self'],
                         msg = "La méthode __str__ ne possède pas la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.add_an_edge)[1], None,
                         msg = "La méthode __str__ ne possède pas la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.add_an_edge)[2], None,
                         msg = "La méthode __str__ ne possède pas la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.add_an_edge)[3], None,
                         msg = "La méthode __str__ ne possède pas la bonne signature...")

    def tearDown(self):
        """ Method called immediately after the test method has been called and
        the result recorded
        """
        self.__graph_1 = None

if __name__ == '__main__':
    unittest.main()
