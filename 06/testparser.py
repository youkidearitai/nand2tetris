#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import parser

class TestParser(unittest.TestCase):
    """
    Parserモジュールのテスト
    """

    def setUp(self):
        self.parser = parser.Parser(open('test.asm', 'r'))

    def test_hasMoreCommands(self):
        a = self.parser.hasMoreCommands()
        self.assertTrue(a)

    def test_advance(self):
        pass

    def test_commandType(self):
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), parser.C_COMMAND)
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), parser.C_COMMAND)
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), parser.A_COMMAND)
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), parser.L_COMMAND)

    def test_symbol(self):
        pass

    def test_dest(self):
        pass

    def test_comp(self):
        pass

    def test_jump(self):
        pass

if __name__ == '__main__':
    unittest.main()

