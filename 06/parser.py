#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

A_COMMAND = 1
C_COMMAND = 2
L_COMMAND = 3

class Parser:
    """Parserモジュール

    各アセンブリコマンドをその基本要素（フィールドとシンボル）に分解する
    """

    stream = None

    nowline = '\n'

    def __init__(self, stream):
        """入力ファイル/ストリームを開きパースを行う準備をする

        Keyword arguments:
        stream -- 入力ファイル/ストリーム

        Return value:
        インスタンス
        """
        self.stream = stream

    def hasMoreCommands(self):
        """
        入力にまだコマンドが存在するか？

        Return value:
        bool -- 入力にまだコマンドが存在するか
        """
        return self.nowline != '' # 空文字列だともうない。空行の場合は\nが入るため

    def advance(self):
        """
        入力から次のコマンドを読み、それを現在のコマンドにする。
        このルーチンはhasMoreCommands()がtrueの場合のみ
        呼ぶようにする。最初は現コマンドは空である。
        """
        self.nowline = self.stream.readline().strip(' ')
        return self.nowline

    def commandType(self):
        """
        現コマンドの種類を返す
        - A_COMMANDは@Xxxを意味し、Xxxはシンボルか10進数の数値である。
        - C_COMMANDはdest=comp;jumpを意味する。
        - L_COMMANDは擬似コマンドであり、(Xxx)をいみする。Xxxはシンボルである。

        Return value:
        [ACL]_COMMAND
        """
        symbol = re.search('^\\@[a-zA-Z0-9]+', self.nowline)
        if symbol is not None:
            return A_COMMAND

        c_command = re.search(
            '^(([AMD]{1,3})=)?([-!]?[AMD])([-+&|])?([01AMD])?(;J[GELNM][TQETP])?$',
            self.nowline
        )
        if c_command is not None:
            return C_COMMAND

        l_command = re.search('^\([a-zA-Z0-9]+\)$', self.nowline)
        if l_command is not None:
            return L_COMMAND

        raise NotCommandErrorException(self.nowline)

    def symbol(self):
        """
        現コマンド@Xxxまたは(Xxx)のXxxを返す。
        Xxxはシンボルまたは10進数の数値である。
        このルーチンはcommandType()がA_COMMANDまたは
        C_COMMANDの時だけ呼ぶようにする

        Return value:
        string
        """
        pass

    def dest(self):
        """
        現C命令のdestニーモニックを返す
        (候補として8つの可能性がある)。
        このルーチンはcommandType()がC_COMMANDのときだけ
        呼ぶようにする。
        """
        pass

    def comp(self):
        """
        現C命令のcompニーモニックを返す
        (候補として8つの可能性がある)。
        このルーチンはcommandType()がC_COMMANDのときだけ
        呼ぶようにする。
        """
        pass

    def jump(self):
        """
        現C命令のjumpニーモニックを返す
        (候補として8つの可能性がある)。
        このルーチンはcommandType()がC_COMMANDのときだけ
        呼ぶようにする。
        """
        pass

class NotCommandErrorException(Exception):
    pass

