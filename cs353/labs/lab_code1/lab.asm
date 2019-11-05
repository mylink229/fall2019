    segment .data
a   dq  175
b   dq  0x1b
c   dq  -1
d   dq  -5 
    
    segment .text
    global main
main:
    mov rax, [a] 
    mov rbx, [b]
    mov rcx, [c]
    mov rdx, [d]
    add rax, rbx
    add rax, rcx
    add rax, rdx
    ret
