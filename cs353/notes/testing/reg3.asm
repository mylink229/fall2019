	_segment .data
a 	dq 	175
b	dq	4097
	_segment .text
	global main
main:
	mov rax, [a]
	mov rbx, [b]
	add rax, rbx
	xor eax, eax	
	ret	
