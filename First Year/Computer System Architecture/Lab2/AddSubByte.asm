bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 4
    b db 5
    c db 1
    d db 10

; our code starts here
segment code use32 class=code
    start:
    ;(a+d-c)-(b+b)
        mov al, byte [a]    ; al = a
        mov ah, 0           ; ax = a
        add al, byte [d] 
        adc ah, 0           ; ax = a+d
        sub al, byte [c]
        sbb ah, 0           ; ax = a+d-c
        mov bl, byte [b]    ; bl = b
        mov bh, 0           ; bx  = b
        add bl, byte [b]
        adc bh, 0           ; bx = b+b
        sub ax, bx          ; ax = (a+d-c)-(b+b)
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
