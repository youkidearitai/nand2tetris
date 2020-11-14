// writeFunction SimpleFunction.test 2 コマンド
(SimpleFunction.test)
@SP
A=M
M=D
@SP
M=M+1
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
// push local 1 コマンド
@LCL
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
// notコマンド
@SP // popするのでアドレスを1減らす
D=M
A=D // アドレスをRAM[SP]に変更する
D=M // DレジスタにRAM[SP]の中身を退避させる
A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる
M=!M // RAM[SP] ! RAM[SP-1]
// push argument 0 コマンド
@ARG
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
// writeReturn コマンド
// FRAME = LCL FRAME = R13
@LCL
D=M
@R13
M=D
// RET = *(FRAME - 5)
@5
D=A
@R13
A=M-D
D=M
@R14
M=D
// *ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// SP = ARG+1
@ARG
D=M+1
@SP
M=D
// THAT = *(FRAME - 1)
@R13
AM=M-1
D=M
@THAT
M=D
// THIS = *(FRAME - 2)
@R13
AM=M-1
D=M
@THIS
M=D
// ARG = *(FRAME - 3)
@R13
AM=M-1
D=M
@ARG
M=D
// LCL = *(FRAME - 4)
@R13
AM=M-1
D=M
@LCL
M=D
// goto RET
@R14
A=M
0;JMP
