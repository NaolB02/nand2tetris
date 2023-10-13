// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(LOOP)
    @i
    M=0                    // i = 0
    @8192
    D=A
    @n
    M=D                    // n = 8192 - the number of registers that represent the screen

    @KBD
    D=M
    @LOOP3
    D;JEQ                  // if RAM[KBD] == 0 goto LOOP3

    (LOOP2)                // when a key is pressed turn the whole screen to black
        @i
        D=M
        @n
        D=D-M
        @END
        D;JGE              // if i >= n, goto END

        @i
        D=M
        @SCREEN
        A=A+D
        M=-1               // RAM[SCREEN + i] = -1
        @i
        M=M+1              // i++
        @LOOP2
        0;JMP              // goto LOOP2
    
    (LOOP3)                // when no key is pressed turn the whole screen to white
        @i
        D=M
        @n
        D=D-M
        @END
        D;JGE              // if i >= n, goto END

        @i
        D=M
        @SCREEN
        A=A+D
        M=0                // RAM[SCREEN + i] = 0
        @i
        M=M+1              // i++
        @LOOP3
        0;JMP              // goto LOOP3
    
    (END)
        @LOOP
        0;JMP              // goto LOOP