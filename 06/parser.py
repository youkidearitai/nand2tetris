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

    # 入力ストリーム
    stream = None

    # コマンドの種類
    command_type = None

    # 現在の行
    nowline = '\n'

    # A_COMMANDの正規表現
    a_command_rex = None

    # C_COMMANDの正規表現
    c_command_rex = None

    # L_COMMANDの正規表現
    l_comand_rex = None

    # 無視する文字列の正規表現
    delete_rex = None

    def __init__(self, stream):
        """入力ファイル/ストリームを開きパースを行う準備をする

        Keyword arguments:
        stream -- 入力ファイル/ストリーム

        Return value:
        インスタンス
        """
        self.stream = stream

        self.a_command_rex = re.compile('^\\@([a-zA-Z0-9]+)')
        self.c_command_rex = re.compile(
            '^(([AMD]{1,3})=)?([-!]?[AMD01])([-+&|])?([01AMD])?(;)?(J[GELNM][TQETP])?$'
        )
        self.l_comand_rex = re.compile('^\(([a-zA-Z0-9]+)\)$')
        self.delete_rex = re.compile('(?://.*| )')

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
        self.nowline = self.delete_rex.sub("", self.stream.readline())
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
        self.command_type = self.a_command_rex.match(self.nowline)
        if self.command_type is not None:
            return A_COMMAND

        self.command_type = self.c_command_rex.match(self.nowline)
        if self.command_type is not None:
            return C_COMMAND

        self.command_type = self.l_comand_rex.match(self.nowline)
        if self.command_type is not None:
            return L_COMMAND

    def symbol(self):
        """
        現コマンド@Xxxまたは(Xxx)のXxxを返す。
        Xxxはシンボルまたは10進数の数値である。
        このルーチンはcommandType()がA_COMMANDまたは
        L_COMMANDの時だけ呼ぶようにする

        Return value:
        string
        """
        return self.command_type.group(1)

    def dest(self):
        """
        現C命令のdestニーモニックを返す
        (候補として8つの可能性がある)。
        このルーチンはcommandType()がC_COMMANDのときだけ
        呼ぶようにする。
        """
        dest = self.command_type.group(2)
        if dest is None:
            return ''

        return dest

    def comp(self):
        """
        現C命令のcompニーモニックを返す
        (候補として8つの可能性がある)。
        このルーチンはcommandType()がC_COMMANDのときだけ
        呼ぶようにする。
        """

        left_var = self.command_type.group(3)
        if left_var is None:
            left_var = ''

        ctr_var = self.command_type.group(4)
        if ctr_var is None:
            ctr_var = ''

        rght_var = self.command_type.group(5)
        if rght_var is None:
            rght_var = ''

        return left_var + ctr_var + rght_var

    def jump(self):
        """
        現C命令のjumpニーモニックを返す
        (候補として8つの可能性がある)。
        このルーチンはcommandType()がC_COMMANDのときだけ
        呼ぶようにする。
        """
        jump = self.command_type.group(7)

        if jump is None:
            return ''

        return jump

class NotCommandErrorException(Exception):
    pass

