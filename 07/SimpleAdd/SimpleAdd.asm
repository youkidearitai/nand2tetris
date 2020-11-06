// push constant 7 コマンド
@7 // 7をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 7が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// push constant 8 コマンド
@8 // 8をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 8が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// addコマンド
@SP // popするのでアドレスを1減らす
M=M-1
D=M
A=D // アドレスをRAM[SP]に変更する
D=M // DレジスタにRAM[SP]の中身を退避させる
A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる
M=M+D // RAM[SP] + RAM[SP-1]
