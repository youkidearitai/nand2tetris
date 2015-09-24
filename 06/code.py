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
        if "M" in mnemonic:
            if mnemonic == "M":
                return 0b1110000

            if mnemonic == "!M":
                return 0b1110001

            if mnemonic == "-M":
                return 0b1110011

            if mnemonic == "M+1":
                return 0b1110111

            if mnemonic == "M-1":
                return 0b1110010

            if mnemonic == "D+M":
                return 0b1000010

            if mnemonic == "D-M":
                return 0b1010011

            if mnemonic == "M-D":
                return 0b1000111

            if mnemonic == "D&M":
                return 0b1000000

            if mnemonic == "D|M":
                return 0b1010101

        else:
            if mnemonic == '0':
                return 0b0101010

            if mnemonic == '1':
                return 0b0111111

            if mnemonic == "-1":
                return 0b0111010

            if mnemonic == "D":
                return 0b0001100

            if mnemonic == "A":
                return 0b0110000

            if mnemonic == "!D":
                return 0b0001101

            if mnemonic == "!A":
                return 0b0110001

            if mnemonic == "-D":
                return 0b0001111

            if mnemonic == "-A":
                return 0b0110011

            if mnemonic == "D+1":
                return 0b0011111

            if mnemonic == "A+1":
                return 0b0110111

            if mnemonic == "D-1":
                return 0b0001110

            if mnemonic == "A-1":
                return 0b0110010

            if mnemonic == "D+A":
                return 0b0000010

            if mnemonic == "D-A":
                return 0b0010011

            if mnemonic == "A-D":
                return 0b0000111

            if mnemonic == "D&A":
                return 0b0000000

            if mnemonic == "D|A":
                return 0b0010101


    def jump(self, mnemonic):
        """
        jumpニーモニックのバイナリコードを返す

        Keyword arguments:
        mnemonic - ニーモニック(文字列)
        """
        binary = 0b000

        if mnemonic is None:
            return binary

        if mnemonic == "JMP":
            return 0b111

        if "JG" in mnemonic:
            binary = binary + 0b001

        if "JL" in mnemonic:
            binary = binary + 0b100

        if "E" in mnemonic:
            if mnemonic == "JNE":
                return 0b101

            binary = binary + 0b010

        return binary

