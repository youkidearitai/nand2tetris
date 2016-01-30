@256 // 256(RAM[256])をDレジスタに一時退避
D=A
@SP // スタックポインタを256に設定する
M=D // RAM[0]に256を入れる
// push constant 10 コマンド
@10 // 10をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 10が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// push constant 9 コマンド
@9 // 9をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 9が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// eqコマンド
@SP // popするのでアドレスを1減らす
M=M-1
D=M
A=D // アドレスをRAM[SP]に変更する
D=M // DレジスタにRAM[SP]の中身を退避させる
A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる
D=M-D // RAM[SP] - RAM[SP-1]
@GTHAN_EQ0 // RAM[SP] - RAM[SP-1]
D;JEQ // RAM[SP] - RAM[SP-1]
@SP
D=M
A=D-1
M=0
@GTHAN_EQ_END0
0;JMP
(GTHAN_EQ0)
  @SP
  D=M
  A=D-1
  M=-1
(GTHAN_EQ_END0)
