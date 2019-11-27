    segment .data
a dw 1,2,3,4
b dw 5,6,7,8

;will hold the sum
c dw
n dw 4

    segment .text
    global main
main:
mov edx, [n-1]
xor ecx, ecx
for: cmp    ecx, edx
    je  end_for
    mov eax, [a+rcx*2]
    imul eax, [b+rcx*2]
    mov [c+ecx*2], eax
    inc ecx
    jmp for
end_for:
