#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Code:
    """Codeモジュール

    Hackのアセンブリ言語のニーモニックをバイナリコードへ変換する
    """

    def dest(self, mnemonic):
        """
        destニーモニックのバイナリコードを返す

        Keyword arguments:
        mnemonic - ニーモニック(文字列)
        """
        binary = 0b000

        if mnemonic is None:
            return binary

        if 'M' in mnemonic:
            binary = binary + 0b001

        if 'D' in mnemonic:
            binary = binary + 0b010

        if 'A' in mnemonic:
            binary = binary + 0b100

        return binary

    def comp(self, mnemonic):
        """
        compニーモニックのバイナリコードを返す

        Keyword arguments:
        mnemonic - ニーモニック(文字列)
        """
        pass

    def jump(self):
        """
        jumpニーモニックのバイナリコードを返す

        Keyword arguments:
        mnemonic - ニーモニック(文字列)
        """
        pass

