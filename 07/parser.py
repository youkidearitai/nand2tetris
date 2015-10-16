#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

C_ARITHMETIC = 1
C_PUSH       = 2
C_POP        = 3
C_LABEL      = 4
C_GOTO       = 5
C_IF         = 6
C_FUNCTION   = 7
C_RETURN     = 8
C_CALL       = 9

class Parser:
    """Parserモジュール

    ひとつの.vmファイルに対してパースを行うとともに、入力コードの
    アクセスをカプセル化する。
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

        self.a_command_rex = re.compile('^\\@([_.$:a-zA-Z0-9]+)')
        self.c_command_rex = re.compile(
            '^(([AMD]{1,3})=)?([-!]?[AMD01])([-+&|])?([01AMD])?(;)?(J[GELNM][TQETP])?$'
        )
        self.l_comand_rex = re.compile('^\(([_.$:a-zA-Z0-9]+)\)$')
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

    def arg1(self):
        """
        現コマンドの最初の引数が返される。
        """

        return ""

    def arg2(self):
        """
        現コマンドの2番めの引数が返される
        現コマンドがC_PUSH C_POP C_FUNCTION, C_CALLの
        場合のみ本ルーチンを呼ぶようにする
        """

        return ""

class NotCommandErrorException(Exception):
    pass

