#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import symboltable

class TestSymbolTable(unittest.TestCase):
    """
    SymbolTableモジュールのテスト
    """

    def setUp(self):
        self.symboltable = symboltable.SymbolTable()

    def test_symbol(self):
        self.symboltable.addEntity("hoge", 1)
        self.assertTrue(self.symboltable.contains("hoge"))
        self.assertEqual(self.symboltable.getAddress("hoge"), 1)

        self.symboltable.addEntity("huga", 2)
        self.assertTrue(self.symboltable.contains("huga"))
        self.assertEqual(self.symboltable.getAddress("huga"), 2)

        self.assertFalse(self.symboltable.contains("hello"))

        self.assertTrue(self.symboltable.contains("SP"))

        self.assertTrue(self.symboltable.contains("R10"))
        self.assertEqual(self.symboltable.getAddress("R10"), 0x000a)

if __name__ == '__main__':
    unittest.main()

