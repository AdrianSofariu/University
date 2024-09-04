bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program

extern scanf, printf, getchar, exit
import scanf msvcrt.dll
import printf msvcrt.dll              
import getchar msvcrt.dll
import exit msvcrt.dll

extern get_word

                          
;Read an integer (positive number) n from keyboard. Then read n sentences containing at least n words (no validation needed).
;Print the string containing the concatenation of the word i of the sentence i, for i=1,n (separated by a space).
;Example: n=5
;We read the following 5 sentences:
;We read the following 5 sentences.
;Today is monday and it is raining.
;My favorite book is the one I just showed you.
;It is pretty cold today.
;Tomorrow I am going shopping.

;The string printed on the screen should be:
;We is book cold shopping.


segment data use32 class=data
    
    format db " %d", 0
    formatStr db " %[^", 0x0a,"]%*c", 0
    formatWrd db "%s", 0
    space db " ", 0
    n db 0
    new_sentence resb 256
    sentence resb 256
    counter dd 0

segment code use32 public class=code
    
    
    start:
    ; Read the number of sentences
    push n
    push format
    call [scanf]
    add esp, 8
    
    ; Prepare to store the words of the n sentences
    mov edi, new_sentence
    cld

    ; Loop n times to read each sentence and get the i-th word
    mov ecx, [n]
    cmp ecx, 0
    je ending
    
    loop_start:
    
        ; save loop before calling functions
        push ecx
        
        ; read sentence
        push dword sentence
        push dword formatStr
        call [scanf]
        add esp, 8
        
        ; get i'th word of the sentence using the function in the module
        inc dword [counter]
        
        push dword [counter]
        push sentence
        call get_word
        add esp, 8
        
        ; Store the returned word
        mov esi, eax ; Source address
        
        copy_word:
            lodsb ; load byte at address DS:ESI into AL
            test al, al ; test if AL is null
            jz end_copy ; if not, continue copying
            stosb ; store AL at address ES:EDI
            jmp copy_word
        end_copy:
            mov al, [space]
            stosb ; store a space

              
        pop ecx ; restore ecx
        loop loop_start
        
    ; add a \0 character for ASCIIZ format
    mov al, 0
    stosb
    
    push dword new_sentence ; push the address of new_sentence
    push dword formatWrd ; push the format string for printing
    call [printf] ; call printf
    add esp, 8 ; clean up the stack

    ending:
    ; Keep program open
    call [getchar]
    ; Exit the program
    push dword 0
    call [exit]