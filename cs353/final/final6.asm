    segment .bss
a   resd 100       

    segment .data
n   dd 100

    segment .text
    global main
main:
    mov edx, [n-1] ; n - 1 = 99
    xor ecx, ecx ; ecx == 0 ;

for: cmp ecx, edx ; ecx < edx    edx should == 99
    xor r8d, r8d ; r8d == 0 ;
    xor r9d, r9d ; r9d == 0 ;
    xor r10d, r10d ; r10d == 0 ;

    add r8d, [ecx+0] ; 0 + ecx (counter value) ;
    add r9d, [ecx+0] ; 0 + ecx (counter value) ;
    add r10d,[ecx+0] ; 0 + ecx (counter value) ;
    
    imul r9d, r8d ; first multiplication ;
    mov r10d, r9d ; moving result of first multiplication ; 
    imul r10d, r8d ; second multiplication ;
    mov r9d, r10d ; moving result of second multiplication ;
    imul r9d, r8d ; third multiplication ;
    
    mov [a + ecx * 4], r9d ; finally moving third multiplication result into array ;
    inc ecx ; incrementing ecx (counter value) ;
    jmp for ; jump to beginning for loop ; 
end_for:

