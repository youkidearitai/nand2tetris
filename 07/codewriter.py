#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CodeWriter:
    """
    CodeWriterモジュール
    vmコマンドをHackアセンブリコードに変換する
    """

    def __init__(self, stream):
        """
        出力ファイル・ストリームを開き書き込む準備を行う
        """
        pass

    def setFileName(self, fileName):
        """
        CodeWriterモジュールに新しいVMファイルの変換が
        開始したことを知らせる
        """
        pass

    def writeArithmetic(self, command):
        """
        与えられた算術コマンドをアセンブリコードに変換し、
        それを書き込む
        """
        pass

    def writePushpop(self, c_command):
        """
        C_PUSHまたはC_POPコマンドをアセンブリコードに変換し、
        それを書き込む
        """
        pass

    def close(self):
        """
        出力ファイルを閉じる
        """
        pass

