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

    def __init__(self, stream):
        """
        出力ファイル・ストリームを開き書き込む準備を行う
        """
        self.stream = stream
        segment = "constant"
        self.stream.write("@{0} // {0}(RAM[{0}])をDレジスタに一時退避\n".format(self.segment[segment]))
        self.stream.write("D=A\n")
        self.stream.write("@SP // スタックポインタを{0}に設定する\n".format(self.segment[segment]))
        self.stream.write("M=D // RAM[0]に{0}を入れる\n".format(self.segment[segment]))
        segment = "local"
        self.stream.write("@{0} // {0}(RAM[{0}])をDレジスタに一時退避\n".format(self.segment[segment]))
        self.stream.write("D=A\n")
        self.stream.write("@LCL // スタックポインタを{0}に設定する\n".format(self.segment[segment]))
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
            self.stream.write("D=A+1 // DレジスタにSPを入れて退避させる\n")
            self.stream.write("@SP\n")
            self.stream.write("M=D // Dレジスタに退避させていたSPを入れて次のpush popに備える\n")

        if command == "sub":
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("M=M-1\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("M=M-D // RAM[SP] - RAM[SP-1]\n")
            self.stream.write("D=A+1 // DレジスタにSPを入れて退避させる\n")
            self.stream.write("@SP\n")
            self.stream.write("M=D // Dレジスタに退避させていたSPを入れて次のpush popに備える\n")

        if command == "neg":
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("M=M-1\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("M=-M // -RAM[SP]\n")
            self.stream.write("D=A+1 // DレジスタにSPを入れて退避させる\n")
            self.stream.write("@SP\n")
            self.stream.write("M=D // Dレジスタに退避させていたSPを入れて次のpush popに備える\n")

        if command == "eq":
            self.stream.write("@SP // popするのでアドレスを1減らす\n")
            self.stream.write("M=M-1\n")
            self.stream.write("D=M\n")
            self.stream.write("A=D // アドレスをRAM[SP]に変更する\n")
            self.stream.write("D=M // DレジスタにRAM[SP]の中身を退避させる\n")
            self.stream.write("A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる\n")
            self.stream.write("M=M-D // RAM[SP] - RAM[SP-1]\n")
            self.stream.write("D=A+1 // DレジスタにSPを入れて退避させる\n")
            self.stream.write("@SP\n")
            self.stream.write("M=D // Dレジスタに退避させていたSPを入れて次のpush popに備える\n")

        if command == "gt":
            return ">"

        if command == "lt":
            return "<"

        if command == "and":
            return "&"

        if command == "or":
            return "|"

        if command == "not":
            return "!"

    def writePushCommand(self, segment, index):
        """
        アセンブリ言語に書き換えるためのメソッド
        共通ならばここに書いてしまおう
        """
        if segment == "constant":
            ptr = "SP"
        elif segment == "local":
            ptr = "LCL"
        elif segment == "argument":
            ptr = "ARG"
        elif segment == "this":
            ptr = "THIS"
        elif segment == "that":
            ptr = "THAT"
        else:
            raise BaseException("notfound segment: {0}".format(segment))

        self.stream.write("// push {0} {1} コマンド\n".format(segment, index))
        self.stream.write("@{0} // {0}をpushする\n".format(index))
        self.stream.write("D=A\n")
        self.stream.write("@{0}\n".format(ptr))
        self.stream.write("A=M // アドレスを{0}に設定する\n".format(self.segment[segment]))
        self.stream.write("M=D // RAM[{0}]に{1} {2}が入る\n".format(self.segment[segment], segment, index))
        self.stream.write("D=A+1 // SPレジスタ(RAM[{0}])に1を追加してDレジスタに退避\n".format(self.segment[segment]))
        self.stream.write(
            "@{0} // pushの作業が終わったのでSPレジスタに1追加したDレジスタから代入して終了\n".format(
                ptr
            )
        )
        self.stream.write("M=D\n")

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
                self.stream.write("// push {0} {1} コマンド\n".format(segment, index))
                self.stream.write("@{0} // {0}をpushする\n".format(index))
                self.stream.write("D=A\n")
                self.stream.write("@SP\n")
                self.stream.write("A=M // アドレスを{0}に設定する\n".format(self.segment[segment]))
                self.stream.write("M=D // RAM[{0}]に{1} {2}が入る\n".format(self.segment[segment], segment, index))
                self.stream.write("D=A+1 // SPレジスタ(RAM[{0}])に1を追加してDレジスタに退避\n".format(self.segment[segment]))
                self.stream.write("@SP // pushの作業が終わったのでSPレジスタに1追加したDレジスタから代入して終了\n")
                self.stream.write("M=D\n")
        elif c_command == "pop":
            if segment == "local" or \
                    segment == "argument" or \
                    segment == "this" or \
                    segment == "that":
                self.stream.write("// push {0} {1} コマンド\n".format(segment, index))
                self.stream.write("@{0} // {0}をpushする\n".format(index))
                self.stream.write("D=A\n")
                self.stream.write("@SP\n")
                self.stream.write("A=M // アドレスを{0}に設定する\n".format(self.segment[segment]))
                self.stream.write("M=D // RAM[{0}]に{1} {2}が入る\n".format(self.segment[segment], segment, index))
                self.stream.write("D=A-1 // SPレジスタ(RAM[{0}])に1を追加してDレジスタに退避\n".format(self.segment[segment]))
                self.stream.write("@SP // pushの作業が終わったのでSPレジスタに1追加したDレジスタから代入して終了\n")
                self.stream.write("M=D\n")


    def close(self):
        """
        出力ファイルを閉じる
        """
        self.stream.close()

