bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 5
    b dw 300
    c dd 66000
    d dq 100000

; our code starts here
segment code use32 class=code
    start:
    ;(a+d)-(c-b)+c
        mov eax, dword [d]      
        mov edx, dword [d+4]    ; edx:eax = d
        mov ebx, 0      
        mov bl, byte [a]        ; ebx = a
        add eax, ebx            
        adc edx, 0              ; edx:eax = a+d
        mov ebx, dword [c]      ; ebx = c
        mov ecx, 0
        mov cx, word [b]        ; ecx = b
        sub ebx, ecx            ; ebx = c-b
        sub eax, ebx            ; eax = (a+d)-(c-b)
        add eax, dword [c]      ; eax = (a+d)-(c-b) + c
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
