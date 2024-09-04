bits 32

global _display_in_octal

    
segment code use32 public class=code
_display_in_octal:

    push ebp
    mov ebp, esp    ; create stack frame

    mov eax, 0
    mov esi, [ebp+8]    ;  prepare the number in string format for conversion
    mov ecx, 0

    ; Convert binary string to integer
    next_digit:
        lodsb           ; load character
        shl ecx, 1      ; shift the number to make place for the new digit
        sub eax, '0'    ; transform character into digit
        add ecx, eax    ; add new digit to final number
        cmp dword [esi], 0  ; end when we reach the null character
        jne next_digit

    ; Return integer in eax
    mov eax, 0
    mov eax, ecx    ; return the number 

    mov esp, ebp    ; restore stack frame
    pop ebp
    ret             ; return