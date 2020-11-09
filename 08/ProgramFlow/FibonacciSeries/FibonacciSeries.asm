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
// pop pointer 1 コマンド
@SP
M=M-1
A=M
D=M
@4
M=D
// push constant 0 コマンド
@0 // 0をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 0が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop that 0 コマンド
@0
D=A
@THAT
M=D+M
@0
@SP // 0 スタックポインタをセットする
M=M-1
A=M
D=M
@THAT
A=M
M=D
@0
D=A
@THAT
M=M-D
// push constant 1 コマンド
@1 // 1をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 1が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// pop that 1 コマンド
@1
D=A
@THAT
M=D+M
@1
@SP // 1 スタックポインタをセットする
M=M-1
A=M
D=M
@THAT
A=M
M=D
@1
D=A
@THAT
M=M-D
// push argument 0 コマンド
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 2 コマンド
@2 // 2をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 2が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// subコマンド
@SP // popするのでアドレスを1減らす
M=M-1
D=M
A=D // アドレスをRAM[SP]に変更する
D=M // DレジスタにRAM[SP]の中身を退避させる
A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる
M=M-D // RAM[SP] - RAM[SP-1]
// pop argument 0 コマンド
@0
D=A
@ARG
M=D+M
@0
@SP // 0 スタックポインタをセットする
M=M-1
A=M
D=M
@ARG
A=M
M=D
@0
D=A
@ARG
M=M-D
// label MAIN_LOOP_START コマンド
(MAIN_LOOP_START)
// push argument 0 コマンド
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// if-goto COMPUTE_ELEMENT コマンド
// pop global コマンド
@SP // global スタックポインタをセットする
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE
// goto END_PROGRAM コマンド
@END_PROGRAM
0;JMP
// label COMPUTE_ELEMENT コマンド
(COMPUTE_ELEMENT)
// push that 0 コマンド
@THAT
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push that 1 コマンド
@THAT
A=M
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
// push pointer 1 コマンド
@4
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 1 コマンド
@1 // 1をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 1が入る
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
// pop pointer 1 コマンド
@SP
M=M-1
A=M
D=M
@4
M=D
// push argument 0 コマンド
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 1 コマンド
@1 // 1をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 1が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// subコマンド
@SP // popするのでアドレスを1減らす
M=M-1
D=M
A=D // アドレスをRAM[SP]に変更する
D=M // DレジスタにRAM[SP]の中身を退避させる
A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる
M=M-D // RAM[SP] - RAM[SP-1]
// pop argument 0 コマンド
@0
D=A
@ARG
M=D+M
@0
@SP // 0 スタックポインタをセットする
M=M-1
A=M
D=M
@ARG
A=M
M=D
@0
D=A
@ARG
M=M-D
// goto MAIN_LOOP_START コマンド
@MAIN_LOOP_START
0;JMP
// label END_PROGRAM コマンド
(END_PROGRAM)
