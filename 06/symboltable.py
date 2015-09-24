#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SymbolTable:
    """SymbolTableモジュール

    Hack命令のシンボルを実際のアドレスに変換する
    """

    # シンボルとアドレスのペア
    symbol_address = None

    def __init__(self):
        """
        空のシンボルテーブルを作成する
        """
        self.symbol_address = {
            "SP":     0x0000,
            "LCL":    0x0001,
            "ARG":    0x0002,
            "THIS":   0x0003,
            "THAT":   0x0004,
            "R0":     0x0000,
            "R1":     0x0001,
            "R2":     0x0002,
            "R3":     0x0003,
            "R4":     0x0004,
            "R5":     0x0005,
            "R6":     0x0006,
            "R7":     0x0007,
            "R8":     0x0008,
            "R9":     0x0009,
            "R10":    0x000a,
            "R11":    0x000b,
            "R12":    0x000c,
            "R13":    0x000d,
            "R14":    0x000e,
            "R15":    0x000f,
            "SCREEN": 0x4000,
            "KBD":    0x6000
        }

    def addEntity(self, symbol, address):
        """
        テーブルに(symbol,address)のペアを追加する

        Keyword arguments:
        symbol - 文字列
        address - 整数
        """
        self.symbol_address[symbol] = address

    def contains(self, symbol):
        """
        シンボルテーブルは与えられたsymbolを含むか

        Keyword arguments:
        symbol - 文字列
        """

        return symbol in self.symbol_address # 戻り値はブール

    def getAddress(self, symbol):
        """
        symbolに結び付けられたアドレスを返す

        Keyword arguments:
        symbol - 文字列r
        """

        return self.symbol_address[symbol] # 戻り値は整数

