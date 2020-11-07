// push constant 3030 コマンド
@3030 // 3030をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 3030が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop pointer 0 コマンド
@SP
M=M-1
@3
M=D
@SP
A=M
M=D
// push constant 3040 コマンド
@3040 // 3040をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 3040が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop pointer 1 コマンド
@SP
M=M-1
@4
M=D
@SP
A=M
M=D
// push constant 32 コマンド
@32 // 32をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 32が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop this 2 コマンド
@2
D=A
@THIS
M=D+M
@2
@SP // 2 スタックポインタをセットする
M=M-1
A=M
D=M
@THIS
A=M
M=D
@2
D=A
@THIS
M=M-D
// push constant 46 コマンド
@46 // 46をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 46が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop that 6 コマンド
@6
D=A
@THAT
M=D+M
@6
@SP // 6 スタックポインタをセットする
M=M-1
A=M
D=M
@THAT
A=M
M=D
@6
D=A
@THAT
M=M-D
// push pointer 0 コマンド
@3
D=M
@SP
A=M
M=D
@SP
M=M+1
// push pointer 1 コマンド
@4
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
// push this 2 コマンド
@THIS
A=M
A=A+1
A=A+1
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
// push that 6 コマンド
@THAT
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
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
