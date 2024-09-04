bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 1
    b dw 1
    c dd 30000
    x dq 10

; our code starts here
segment code use32 class=code
    start:
        ;x+(2-a*b)/(a*3)-a+c
        mov ah, 0
        mov al, byte [a]        ; ax = a
        mov bx, word [b]        ; bx = b
        mul word bx             ; dx:ax = a*b
        push dx
        push ax
        pop ebx                 ; ebx = a*b
        mov ecx, 2              ; ecx = 2
        sub ecx, ebx            ; ecx = 2-a*b
        push ecx
        mov al, byte [a]        ; al = a
        mov ah, 3               ; ah = 3
        mul byte ah             ; ax = a*3
        mov cx, ax              ; cx = a*3
        pop ax  
        pop dx                  ; dx:ax = 2-a*b
        div word cx             ; ax = (2-a*b)/(a*3)
        mov ebx, dword [x]
        mov edx, dword [x+4]    ; edx:ebx = x
        add ebx, eax
        adc edx, 0              ; edx:ebx = x + (2-a*b)/(a*3)
        mov eax, 0
        mov al, byte [a]        ; eax = a
        sub ebx, eax
        sbb edx, 0              ; edx:ebx = x + (2-a*b)/(a*3)-a
        mov eax, [c]            ; eax = c
        add ebx, eax
        adc edx, 0              ; edx:ebx = x + (2-a*b)/(a*3)-a+c
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
