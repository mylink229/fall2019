    segment .data
a   dw 0
b   dw 0

format: 
    dw "%hd %hd"

    segment .text
    global main
    global ecal
    extern scanf
main:
    xor rbx, rbx
    
    lea rdi, format
    lea rsi, [a]
    lea rdx, [b]
    xor rax, rax
    call scanf
    mov rdi, [a]
    mov rsi, [b]
    
    xor rdx, rdx
    xor eax, eax
    
    call scanf
    call ecal
ecal:
    push rbp
    mov rbp, rsp
    sub rsp, 16
    mov rdx, rdi
    mov eax, rsi
