bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 10
    b db 2
    c db 20
    d dw 300

; our code starts here
segment code use32 class=code
    start:
    ;(d-b*c+b*2)/a
        mov al, byte [b]    ; ax = b
        mul byte [c]        ; ax = b*c
        mov bx, word [d]    ; bx = d
        sub bx, ax          ; bx = d-b*c
        mov al, byte [b]    ; al =b
        mov ah, 2           ; ah = 2
        mul ah              ; ax = b*2
        mov dx, 0           
        add bx, ax          
        adc dx, 0           ; dx:bx = d-b*c+b*2
        mov ax, bx          ; dx:ax = d-b*c+b*2
        mov cl, byte [a]    
        mov ch, 0           ; cx = a
        div word cx         ; ax = (d-b*c+b*2)/a
            
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
