bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fprintf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions 
import fopen msvcrt.dll 
import fprintf msvcrt.dll 
import fclose msvcrt.dll 


; A file name and a text (defined in the data segment) are given. 
; The text contains lowercase letters, uppercase letters, digits and special characters.
; Transform all the uppercase letters from the given text in lowercase. 
; Create a file with the given name and write the generated text to file.


; our data is declared here (the variables needed by our program)
segment data use32 class=data
    text db "AB76#$ab/MNZ;", 0
    len equ $-text
    
    modified_text resb len
    file_name db "nou.txt", 0
    
    file_descriptor dd -1
    acces_mode db "w", 0

; our code starts here
segment code use32 class=code
    start:
    
        ;call fopen to create the new file
        push dword acces_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor], eax  ; store file descriptor
        
        ;check if creation was successful, if not jump to the end
        cmp eax, 0
        je final
        
        ;transform text byte by byte
        mov esi, text
        mov edi, modified_text
        cld
        
    transform:
        
        lodsb       ;load byte from text into al 
        cmp al, 0   ; check if we are at the end of the file
        je write
        
        ;check if the character is an uppercase letter
        cmp al, "A"
        jb next
        
        cmp al, "Z"
        ja next
        
        ;transform number to lowercase
        add al, "a"-"A"
        
    next:
        stosb       ;store byte into modified_text
        jmp transform   ; repeat for each character
  
    write:
    
        mov al, 0
        stosb       ;save 0 at the end of the new text
        
        ;write in file
        push dword modified_text
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4*2
        
        ;close the file
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
    final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
