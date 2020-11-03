#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import asm_parser

class TestParser(unittest.TestCase):
    """
    Parserモジュールのテスト
    """

    def setUp(self):
        self.parser = asm_parser.Parser(open('test.asm', 'r'))

    def test_hasMoreCommands(self):
        self.parser = asm_parser.Parser(open('test.asm', 'r'))
        a = self.parser.hasMoreCommands()
        self.assertTrue(a)

    def test_advance(self):
        self.parser = asm_parser.Parser(open('test.asm', 'r'))
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), asm_parser.C_COMMAND)

    def test_commandType(self):
        self.parser = asm_parser.Parser(open('test.asm', 'r'))
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), asm_parser.C_COMMAND)
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), asm_parser.C_COMMAND)
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), asm_parser.A_COMMAND)
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), asm_parser.L_COMMAND)

    def test_mnmonic(self):
        self.parser = asm_parser.Parser(open('test.asm', 'r'))

        self.parser.advance()
        self.parser.commandType()
        self.assertEqual(self.parser.dest(), "D")
        self.assertEqual(self.parser.comp(), "M")
        self.assertEqual(self.parser.jump(), "")

        self.parser.advance()
        self.parser.commandType()
        self.assertEqual(self.parser.dest(), "A")
        self.assertEqual(self.parser.comp(), "M+1")
        self.assertEqual(self.parser.jump(), "")

        self.parser.advance()
        self.parser.commandType()
        self.assertEqual(self.parser.symbol(), "hoge")

        self.parser.advance()
        self.parser.commandType()
        self.assertEqual(self.parser.symbol(), "LOOP")

        self.parser.advance()
        self.parser.commandType()
        self.assertEqual(self.parser.dest(), "")
        self.assertEqual(self.parser.comp(), "0")
        self.assertEqual(self.parser.jump(), "JGT")

if __name__ == '__main__':
    unittest.main()

