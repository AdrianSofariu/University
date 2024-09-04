bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern scanf, fopen, fclose, fprintf
import scanf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll

;A file name is given in the data segment. Read from the console numbers in base 10, until 0 is met.
;Write to the file each number followed by the product with all the numbers read so far.

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    filename db "out.txt",0
    readformat db "%d",0
    writeformat db "%d - %d",10,0
    appendmode db "a",0
    filedesc resd 1
    number resd 1
    product dd 1

; our code starts here
segment code use32 class=code
    start:
    
        ;open output file in append mode
        push dword appendmode
        push dword  filename
        call [fopen]
        add esp, 4*2
        
        ; check if file is open
        cmp eax, 0
        je end
        
        ; save descriptor
        mov [filedesc], eax
        
        repeat:
        
        ; read a number
        push dword number
        push dword readformat
        call [scanf]
        add esp, 4*2
        
        ; if we read 0 then we can end
        cmp dword [number], 0
        je closefile
        
        ; if number is not 0 we multiply the product
        ; whole product is in edx:eax
        mov eax, [product]
        imul dword [number]
        
        ;save only the low dword in memory
        mov [product], eax
        
        ; write number and  product in file with format "number - product\n"
        push dword [product]
        push dword [number]
        push dword writeformat
        push dword [filedesc]
        call [fprintf]
        add esp, 4*4
        
        ;next number
        jmp repeat
        
        ; close the file
        closefile:
        push dword [filedesc]
        call [fclose]
        add esp, 4
        
    end:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
