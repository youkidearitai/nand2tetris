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
        c = code.Code()

        # a = 0
        self.assertEqual(c.comp("0"),   0b0101010)
        self.assertEqual(c.comp("1"),   0b0111111)
        self.assertEqual(c.comp("-1"),  0b0111010)
        self.assertEqual(c.comp("D"),   0b0001100)
        self.assertEqual(c.comp("A"),   0b0110000)
        self.assertEqual(c.comp("!D"),  0b0001101)
        self.assertEqual(c.comp("!A"),  0b0110001)
        self.assertEqual(c.comp("-D"),  0b0001111)
        self.assertEqual(c.comp("-A"),  0b0110011)
        self.assertEqual(c.comp("D+1"), 0b0011111)
        self.assertEqual(c.comp("A+1"), 0b0110111)
        self.assertEqual(c.comp("D-1"), 0b0001110)
        self.assertEqual(c.comp("A-1"), 0b0110010)
        self.assertEqual(c.comp("D+A"), 0b0000010)
        self.assertEqual(c.comp("D-A"), 0b0010011)
        self.assertEqual(c.comp("A-D"), 0b0000111)
        self.assertEqual(c.comp("D&A"), 0b0000000)
        self.assertEqual(c.comp("D|A"), 0b0010101)

        # a = 1
        self.assertEqual(c.comp("M"),   0b1110000)
        self.assertEqual(c.comp("!M"),  0b1110001)
        self.assertEqual(c.comp("-M"),  0b1110011)
        self.assertEqual(c.comp("M+1"), 0b1110111)
        self.assertEqual(c.comp("M-1"), 0b1110010)
        self.assertEqual(c.comp("D+M"), 0b1000010)
        self.assertEqual(c.comp("D-M"), 0b1010011)
        self.assertEqual(c.comp("M-D"), 0b1000111)
        self.assertEqual(c.comp("D&M"), 0b1000000)
        self.assertEqual(c.comp("D|M"), 0b1010101)

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

