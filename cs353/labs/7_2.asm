    segment .data
a dq 10
b dq 5
    segment .text
    global main
main:
    mov al, [a]
    mov bl, [b]
    
    xor al, bl
    xor bl, al
    xor al, bl
    
    mov [a], al
    mov [b], bl
    ret
