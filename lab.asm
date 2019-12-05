    segment .text
    global main
    external printf
a equ 0
b equ 0
    
print_max:
    push rbp
    mov rbp, rsp
    sub rsp, 32

max equ 16
    mov[rsp+a], rdi ; local a = parameter a
    mov [rsp+b], rsi
    mov [rsp+max], rdi
    
    cmp rdi, rsi
    jge skip
    mov [rsp+max], rsi
        
skip:
    ;printf("max(%ld, %ld) = %ld
    segment .data
fat db "max(%ld,%ld) = %ld", 0x0a, 0
    segment .text
    
    lea rdi, [fxt]
    mov rsi, [rsp+a]
    mov rdx, [rsp+b]
    mov rcx, [rsp+max]
    xor eax, eax
    call printf
    
    leave
    ret
    
main:
    push rbp
    mov rbp, rsp
    
    mov rdi, 100
    mov rsi, 200
    call print_max
    
    xor eax, eax
    leave
    ret 
