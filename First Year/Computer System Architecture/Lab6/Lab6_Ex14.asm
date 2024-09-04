bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s dd 12345607h, 1A2B3C15h
    lens equ $-s
    d resb 8

; our code starts here
segment code use32 class=code
    start:
        cld
        mov esi, s
        mov edi, d
        mov ecx, 2
        rep movsd           ; copy the doubleword array
        mov ecx, lens
        dec ecx
        mov edx, lens
        
    outerloop:
        mov esi, d      
        mov edi, d
        inc edi
        
    innerloop:
        lodsb           ; load byte x into al, go to x+1
        mov bl, al     ; load first byte into bl
        
        lodsb           ; load byte x + 1 into al, go to x+2
        dec esi         ; stay to x+1
        cmp al, bl      ; compare the two adjacent bytes s[x+1] and s[x]
        jae no_swap     ; if they are in ascending order do nothing
        
        ;Swap if al < bl (s[x+1] < s[x])
        stosb           ; store s[x+1] into the list
        mov al, bl
        stosb           ; store s[x] after s[x+1]

        
    no_swap:
        mov edi, esi    ; insert at position x+1
        loop innerloop
        cmp edx, 0
        ja reset_loop
        jmp final
    
    reset_loop:
        dec edx
        mov ecx, edx
        loop outerloop

    final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
