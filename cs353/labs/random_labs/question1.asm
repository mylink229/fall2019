    segment .data
a   dq  01000101b
b   db  0

    segment .text
    global main
main:
    xor rdx, rdx
    xor rax, rax
    mov rax, [a]
    
    bt  ax, 0
    setc dl
    mov [b], dl
    
    bt  ax, 1
    setc dl
    add [b], dl
    
    bt  ax, 2
    setc dl
    add [b], dl
    
    bt  ax, 3
    setc dl
    add [b], dl
    
    bt  ax, 4
    setc dl
    add [b], dl
    
    bt  ax, 5
    setc dl
    add [b], dl
    
    bt  ax, 6
    setc dl
    add [b], dl
    
    bt  ax, 7
    setc dl
    add [b], dl 

    ret


