#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import tempfile
import codewriter

class TestCodewriter(unittest.TestCase):
    def setUp(self):
        pass

    def testWriteAsmFile(self):
        o = tempfile.NamedTemporaryFile()
        c = codewriter.CodeWriter(o)

        c.writePushpop("push", "constant", 6)
        c.writePushpop("push", "constant", 7)
        c.writeArithmetic("add")

        example = """// push constant 6 コマンド
@256 // 256(RAM[256])をDレジスタに一時退避
D=A
@SP // スタックポインタを256に設定する
M=D // RAM[0]に256を入れる
@6 // 6をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 6が入る
D=A+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
@SP // pushの作業が終わったのでSPレジスタに1追加したDレジスタから代入して終了
M=D
// push constant 7 コマンド
@257 // 257(RAM[257])をDレジスタに一時退避
D=A
@SP // スタックポインタを257に設定する
M=D // RAM[0]に257を入れる
@7 // 7をpushする
D=A
@SP
A=M // アドレスを257に設定する
M=D // RAM[257]にconstant 7が入る
D=A+1 // SPレジスタ(RAM[257])に1を追加してDレジスタに退避
@SP // pushの作業が終わったのでSPレジスタに1追加したDレジスタから代入して終了
M=D
// addコマンド
@SP // popするのでアドレスを1減らす
M=M-1
D=M
A=D // アドレスをRAM[SP]に変更する
D=M // DレジスタにRAM[SP]の中身を退避させる
A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる
M=M+D // RAM[SP] + RAM[SP-1]
D=A+1 // DレジスタにSPを入れて退避させる
@SP
M=D // Dレジスタに退避させていたSPを入れて次のpush popに備える
"""

        c.stream.seek(0)
        example = example.split("\n")

        for e in example:
            c_line = c.stream.readline().strip()
            self.assertEqual(c_line, e)

        c.close()

if __name__ == "__main__":
    unittest.main()

