bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s db 1, 3, -2, -5, 3, -8, 5, 0
    lens equ $-s
    d1 resb 10
    d2 resb 10
    

; our code starts here
segment code use32 class=code
    start:
        mov esi, 0          ; start with element at position 0
        mov ecx, 0
        mov ecx, lens       ; move length of s into ecx
        mov ebx, d1         ; move address of current element of d1 in ebx
        mov edx, d2         ; move address of current element of d2 in edx
        jecxz final
        
    lp:
       mov al, [s + esi]    ; move s[0] in al
       cmp al, 0            ; compare the element with 0
       jl negative          ; jump if negative
       mov [ebx], al        ; if element is positive move it into d1
       inc ebx
       jmp continue
       
    negative:
       mov [edx], al        ; if element is negative move it into d2
       inc edx
       
    continue:
        inc esi             ; move to next element in s
        loop lp
    
    final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
