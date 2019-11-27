    segment .data
a   dq    1
b   dq    2   
    segment .text
    global main
 main:
    
    mov rax, [a]
    mov rbx, [b]
 
    xor rax, rbx    ;a = a ^ b
    xor rbx, rax    ;b = a ^ b
    xor rax, rbx    ;a = a ^ b
    mov [a], rax    ;move the rax values into [a] to confirm that it flipped
    mov [b], rbx    ;now confirm the same flip with rbx into [b]
    
    ret
