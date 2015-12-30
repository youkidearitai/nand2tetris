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
// push constant 4 コマンド
@4 // 4をpushする
D=A
@SP
A=M // アドレスを256に設定する
M=D // RAM[256]にconstant 4が入る
@SP
M=M+1 // SPレジスタ(RAM[256])に1を追加してDレジスタに退避
// orコマンド
@SP // popするのでアドレスを1減らす
M=M-1
D=M
A=D // アドレスをRAM[SP]に変更する
D=M // DレジスタにRAM[SP]の中身を退避させる
A=A-1 // RAM[SP-1]の中身をみるためにアドレスを減算させる
M=M|D // RAM[SP] | RAM[SP-1]
