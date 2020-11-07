// push constant 111 コマンド
@111 // 111をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 111が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// push constant 333 コマンド
@333 // 333をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 333が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// push constant 888 コマンド
@888 // 888をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 888が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop static 8 コマンド
@SP
M=M-1
A=M
D=M
@24
M=D
@SP
A=M
M=D
// pop static 3 コマンド
@SP
M=M-1
A=M
D=M
@19
M=D
@SP
A=M
M=D
// pop static 1 コマンド
@SP
M=M-1
A=M
D=M
@17
M=D
@SP
A=M
M=D
// push static 3 コマンド
@None.3
D=M
@19
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1 コマンド
@None.1
D=M
@17
D=M
@SP
A=M
M=D
@SP
M=M+1
// subコマンド
@SP // popするのでアドレスを1減らす
M=M-1
D=M
A=D // アドレスをRAM[SP]に変更する
D=M // DレジスタにRAM[SP]の中身を退避させる
A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる
M=M-D // RAM[SP] - RAM[SP-1]
// push static 8 コマンド
@None.8
D=M
@24
D=M
@SP
A=M
M=D
@SP
M=M+1
// addコマンド
@SP // popするのでアドレスを1減らす
M=M-1
D=M
A=D // アドレスをRAM[SP]に変更する
D=M // DレジスタにRAM[SP]の中身を退避させる
A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる
M=M+D // RAM[SP] + RAM[SP-1]
