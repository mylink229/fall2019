    segment .data
msg:    db  "Hello world!", 0x0a, 0
    section .text
    global main
    extern printf
main:
    push rbp
    mov rbp, rsp
    
    lea rdi, [msg]
    xor eax, eax
    cell printf
    
    xor eax, eax
    pop rdp
    ret
