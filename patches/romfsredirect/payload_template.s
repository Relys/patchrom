.arm

.global _start
.type _start, %function
_start:
STMFD   SP!, {R3-R11,LR}
ldr		r0, =str
MOV     R5, R0
MOV     R1, #9
MOV     R0, SP
ldr		R4, =%mountArchive%
BLX      R4
MOV     R3, #0
LDR     R1, [SP]
MOV     R2, R3
MOV     R0, R5
ldr		R4, =%regArchive%
BLX      R4
MOV     R5, R0
LDR     R0, [SP]
LDR     R1, [R0]
LDR     R1, [R1,#0x30]

MOV     R0, R5
LDMFD   SP!, {R3-R11,PC}

str: 
	.asciz "rom:"

