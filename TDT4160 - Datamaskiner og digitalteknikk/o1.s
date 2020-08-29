.thumb
.syntax unified

.include "gpio_constants.s"     // Register-adresser og konstanter for GPIO

.text
	.global Start

Start:

    // Skriv din kode her...
    LDR R0, =LED_PORT
    LDR R1, =BUTTON_PORT
    LDR R2, =GPIO_BASE
    LDR R3, =PORT_SIZE

    MUL R0, R0, R3
    MUL R1, R1, R3

    ADD R0, R0, R2 // R0 = GPIO_BASE + (LED_PORT * PORT_SIZE)

    ADD R1, R1, R2 // R1 = GPIO_BASE + (BUTTON_PORT * PORT_SIZE)
    LDR R2, =GPIO_PORT_DIN
    ADD R1, R1, R2 //  R1 = GPIO_BASE + (BUTTON_PORT * PORT_SIZE) + GPIO_PORT_DIN

    MOV R2, #1
    LSL R2, R2, #LED_PIN

    MOV R3, #1
    LSL R3, R3, #BUTTON_PIN

    LDR R4, =GPIO_PORT_DOUTSET
    LDR R5, =GPIO_PORT_DOUTCLR

LOOP:
	LDR R6, [R1]
	AND R6, R6, R3
	CMP R6, R3
	BEQ LEDON // G til LEDON hvis R6 == R3

LEDOFF:
	STR R2, [R0, R4]
	B LOOP

LEDON:
	STR R2, [R0, R5]
	B LOOP

NOP // Behold denne p bunnen av fila
