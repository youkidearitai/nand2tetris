#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import code

class TestCode(unittest.TestCase):
    """
    Codeモジュールのテスト
    """

    def test_dest(self):
        c = code.Code()
        self.assertEqual(c.dest("M"),   0b001)
        self.assertEqual(c.dest("D"),   0b010)
        self.assertEqual(c.dest("MD"),  0b011)
        self.assertEqual(c.dest("A"),   0b100)
        self.assertEqual(c.dest("AM"),  0b101)
        self.assertEqual(c.dest("AD"),  0b110)
        self.assertEqual(c.dest("AMD"), 0b111)

    def test_comp(self):
        pass

    def test_jump(self):
        c = code.Code()
        self.assertEqual(c.jump("JGT"), 0b001)
        self.assertEqual(c.jump("JEQ"), 0b010)
        self.assertEqual(c.jump("JGE"), 0b011)
        self.assertEqual(c.jump("JLT"), 0b100)
        self.assertEqual(c.jump("JNE"), 0b101)
        self.assertEqual(c.jump("JLE"), 0b110)
        self.assertEqual(c.jump("JMP"), 0b111)

if __name__ == '__main__':
    unittest.main()

