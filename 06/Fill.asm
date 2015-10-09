// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.
(LOOP)

    @i
    M=0

    @KBD
    D=M

    @BLACK
    D;JGT

    (WHITE)
        @SCREEN
        M=0

        @i
        D=M

        @8190
        D=D-A

        @LOOP
        D;JGT

        @i
        D=M+1

        @SCREEN
        A=D+A
        M=0

        @i
        M=M+1
    @WHITE
    0;JMP


    (BLACK)
        @SCREEN
        M=-1

        @i
        D=M

        @8190
        D=D-A

        @LOOP
        D;JGT

        @i
        D=M+1

        @SCREEN
        A=D+A
        M=-1

        @i
        M=M+1
    @BLACK
    0;JMP

@LOOP
0;JMP

(END)
@END
0;JMP
