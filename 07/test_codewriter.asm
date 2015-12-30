@256 // 256(RAM[256])をDレジスタに一時退避
D=A
@SP // スタックポインタを256に設定する
M=D // RAM[0]に256を入れる
// push constant 6 コマンド
@6 // 6をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 6が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// push constant 7 コマンド
@7 // 7をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 7が入る
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
// pop local 1 コマンド
@SP // 1 スタックポインタをセットする
D=M
A=D
D=M
@1
A=M+D // DレジスタにLCL + 1が入る
A=A-D // DレジスタにLCL + 1が入る
M=D
@SP
M=M-1 // SPレジスタ(RAM[1])に1を追加してDレジスタに退避
// pop argument 3 コマンド
@SP // 3 スタックポインタをセットする
D=M
A=D
D=M
@3
A=M+D // DレジスタにARG + 3が入る
A=A-D // DレジスタにARG + 3が入る
M=D
@SP
M=M-1 // SPレジスタ(RAM[2])に1を追加してDレジスタに退避
