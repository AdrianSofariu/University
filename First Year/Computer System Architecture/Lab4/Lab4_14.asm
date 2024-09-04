bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 1234ABCDh
    b resb 4
    c resb 1
   

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; Obtain the integer number n represented on bits 14-17 of A
        mov eax, DWORD [a]
        shr eax, 14
        and eax, 0xF
        mov ecx, eax ; ecx(cl) now contains n
        
        ; Obtain the doubleword B by rotating A n positions to the left
        mov eax, DWORD [a]
        
        ;B is in eax
        
        rol eax, cl         ; rotate n times
        

        mov [b], eax    ; eax in b
        mov ecx, 0      ; 0 in ecx
        
        ; Obtain the byte C as follows
        
        ;the bits 0-5 of C are the same as the bits 1-6 of B
        mov ebx, eax    ; B in ebx
        shr ebx, 1      ; bits 1-6 become bits 0-5
        and ebx, 0x3F   ; keep just the bits 0-5 with value 1
        
        
        ;the bits 6-7 of C are the same as the bits 17-18 of B
        mov ecx, eax    ; B in ecx
        shr ecx, 11     ; bits 17-18 become bits 6-7
        and ecx, 0xC0   ; keep just the bits 6-7 with value 1
        
        or ebx, ecx     ; C in ebx(bl)
        mov [c], bl
        
               
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
