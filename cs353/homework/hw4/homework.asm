    segment .data
z   dq  10, 9, 8, 7, 6, 5, 4, 3, 2, 1
x   dw  "Hello world.", 0

    segment .bss
v   resb  5

    segment .text
    global main
main:
    ret
