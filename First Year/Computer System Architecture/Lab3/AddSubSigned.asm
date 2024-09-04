bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db -5
    b dw 30000
    c dd 100000

; our code starts here
segment code use32 class=code
    start:
        ;c-b-(a+a)-b
        
        mov ebx, dword [c]  ; ebx = c
        mov ax, word [b]    ; ax = b
        cwde                ; eax = b
        sub ebx, eax        ; ebx = c-b
        mov al, byte [a]    ; al = a
        cbw                 ; ax = a
        cwde                ; eax = a
        mov ecx, eax        ; ecx = a
        mov al, byte [a]    ; al = a
        cbw                 ; ax = a
        cwde                ; eax = a
        add ecx, eax        ; ecx = a+a
        sub ebx, ecx        ; ebx = c-b-(a+a)
        mov ax, word [b]    ; ax = b
        cwde                ; eax = b
        sub ebx, eax        ; ebx = c-b-(a+a)-b
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
