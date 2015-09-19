#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SymbolTable:
    """SymbolTableモジュール

    Hack命令のシンボルを実際のアドレスに変換する
    """

    def __init__(self):
        """
        空のシンボルテーブルを作成する
        """
        pass

    def addEntity(self, symbol, address):
        """
        テーブルに(symbol,address)のペアを追加する

        Keyword arguments:
        symbol - 文字列
        address - 整数
        """
        pass

    def contains(self, symbol):
        """
        シンボルテーブルは与えられたsymbolを含むか

        Keyword arguments:
        symbol - 文字列
        """

        return True # 戻り値はブール

    def getAddress(self, symbol):
        """
        symbolに結び付けられたアドレスを返す

        Keyword arguments:
        symbol - 文字列r
        """

        return 0 # 戻り値は整数

