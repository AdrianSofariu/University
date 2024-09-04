bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 256
    b dw 255
    c dw 300
    d dw 400
    
; our code starts here
segment code use32 class=code
    start:
    ;(c+d)+(a-b)+a
        mov eax, 0
        mov ax, word [c]    ; ax = c
        add ax, word [d]    
        adc eax, 0          ; ax = c + d
        mov ebx, 0
        mov bx, word [a]    ; bx = a
        sub bx, word [b]    ; bx = a - b
        add eax, ebx        ; eax = c+d+(a-b)
        mov ebx, 0
        mov bx, word [a]    ; ebx = a
        add eax, ebx        ; eax = (c+d)+(a-b)+a
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
