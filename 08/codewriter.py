#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class CodeWriter:
    """
    CodeWriterモジュール
    vmコマンドをHackアセンブリコードに変換する
    """

    # 出力ファイル名
    fileName = None

    # 入力ストリーム
    stream = None

    # Parserモジュール
    parser = None

    # セグメント RAM内のベースアドレス
    segment = {
        "local": 1,
        "argument": 2,
        "this": 3,
        "that": 4,
        "pointer": 3,    # this, that
        "temp": 5,       # R5 to R12
        "constant": 256, # 単純な定数値
        "static": 16     # アセンブリ内で新しいシンボルに出くわした場合の新しいRAMアドレス
    }

    segmentPtr = {
        "local": "LCL",
        "argument": "ARG",
        "this": "THIS",
        "that": "THAT"
    }

    # ジャンプアドレス
    jmpAddr = 0

    labelNum = 0

    def __init__(self, stream):
        """
        出力ファイル・ストリームを開き書き込む準備を行う
        """
        self.stream = stream
        self.jmpAddr = 0

    def setFileName(self, fileName):
        """
        CodeWriterモジュールに新しいVMファイルの変換が
        開始したことを知らせる
        """
        self.fileName = fileName.split(".")[0]

    def writeArithmetic(self, command):
        """
        与えられた算術コマンドをアセンブリコードに変換し、
        それを書き込む
        """

        if command == "add":
            self.stream.write("// addコマンド\n")
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("M=M-1\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("M=M+D // RAM[SP] + RAM[SP-1]\n")

        if command == "sub":
            self.stream.write("// subコマンド\n")
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("M=M-1\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("M=M-D // RAM[SP] - RAM[SP-1]\n")

        if command == "neg":
            self.stream.write("// negコマンド\n")
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("M=-M // RAM[SP] - RAM[SP-1]\n")

        if command == "eq":
            self.stream.write("// eqコマンド\n")
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("M=M-1\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("D=M-D // RAM[SP] - RAM[SP-1]\n")
            self.stream.write("@GTHAN_EQ{0} // RAM[SP] - RAM[SP-1]\n".format(self.jmpAddr))
            self.stream.write("D;JEQ // RAM[SP] - RAM[SP-1]\n")
            self.stream.write("@SP\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D-1\n")
            self.stream.write("M=0\n")
            self.stream.write("@GTHAN_EQ_END{0}\n".format(self.jmpAddr))
            self.stream.write("0;JMP\n")
            self.stream.write("(GTHAN_EQ{0})\n".format(self.jmpAddr))
            self.stream.write("  @SP\n")
            self.stream.write("  D=M\n")
            self.stream.write("  A=D-1\n")
            self.stream.write("  M=-1\n")
            self.stream.write("(GTHAN_EQ_END{0})\n".format(self.jmpAddr))
            self.jmpAddr = self.jmpAddr + 1

        if command == "gt":
            self.stream.write("// gtコマンド\n")
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("M=M-1\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("D=M-D // RAM[SP] - RAM[SP-1]\n")
            self.stream.write("@GTHAN_EQ{0} // RAM[SP] - RAM[SP-1]\n".format(self.jmpAddr))
            self.stream.write("D;JGT // RAM[SP] - RAM[SP-1]\n")
            self.stream.write("@SP\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D-1\n")
            self.stream.write("M=0\n")
            self.stream.write("@GTHAN_EQ_END{0}\n".format(self.jmpAddr))
            self.stream.write("0;JMP\n")
            self.stream.write("(GTHAN_EQ{0})\n".format(self.jmpAddr))
            self.stream.write("  @SP\n")
            self.stream.write("  D=M\n")
            self.stream.write("  A=D-1\n")
            self.stream.write("  M=-1\n")
            self.stream.write("(GTHAN_EQ_END{0})\n".format(self.jmpAddr))
            self.jmpAddr = self.jmpAddr + 1

        if command == "lt":
            self.stream.write("// ltコマンド\n")
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("M=M-1\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("D=M-D // RAM[SP] - RAM[SP-1]\n")
            self.stream.write("@GTHAN_EQ{0} // RAM[SP] - RAM[SP-1]\n".format(self.jmpAddr))
            self.stream.write("D;JLT // RAM[SP] - RAM[SP-1]\n")
            self.stream.write("@SP\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D-1\n")
            self.stream.write("M=0\n")
            self.stream.write("@GTHAN_EQ_END{0}\n".format(self.jmpAddr))
            self.stream.write("0;JMP\n")
            self.stream.write("(GTHAN_EQ{0})\n".format(self.jmpAddr))
            self.stream.write("  @SP\n")
            self.stream.write("  D=M\n")
            self.stream.write("  A=D-1\n")
            self.stream.write("  M=-1\n")
            self.stream.write("(GTHAN_EQ_END{0})\n".format(self.jmpAddr))
            self.jmpAddr = self.jmpAddr + 1

        if command == "and":
            self.stream.write("// andコマンド\n")
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("M=M-1\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("M=M&D // RAM[SP] & RAM[SP-1]\n")

        if command == "or":
            self.stream.write("// orコマンド\n")
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("M=M-1\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("M=M|D // RAM[SP] | RAM[SP-1]\n")

        if command == "not":
            self.stream.write("// notコマンド\n")
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("M=!M // RAM[SP] ! RAM[SP-1]\n")

    def writePushCommand(self, segment, index):
        """
        アセンブリ言語に書き換えるためのメソッド
        共通ならばここに書いてしまおう
        """
        if segment == "local":
            ptr = "LCL"
        elif segment == "argument":
            ptr = "ARG"
        elif segment == "this":
            ptr = "THIS"
        elif segment == "that":
            ptr = "THAT"
        elif segment == "pointer":
            pass # 3 + i
        elif segment == "temp":
            pass # 5 + i

        if segment == "local" or segment == "argument" or segment == "this" or segment == "that":
            self.stream.write("// push {0} {1} コマンド\n".format(segment, index))
            self.stream.write("@{0}\n".format(ptr))
            self.stream.write("A=M\n")
            for i in range(int(index)):
                self.stream.write("A=A+1\n")
            self.stream.write("D=M\n")
            self.stream.write("@SP\n")
            self.stream.write("A=M\n")
            self.stream.write("M=D\n")
            self.stream.write("@SP\n")
            self.stream.write("M=M+1\n")
        elif segment == "pointer" or segment == "temp":
            self.stream.write("// push {0} {1} コマンド\n".format(segment, index))
            self.stream.write("@{0}\n".format(int(index) + self.segment[segment]))
            self.stream.write("D=M\n")
            self.stream.write("@SP\n")
            self.stream.write("A=M\n")
            self.stream.write("M=D\n")
            self.stream.write("@SP\n")
            self.stream.write("M=M+1\n")
        elif segment == "static":
            self.stream.write("// push {0} {1} コマンド\n".format(segment, index))
            self.stream.write("@{0}.{1}\n".format(self.fileName, index))
            self.stream.write("D=M\n")
            self.stream.write("@SP\n")
            self.stream.write("A=M\n")
            self.stream.write("M=D\n")
            self.stream.write("@SP\n")
            self.stream.write("M=M+1\n")
        else: # constant
            ptr = "SP"
            self.stream.write("// push {0} {1} コマンド\n".format(segment, index))
            self.stream.write("@{0} // {0}をpushする\n".format(index))
            self.stream.write("D=A\n")
            self.stream.write("@{0}\n".format(ptr))
            self.stream.write("A=M // アドレスを{0}に設定する\n".format(self.segment[segment]))
            self.stream.write("M=D // RAM[{0}]に{1} {2}が入る\n".format(self.segment[segment], segment, index))
            self.stream.write("@SP\n")
            self.stream.write("M=M+1 // SPレジスタ(RAM[{0}])に1を追加してDレジスタに退避\n".format(self.segment[segment]))

    def writePopCommand(self, segment, index):
        if segment in self.segmentPtr.keys():
            ptr = self.segmentPtr[segment]
            self.stream.write("// pop {0} {1} コマンド\n".format(segment, index))
            self.stream.write("@{0}\n".format(index))
            self.stream.write("D=A\n")
            self.stream.write("@{0}\n".format(ptr))
            self.stream.write("M=D+M\n")
            self.stream.write("@{0}\n".format(index))
            self.stream.write("@SP // {0} スタックポインタをセットする\n".format(index))
            self.stream.write("M=M-1\n")
            self.stream.write("A=M\n")
            self.stream.write("D=M\n")
            self.stream.write("@{0}\n".format(ptr))
            self.stream.write("A=M\n")
            self.stream.write("M=D\n")
            self.stream.write("@{0}\n".format(index))
            self.stream.write("D=A\n")
            self.stream.write("@{0}\n".format(ptr))
            self.stream.write("M=M-D\n")
        elif segment == "pointer" or segment == "temp": # pointer or tempセグメント
            self.stream.write("// pop {0} {1} コマンド\n".format(segment, index))
            self.stream.write("@SP\n")
            self.stream.write("M=M-1\n")
            self.stream.write("A=M\n")
            self.stream.write("D=M\n")
            self.stream.write("@{0}\n".format(self.segment[segment] + int(index)))
            self.stream.write("M=D\n")
        elif segment == "static": # staticセグメント
            self.stream.write("// pop {0} {1} コマンド\n".format(segment, index))
            self.stream.write("@SP\n")
            self.stream.write("M=M-1\n")
            self.stream.write("A=M\n")
            self.stream.write("D=M\n")
            self.stream.write("@{0}.{1}\n".format(self.fileName, index))
            self.stream.write("M=D\n")
        else: # global
            ptr = "SP"
            self.stream.write("// pop {0} コマンド\n".format(segment))
            self.stream.write("@SP // {0} スタックポインタをセットする\n".format(segment))
            self.stream.write("M=M-1\n")
            self.stream.write("A=M\n")
            self.stream.write("D=M\n")

    def writePushpop(self, c_command, segment, index):
        """
        C_PUSHまたはC_POPコマンドをアセンブリコードに変換し、
        それを書き込む
        """
        if c_command == "push":
            if segment == "constant" or \
               segment == "local" or \
               segment == "argument" or \
               segment == "this" or \
               segment == "that" or \
               segment == "pointer" or \
               segment == "temp" or \
               segment == "static":
                self.writePushCommand(segment, index)
            else:
                raise UndefinedSymbolException("Undefined push symbol: {}".format(segment))
        elif c_command == "pop":
            if segment == "global" or \
                    segment == "local" or \
                    segment == "argument" or \
                    segment == "this" or \
                    segment == "that" or \
                    segment == "pointer" or \
                    segment == "temp" or \
                    segment == "static":
                self.writePopCommand(segment, index)
            else:
                raise UndefinedSymbolException("Undefined pop symbol: {}".format(segment))
        else:
            raise UndefinedCommandException("Undefined command: {}".format(c_command))

    def writeInit(self):
        """
        VMの初期化を行うアセンブリコードを書く
        (ブートストラップ)
        """
        self.stream.write("// writeInit コマンド\n")
        self.stream.write("@256\n")
        self.stream.write("D=A\n")
        self.stream.write("@SP\n")
        self.stream.write("M=D\n")
        self.writeCall("Sys.init", 0)

    def writeFunction(self, f, k):
        """
        k個のローカル変数を持つ関数fを宣言する
        """
        self.stream.write("// writeFunction {0} {1} コマンド\n".format(f, k))
        self.stream.write("({0})\n".format(f))

        for i in range(int(k)):
            self.stream.write("@SP\n")
            self.stream.write("A=M\n")
            self.stream.write("M=D\n")
            self.stream.write("@SP\n")
            self.stream.write("M=M+1\n")

    def getNewCallLabel(self, f):
        self.labelNum += 1
        return "_CALL_{0}{1}".format(f, self.labelNum)

    def writeCall(self, f, n):
        """
        n個の引数がスタックにプッシュされた後に
        関数fが呼ばれる
        """
        return_address_label = self.getNewCallLabel(f)
        self.stream.write("// writeCall {0} {1} コマンド\n".format(f, n))
        self.stream.write("// push return-address コマンド\n")
        self.stream.write("@{0}\n".format(return_address_label))
        self.stream.write("D=A\n")
        self.stream.write("@SP\n")
        self.stream.write("A=M\n")
        self.stream.write("M=D\n")
        self.stream.write("@SP\n")
        self.stream.write("M=M+1\n")
        self.stream.write("// push LCL コマンド\n")
        self.stream.write("@LCL\n")
        self.stream.write("D=M\n")
        self.stream.write("@SP\n")
        self.stream.write("A=M\n")
        self.stream.write("M=D\n")
        self.stream.write("@SP\n")
        self.stream.write("M=M+1\n")
        self.stream.write("// push ARG コマンド\n")
        self.stream.write("@ARG\n")
        self.stream.write("D=M\n")
        self.stream.write("@SP\n")
        self.stream.write("A=M\n")
        self.stream.write("M=D\n")
        self.stream.write("@SP\n")
        self.stream.write("M=M+1\n")
        self.stream.write("// push THIS コマンド\n")
        self.stream.write("@THIS\n")
        self.stream.write("D=M\n")
        self.stream.write("@SP\n")
        self.stream.write("A=M\n")
        self.stream.write("M=D\n")
        self.stream.write("@SP\n")
        self.stream.write("M=M+1\n")
        self.stream.write("// push THAT コマンド\n")
        self.stream.write("@THAT\n")
        self.stream.write("D=M\n")
        self.stream.write("@SP\n")
        self.stream.write("A=M\n")
        self.stream.write("M=D\n")
        self.stream.write("@SP\n")
        self.stream.write("M=M+1\n")
        self.stream.write("// ARG = SP - n - 5\n")
        self.stream.write("@SP\n")
        self.stream.write("D=M\n")
        self.stream.write("@5\n")
        self.stream.write("D=D-A\n")
        self.stream.write("@{0}\n".format(n))
        self.stream.write("D=D-A\n")
        self.stream.write("@ARG\n")
        self.stream.write("M=D\n")
        self.stream.write("// LCL = SP\n")
        self.stream.write("@SP\n")
        self.stream.write("D=M\n")
        self.stream.write("@LCL\n")
        self.stream.write("M=D\n")
        self.stream.write("// goto {0}\n".format(f))
        self.stream.write("@{0}\n".format(f))
        self.stream.write("0;JMP\n")
        self.stream.write("({0})\n".format(return_address_label))

    def writeReturn(self):
        """
        関数からのリターン
        """
        self.stream.write("// writeReturn コマンド\n")
        self.stream.write("// FRAME = LCL FRAME = R13\n")
        self.stream.write("@LCL\n")
        self.stream.write("D=M\n")
        self.stream.write("@R13\n")
        self.stream.write("M=D\n")
        self.stream.write("// RET = *(FRAME - 5)\n")
        self.stream.write("@5\n")
        self.stream.write("D=A\n")
        self.stream.write("@R13\n")
        self.stream.write("A=M-D\n")
        self.stream.write("D=M\n")
        self.stream.write("@R14\n")
        self.stream.write("M=D\n")

        self.stream.write("// *ARG = pop()\n")
        self.stream.write("@SP\n")
        self.stream.write("M=M-1\n")
        self.stream.write("A=M\n")

        self.stream.write("D=M\n")
        self.stream.write("@ARG\n")
        self.stream.write("A=M\n")
        self.stream.write("M=D\n")

        self.stream.write("// SP = ARG+1\n")
        self.stream.write("@ARG\n")
        self.stream.write("D=M+1\n")
        self.stream.write("@SP\n")
        self.stream.write("M=D\n")

        self.stream.write("// THAT = *(FRAME - 1)\n")
        self.stream.write("@R13\n")
        self.stream.write("AM=M-1\n")
        self.stream.write("D=M\n")
        self.stream.write("@THAT\n")
        self.stream.write("M=D\n")

        self.stream.write("// THIS = *(FRAME - 2)\n")
        self.stream.write("@R13\n")
        self.stream.write("AM=M-1\n")
        self.stream.write("D=M\n")
        self.stream.write("@THIS\n")
        self.stream.write("M=D\n")

        self.stream.write("// ARG = *(FRAME - 3)\n")
        self.stream.write("@R13\n")
        self.stream.write("AM=M-1\n")
        self.stream.write("D=M\n")
        self.stream.write("@ARG\n")
        self.stream.write("M=D\n")

        self.stream.write("// LCL = *(FRAME - 4)\n")
        self.stream.write("@R13\n")
        self.stream.write("AM=M-1\n")
        self.stream.write("D=M\n")
        self.stream.write("@LCL\n")
        self.stream.write("M=D\n")

        self.stream.write("// goto RET\n")
        self.stream.write("@R14\n")
        self.stream.write("A=M\n")
        self.stream.write("0;JMP\n")

    def writeLabel(self, label):
        """
        labelコマンドを行うアセンブリコード
        """
        self.stream.write("// label {0} コマンド\n".format(label))
        self.stream.write("({0}${1})\n".format(self.fileName, label))

    def writeGoto(self, label):
        """
        gotoコマンドを行うアセンブリコード
        """
        self.stream.write("// goto {0} コマンド\n".format(label))
        self.stream.write("@{0}${1}\n".format(self.fileName, label))
        self.stream.write("0;JMP\n")

    def writeIf(self, label):
        """
        if-goto コマンドを行うアセンブリコード
        """
        self.stream.write("// if-goto {0} コマンド\n".format(label))
        self.writePushpop("pop", "global", None)
        self.stream.write("@{0}${1}\n".format(self.fileName, label))
        self.stream.write("D;JNE\n")

    def close(self):
        """
        出力ファイルを閉じる
        """
        self.stream.close()

class UndefinedCommandException(Exception):
    pass

class UndefinedSymbolException(Exception):
    pass
