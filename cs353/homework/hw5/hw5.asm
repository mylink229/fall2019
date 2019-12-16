    segment .data
a db 00000011b
b db 00000010b
c db 00000000b 

    segment .text
    global main
main:
    mov ax, [a]
    mov cx, [b]
    mov dx, [c]

    imul ax, [a]
    imul cx, [b]

    add dx, ax
    add dx, cx

    mov [c], dx
    ret 



