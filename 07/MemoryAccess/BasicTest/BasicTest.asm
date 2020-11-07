// push constant 10 コマンド
@10 // 10をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 10が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop local 0 コマンド
@0
D=A
@LCL
M=D+M
@0
@SP // 0 スタックポインタをセットする
M=M-1
A=M
D=M
@LCL
A=M
M=D
@0
D=A
@LCL
M=M-D
// push constant 21 コマンド
@21 // 21をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 21が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// push constant 22 コマンド
@22 // 22をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 22が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop argument 2 コマンド
@2
D=A
@ARG
M=D+M
@2
@SP // 2 スタックポインタをセットする
M=M-1
A=M
D=M
@ARG
A=M
M=D
@2
D=A
@ARG
M=M-D
// pop argument 1 コマンド
@1
D=A
@ARG
M=D+M
@1
@SP // 1 スタックポインタをセットする
M=M-1
A=M
D=M
@ARG
A=M
M=D
@1
D=A
@ARG
M=M-D
// push constant 36 コマンド
@36 // 36をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 36が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop this 6 コマンド
@6
D=A
@THIS
M=D+M
@6
@SP // 6 スタックポインタをセットする
M=M-1
A=M
D=M
@THIS
A=M
M=D
@6
D=A
@THIS
M=M-D
// push constant 42 コマンド
@42 // 42をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 42が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// push constant 45 コマンド
@45 // 45をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 45が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop that 5 コマンド
@5
D=A
@THAT
M=D+M
@5
@SP // 5 スタックポインタをセットする
M=M-1
A=M
D=M
@THAT
A=M
M=D
@5
D=A
@THAT
M=M-D
// pop that 2 コマンド
@2
D=A
@THAT
M=D+M
@2
@SP // 2 スタックポインタをセットする
M=M-1
A=M
D=M
@THAT
A=M
M=D
@2
D=A
@THAT
M=M-D
// push constant 510 コマンド
@510 // 510をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 510が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop temp 6 コマンド
@SP
M=M-1
@11
M=D
// push local 0 コマンド
@LCL
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push that 5 コマンド
@THAT
A=M
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
// push argument 1 コマンド
@ARG
A=M
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
// push this 6 コマンド
@THIS
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
// push this 6 コマンド
@THIS
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
// subコマンド
@SP // popするのでアドレスを1減らす
M=M-1
D=M
A=D // アドレスをRAM[SP]に変更する
D=M // DレジスタにRAM[SP]の中身を退避させる
A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる
M=M-D // RAM[SP] - RAM[SP-1]
// push temp 6 コマンド
@11
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
