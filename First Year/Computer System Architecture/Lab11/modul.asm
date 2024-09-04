bits 32                         

segment data use32 class=data

    delimiters db " ,", 0   ; declare the delimiters for strtok calls

global get_word

extern strtok
import strtok msvcrt.dll

get_word:
        ; Get the i-th word
        
        ;create stack frame
        push ebp
        mov ebp, esp
        
        ; store ebx because we will modify it in this function
        push ebx
        
        ; get parameters from stack
        mov eax, [esp + 12] ; sentence
        mov ebx, [esp + 16] ; index of the wanted word

        ; call strtok for the first word
        push dword delimiters   
        push eax
        call [strtok]
        add esp, 8
        
        ; decrement ebx because we processed 1 word
        dec ebx
        
        ; if we processed the word we need ebx = 0 so we return
        jz func_end
        
        ; call strtok for the rest of the words
        loop_word:
            push dword delimiters
            push dword 0
            call [strtok]
            add esp, 8
            
            ; check if we are ready
            dec ebx
            jnz loop_word
            
        ; return
        func_end:
            ; restore ebx
            pop ebx
            ; restore stack segment
            pop ebp
            ret
	