// writeInit コマンド
@256
D=A
@SP
M=D
// writeCall Sys.init 0 コマンド
// push return-address コマンド
@_CALL_Sys.init1
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL コマンド
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG コマンド
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS コマンド
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT コマンド
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - n - 5
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto Sys.init
@Sys.init
0;JMP
(_CALL_Sys.init1)
// writeFunction Class1.set 0 コマンド
(Class1.set)
// push argument 0 コマンド
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop static 0 コマンド
@SP
M=M-1
A=M
D=M
@Class1.0
M=D
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
// pop static 1 コマンド
@SP
M=M-1
A=M
D=M
@Class1.1
M=D
// push constant 0 コマンド
@0 // 0をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 0が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
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
// writeFunction Class1.get 0 コマンド
(Class1.get)
// push static 0 コマンド
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1 コマンド
@Class1.1
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
// writeFunction Class2.set 0 コマンド
(Class2.set)
// push argument 0 コマンド
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop static 0 コマンド
@SP
M=M-1
A=M
D=M
@Class2.0
M=D
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
// pop static 1 コマンド
@SP
M=M-1
A=M
D=M
@Class2.1
M=D
// push constant 0 コマンド
@0 // 0をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 0が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
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
// writeFunction Class2.get 0 コマンド
(Class2.get)
// push static 0 コマンド
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1 コマンド
@Class2.1
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
// writeFunction Sys.init 0 コマンド
(Sys.init)
// push constant 6 コマンド
@6 // 6をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 6が入る
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
// writeCall Class1.set 2 コマンド
// push return-address コマンド
@_CALL_Class1.set2
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL コマンド
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG コマンド
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS コマンド
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT コマンド
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - n - 5
@SP
D=M
@5
D=D-A
@2
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto Class1.set
@Class1.set
0;JMP
(_CALL_Class1.set2)
// pop temp 0 コマンド
@SP
M=M-1
A=M
D=M
@5
M=D
// push constant 23 コマンド
@23 // 23をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 23が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// push constant 15 コマンド
@15 // 15をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 15が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// writeCall Class2.set 2 コマンド
// push return-address コマンド
@_CALL_Class2.set3
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL コマンド
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG コマンド
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS コマンド
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT コマンド
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - n - 5
@SP
D=M
@5
D=D-A
@2
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto Class2.set
@Class2.set
0;JMP
(_CALL_Class2.set3)
// pop temp 0 コマンド
@SP
M=M-1
A=M
D=M
@5
M=D
// writeCall Class1.get 0 コマンド
// push return-address コマンド
@_CALL_Class1.get4
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL コマンド
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG コマンド
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS コマンド
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT コマンド
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - n - 5
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto Class1.get
@Class1.get
0;JMP
(_CALL_Class1.get4)
// writeCall Class2.get 0 コマンド
// push return-address コマンド
@_CALL_Class2.get5
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL コマンド
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG コマンド
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS コマンド
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT コマンド
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - n - 5
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto Class2.get
@Class2.get
0;JMP
(_CALL_Class2.get5)
// label WHILE コマンド
(Sys$WHILE)
// goto WHILE コマンド
@Sys$WHILE
0;JMP
