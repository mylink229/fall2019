    segment .data
a   db  01100101b
b   db  0

    segment .text
    global main
main:
    mov rax, [a]
    
    bt  rax, 0
    setc dl
    mov [b], dl
    
    bt  rax, 1
    setc dl
    add [b], dl
    
    bt  rax, 2
    setc dl
    add [b], dl
    
    bt  rax, 3
    setc dl
    add [b], dl
    
    bt  rax, 4
    setc dl
    add [b], dl
    
    bt  rax, 5
    setc dl
    add [b], dl
    
    bt  rax, 6
    setc dl
    add [b], dl
    
    bt  rax, 7
    setc dl
    add [b], dl 

    ret

