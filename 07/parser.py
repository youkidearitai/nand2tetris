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
        self.delete_rex = re.compile('(?://.*)')

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
        self.nowline = self.stream.readline().strip()
        nowline = self.delete_rex.sub("", self.nowline)
        self.commands = nowline.split(" ")

    def commandType(self):
        """
        現コマンドの種類を返す
        Return value:
        C_(ARITHMETIC|PUSH|POP)
        """

        if self.commands[0] == "push":
            self.command_type = C_PUSH
        elif self.commands[0] == "pop":
            self.command_type = C_POP
        elif self.commands[0] == "add":
            self.command_type = C_ARITHMETIC
        elif self.commands[0] == "sub":
            self.command_type = C_ARITHMETIC
        elif self.commands[0] == "neg":
            self.command_type = C_ARITHMETIC
        elif self.commands[0] == "eq":
            self.command_type = C_ARITHMETIC
        elif self.commands[0] == "and":
            self.command_type = C_ARITHMETIC
        elif self.commands[0] == "or":
            self.command_type = C_ARITHMETIC
        else:
            raise NotCommandErrorException("no command", self.commands[0])

        return self.command_type

    def arg1(self):
        """
        現コマンドの最初の引数が返される。
        """
        if self.command_type == C_ARITHMETIC:
            return self.commands[0]

        return self.commands[1]

    def arg2(self):
        """
        現コマンドの2番めの引数が返される
        現コマンドがC_PUSH C_POP C_FUNCTION, C_CALLの
        場合のみ本ルーチンを呼ぶようにする
        """

        return self.commands[2]

class NotCommandErrorException(Exception):
    pass

