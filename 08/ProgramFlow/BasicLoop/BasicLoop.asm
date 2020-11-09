// push constant 0 コマンド
@0 // 0をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 0が入る
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
// label LOOP_START コマンド
(LOOP_START)
// push argument 0 コマンド
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 0 コマンド
@LCL
A=M
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
// pop local 0	 コマンド
@0	
D=A
@LCL
M=D+M
@0	
@SP // 0	 スタックポインタをセットする
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
// push argument 0 コマンド
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// if-goto LOOP_START コマンド
// pop global コマンド
@SP // global スタックポインタをセットする
M=M-1
A=M
D=M
@LOOP_START
D;JNE
// push local 0 コマンド
@LCL
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
