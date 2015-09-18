#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Parser:
    """Parserモジュール

    各アセンブリコマンドをその基本要素（フィールドとシンボル）に分解する
    """
    def __init__(self, stream):
        """入力ファイル/ストリームを開きパースを行う準備をする

        Keyword arguments:
        stream -- 入力ファイル/ストリーム

        Return value:
        インスタンス
        """
        pass

    def hasMoreCommands(self):
        """
        入力にまだコマンドが存在するか？

        Return value:
        bool -- 入力にまだコマンドが存在するか
        """
        pass

    def advance(self):
        """
        入力から次のコマンドを読み、それを現在のコマンドにする。
        このルーチンはhasMoreCommands()がtrueの場合のみ
        呼ぶようにする。最初は現コマンドは空である。
        """
        pass

    def commandType(self):
        """
        現コマンドの種類を返す
        - A_COMMANDは@Xxxを意味し、Xxxはシンボルか10進数の数値である。
        - C_COMMANDはdest=comp;jumpを意味する。
        - L_COMMANDは擬似コマンドであり、(Xxx)をいみする。Xxxはシンボルである。

        Return value:
        [ACL]_COMMAND
        """
        pass

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
