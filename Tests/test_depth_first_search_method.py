# -*- coding: utf-8 -*-

import unittest
import inspect

import sys
sys.path.append("..")

from Graph import *

########################################################################
# Institut Villebon, UE 5.i4                                           #
# Unitary tests for the depth_first_search method from the Graph class #
# Version 1                                                            #
# Author : O. Bouillot                                                 #
# Creation : 22/11/15                                                  #
# Last modification : 22/11/1                                          #
########################################################################


class TestDepthFirstSearch(unittest.TestCase):
    """ Class which is a set of unitary tests of the depth_first_search method
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
        self.__graph_4.add_an_edge('b', 'a')
        self.__graph_4.add_an_edge('b', 'd')
        self.__graph_4.add_an_edge('b', 'e')
        self.__graph_4.add_an_edge('c', 'd')
        self.__graph_4.add_an_edge('e', 'd')
        self.__graph_4.add_an_edge('e', 'f')
        self.__graph_4.add_an_edge('f', 'g')
        self.__graph_4.add_an_edge('g', 'e')
        self.__graph_4.add_an_edge('g', 'h')

    def test_1_of_the_depth_first_search_result(self):
        """ Test the return value of the  breadth_first_search_method from the Graph class """
        D = dict()
        D['a'] = None
        D['b'] = 'a'
        D['c'] = 'a'
        D['d'] = 'a'
        D['e'] = 'b'
        D['f'] = 'b'
        D['g'] = 'c'
        D['h'] = 'c'
        D['i'] = 'c'
        D['j'] = 'd'
        D['k'] = 'f'
        D['l'] = 'f'
        D['m'] = 'j'
        D['n'] = 'j'
        self.assertEqual(type(self.__graph_1.depth_first_search('a')), type(D),
                             msg = "La méthode depth_first_search ne retourne pas " + \
                                   "un dictionnaire...")
        self.assertDictEqual(self.__graph_1.depth_first_search('a'), D,
                             msg = "La méthode depth_first_search, appliqué à l'arbre " + \
                                   "de la section 4.2 du sujet, orienté de la racine " + \
                                   "vers ses feuilles, en partant de la racine " + \
                                   "ne retourne pas le bon dictionnaire")

    def test_2_of_the_depth_first_search_result(self):
        """ Test the return value of the depth_first_search_method from the Graph class """
        D = dict()
        D['b'] = None
        D['e'] = 'b'
        D['f'] = 'b'
        D['k'] = 'f'
        D['l'] = 'f'
        dfs = self.__graph_1.depth_first_search('b')
        self.assertEqual(type(dfs), type(D),
                             msg = "La méthode depth_first_search ne retourne pas " + \
                                   "un dictionnaire...")
        self.assertDictEqual(dfs, D,
                             msg = "La méthode depth_first_search, appliqué à l'arbre " + \
                                   "de la section 4.2 du sujet, orienté de la racine " + \
                                   "vers ses feuilles, en partant du fils " + \
                                   "le plus à gauche de la racine ne retourne pas " + \
                                   "le bon dictionnaire")

    def test_3_of_the_depth_first_search_result(self):
        """ Test the return value of the depth_first_search_method from the Graph class """
        D = dict()
        D['a'] = None
        D['b'] = 'a'
        D['c'] = 'b'
        D['d'] = 'c'
        self.assertEqual(type(self.__graph_2.depth_first_search('a')), type(D),
                             msg = "La méthode depth_first_search ne retourne pas " + \
                                   "un dictionnaire...")
        self.assertDictEqual(self.__graph_2.depth_first_search('a'), D,
                             msg = "La méthode depth_first_search, appliqué au graphe " + \
                                   "de Guido van Rossum, en partant du point A " + \
                                   "ne retourne pas le bon dictionnaire")

    def test_4_of_the_depth_first_search_result(self):
        """ Test the return value of the depth_first_search_method from the Graph class """
        D = dict()
        D['e'] = None
        D['f'] = 'e'
        D['c'] = 'f'
        D['d'] = 'c'
        self.assertEqual(type(self.__graph_2.depth_first_search('e')), type(D),
                             msg = "La méthode depth_first_search ne retourne pas " + \
                                   "un dictionnaire...")
        self.assertDictEqual(self.__graph_2.depth_first_search('e'), D,
                             msg = "La méthode depth_first_search, appliqué au graphe " + \
                                   "de Guido van Russo, en partant du point E " + \
                                   "ne retourne pas le bon dictionnaire")

    def test_5_of_the_depth_first_search_result(self):
        """ Test the return value of the depth_first_search_method from the Graph class """
        D = dict()
        D['a'] = None
        D['b'] = 'a'
        D['c'] = 'a'
        D['d'] = 'a'
        D['e'] = 'b'
        D['f'] = 'b'
        D['g'] = 'c'
        D['h'] = 'c'
        D['i'] = 'c'
        D['j'] = 'd'
        D['k'] = 'f'
        D['l'] = 'f'
        D['m'] = 'j'
        D['n'] = 'j'
        self.assertEqual(type(self.__graph_3.depth_first_search('a')), type(D),
                             msg = "La méthode depth_first_search ne retourne pas " + \
                                   "un dictionnaire...")
        self.assertDictEqual(self.__graph_3.depth_first_search('a'), D,
                             msg = "La méthode depth_first_search, appliqué à l'arbre " + \
                                   "de la section 4.2 du sujet, orienté de la racine " + \
                                   "vers ses feuilles, en partant de la racine " + \
                                   "ne retourne pas le bon dictionnaire")

    def test_6_of_the_depth_first_search_result(self):
        """ Test the return value of the depth_first_search_method from the Graph class """
        D = dict()
        D['b'] = None
        D['a'] = 'b'
        D['c'] = 'a'
        D['g'] = 'c'
        D['h'] = 'c'
        D['i'] = 'c'
        D['d'] = 'a'
        D['j'] = 'd'
        D['m'] = 'j'
        D['n'] = 'j'
        D['e'] = 'b'
        D['f'] = 'b'
        D['k'] = 'f'
        D['l'] = 'f'
        self.assertEqual(type(self.__graph_3.depth_first_search('b')), type(D),
                             msg = "La méthode depth_first_search ne retourne pas " + \
                                   "un dictionnaire...")
        self.assertDictEqual(self.__graph_3.depth_first_search('b'), D,
                             msg = "La méthode depth_first_search, appliqué à l'arbre " + \
                                   "de la section 4.2 du sujet, orienté de la racine " + \
                                   "vers ses feuilles, en partant du fils " + \
                                   "le plus à gauche de la racine ne retourne pas " + \
                                   "le bon dictionnaire")

    def test_7_of_the_depth_first_search_result(self):
        """ Test the return value of the depth_first_search_method from the Graph class """
        D = dict()
        D['g'] = None
        D['e'] = 'g'
        D['d'] = 'e'
        D['f'] = 'e'
        D['h'] = 'g'
        self.assertEqual(type(self.__graph_4.depth_first_search('g')), type(D),
                             msg = "La méthode depth_first_search ne retourne pas " + \
                                   "un dictionnaire...")
        self.assertDictEqual(self.__graph_4.depth_first_search('g'), D,
                             msg = "La méthode depth_first_search ne retourne pas " + \
                                   "le bon dictionnaire")

    def test_8_of_the_depth_first_search_result(self):
        """ Test the return value of the depth_first_search_method from the Graph class """
        D = dict()
        D['b'] = None
        D['a'] = 'b'
        D['c'] = 'a'
        D['d'] = 'c'
        D['e'] = 'b'
        D['f'] = 'e'
        D['g'] = 'f'
        D['h'] = 'g'
        self.assertEqual(type(self.__graph_4.depth_first_search('b')), type(D),
                             msg = "La méthode depth_first_search ne retourne pas " + \
                                   "un dictionnaire...")
        self.assertDictEqual(self.__graph_4.depth_first_search('b'), D,
                             msg = "La méthode depth_first_search ne retourne pas " + \
                                   "le bon dictionnaire")

    def test_the_presence_of_some_variables(self):
        source_code = ''.join(inspect.getsourcelines(Graph.depth_first_search)[0])
        self.assertIn('parents', source_code,
                      msg = "Il a été demandé d'utiliser une variable 'parents' pour " + \
                            "effectuer un parcours profondeur d'un graphe. Mais, je ne vois "+\
                            " pas cette variable...")
        self.assertIn('lifo', source_code,
                      msg = "Il a été demandé d'utiliser une variable 'lifo' pour " + \
                            "effectuer un parcours profondeur d'un graphe. Mais, je ne " + \
                            "vois  pas cette variable...")
        self.assertIn('colors', source_code,
                      msg = "Il a été demandé d'utiliser une variable 'colors' pour " + \
                            "effectuer un parcours profondeur d'un graphe. Mais, je ne " + \
                            "vois  pas cette variable...")
        self.assertIn('white', source_code,
                      msg = "Il a été demandé d'utiliser des couleurs lors " + \
                            "d'un parcours profondeur d'un graphe, à savoir 'white', " + \
                            "'grey' et 'black'. Mais, il y en a au moins une des trois " + \
                            "que je ne vois pas cette variable...")
        self.assertIn('grey', source_code,
                      msg = "Il a été demandé d'utiliser des couleurs lors " + \
                            "d'un parcours profondeur d'un graphe, à savoir 'white', " + \
                            "'grey' et 'black'. Mais, il y en a au moins une des trois " + \
                            "que je ne vois pas cette variable...")
        self.assertIn('black', source_code,
                      msg = "Il a été demandé d'utiliser des couleurs lors " + \
                            "d'un parcours profondeur d'un graphe, à savoir 'white', " + \
                            "'grey' et 'black'. Mais, il y en a au moins une des trois " + \
                            "que je ne vois pas cette variable...")

    def test_if_there_is_a_docstring(self):
        """ Check if there is a doc string, which is not a so trivial one... """
        self.assertNotEqual(Graph.depth_first_search.__doc__, '',
                            msg = "La méthode depth_first_search de la classe "+ \
                                  " Graph se devrait de possèder une docstring....")
        self.assertGreater(len(Graph.depth_first_search.__doc__.replace(' ', '')), 15,
                            msg = "Je doute que l'on puisse décrire une méthode " + \
                                  "dans une docstring en utilisant aussi peu de " + \
                                  "caractères...")

    def test_the_parameters(self):
        """ Check if the parameters of the depth_first_search method are correct """
        self.assertEqual(inspect.getargspec(Graph.depth_first_search)[0],
                         ['self', 'departure'],
                         msg = "La méthode depth_first_search ne possède pas " + \
                               "la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.depth_first_search)[1], None,
                         msg = "La méthode depth_first_search ne possède pas " + \
                               "la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.depth_first_search)[2], None,
                         msg = "La méthode depth_first_search ne possède pas  " + \
                               "la bonne signature...")
        self.assertEqual(inspect.getargspec(Graph.depth_first_search)[3], None,
                         msg = "La méthode depth_first_search ne possède pas  " + \
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
