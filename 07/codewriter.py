#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    def __init__(self, stream):
        """
        出力ファイル・ストリームを開き書き込む準備を行う
        """
        self.stream = stream
        self.jmpAddr = 0
        segment = "constant"
        self.stream.write("@{0} // {0}(RAM[{0}])をDレジスタに一時退避\n".format(self.segment[segment]))
        self.stream.write("D=A\n")
        self.stream.write("@SP // スタックポインタを{0}に設定する\n".format(self.segment[segment]))
        self.stream.write("M=D // RAM[0]に{0}を入れる\n".format(self.segment[segment]))

    def setFileName(self, fileName):
        """
        CodeWriterモジュールに新しいVMファイルの変換が
        開始したことを知らせる
        """
        self.fileName = fileName.split(".")[0] + ".asm"

    def writeArithmetic(self, command):
        """
        与えられた算術コマンドをアセンブリコードに変換し、
        それを書き込む
        """

        # TODO:今現在はSimpleAddのみテストしよう
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
            self.stream.write("@{0}\n".format(self.segment[segment] + int(index)))
            self.stream.write("M=D\n")
        else: # constant
            ptr = "SP"
            self.stream.write("// pop {0} {1} コマンド\n".format(segment, index))
            self.stream.write("@SP // {0} スタックポインタをセットする\n".format(index))
            self.stream.write("D=M\n")
            self.stream.write("A=D\n")
            self.stream.write("D=M\n")
            self.stream.write("@{0}\n".format(index))
            self.stream.write("A=M+D // Aレジスタに{0} + {1}が入る\n".format(ptr, index))
            self.stream.write("A=A-D // Aレジスタに{0}が入る\n".format(index))
            self.stream.write("M=D // Mに入るのは {0} + {1}\n".format(ptr, index))
            self.stream.write("@SP\n")
            self.stream.write("M=M-1 // SPレジスタ(RAM[{0}])に1を追加してDレジスタに退避\n".format(self.segment[segment]))


    def writePushpop(self, c_command, segment, index):
        """
        C_PUSHまたはC_POPコマンドをアセンブリコードに変換し、
        それを書き込む
        """
        # TODO:現在のところは push constant nのみ
        if c_command == "push":
            if segment == "constant":
                self.writePushCommand(segment, index)
            elif segment == "local" or \
                    segment == "argument" or \
                    segment == "this" or \
                    segment == "that":
                self.writePushCommand(segment, index)
        elif c_command == "pop":
            if segment == "local" or \
                    segment == "argument" or \
                    segment == "this" or \
                    segment == "that":
                self.writePopCommand(segment, index)
            elif segment == "pointer" or segment == "temp":
                self.writePopCommand(segment, index)

    def close(self):
        """
        出力ファイルを閉じる
        """
        self.stream.close()

