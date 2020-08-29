.thumb
.syntax unified

.include "gpio_constants.s"     // Register-adresser og konstanter for GPIO
.include "sys-tick_constants.s" // Register-adresser og konstanter for SysTick

.text
	.global Start

Start:

    //SYSTICK SETUP
    //LOAD
    LDR R0, =FREQUENCY / 10
    LDR R1, =SYSTICK_BASE + SYSTICK_LOAD
    STR R0, [R1] // 100ms lagret til LOAD

    //VAL
    LDR R0, =SYSTICK_BASE
    LDR R1, =FREQUENCY / 10
    STR R1, [R0] // Setter startdelay til 100ms

   	//CTRL
   	LDR R0, =SYSTICK_BASE + SYSTICK_CTRL
	LDR R1, =SysTick_CTRL_CLKSOURCE_Msk | SysTick_CTRL_TICKINT_Msk
    STR R1, [R0] // 0b110 lagret til CTRL

    // BUTTON INTERRUPT SETUP
    // EXTIPSEL - EXternal Interrupt Port SELect (FUNKER)
	LDR R0, =GPIO_BASE + GPIO_EXTIPSELH
	MOV R1, 0b1111
	LSL R2, R1, #4
	MVN R3, R2
	LDR R4, [R0]
	AND R5, R3, R4
	LDR R6, =BUTTON_PORT
	LSL R7, R6, #4
	ORR R8, R5, R7
	STR R8, [R0]

	// EXTIFALL - EXTernal Interrupt FALLing Edge Trigger (FUNKER)
	LDR R0, =GPIO_BASE + GPIO_EXTIFALL
	LDR R1, [R0]
    LDR R2, =1 << BUTTON_PIN
    ORR R3, R1, R2
    STR R3, [R0]

    // IEN - Interrupt ENable (FUNKER)
    LDR R0, =GPIO_BASE + GPIO_IEN
    LDR R1, [R0]
	LDR R2, =1 << BUTTON_PIN
    ORR R3, R1, R2
    STR R3, [R0]

    // Reset IF - Interrupt Flag (FUNKER)
	LDR R0, =GPIO_BASE + GPIO_IFC //CLEAR FLAG
	LDR R1, [R0]
    LDR R2, =1 << BUTTON_PIN
    ORR R3, R1, R2
    STR R3, [R0]

Loop:
	B Loop

.global SysTick_Handler
.thumb_func
SysTick_Handler:
 	// Tidels sekund
    LDR R0, =tenths //R0 = Minnelokasjon til tenths
    LDR R1, [R0] // R1 = Verdien til tenths
    ADD R1, R1, #1
    CMP R1, #10
    BNE UpdateTenths
    // Hvis tenths == 10
    LDR R1, =0 // Tilbakestill tenths

   // Hele sekunder
   LDR R2, =seconds
   LDR R3, [R2] // Verdien til seconds
   ADD R3, R3, #1
   // TOGGLE LED
   LDR R4, =GPIO_BASE + LED_PORT * PORT_SIZE + GPIO_PORT_DOUTTGL
   LDR R5, =1 << LED_PIN
   STR R5, [R4]

   CMP R3, #60
   BNE UpdateSeconds
   // Hvis seconds == 60
   LDR R3, =0 // Tilbakestill Seconds

   // Hele minutter
   LDR R4, =minutes
   LDR R5, [R4] // R5 = Verdien til minutes
   ADD R5, R5, #1
   STR R5, [R4] // Lagre den nye verdien til minutes


UpdateSeconds:
	STR R3, [R2] //Lagre den nye verdien til seconds

UpdateTenths:
	STR R1, [R0] // Lagre den nye verdien til tenths
	BX LR





.global GPIO_ODD_IRQHandler
.thumb_func
GPIO_ODD_IRQHandler:
	// Din interrupt-kode her

	// TOGGL SYSTICK_CTRL ENABLE
	LDR R0, =SYSTICK_BASE + SYSTICK_CTRL
	LDR R1, [R0]
    LDR R2, =SysTick_CTRL_ENABLE_Msk
    EOR R1, R1, R2
    STR R1, [R0]

	// Reset IF - Interrupt Flag
	LDR R0, =GPIO_BASE + GPIO_IFC //CLEAR FLAG
	LDR R1, [R0]
    LDR R2, =1 << BUTTON_PIN
    ORR R3, R1, R2
    STR R3, [R0]

	BX LR // Returner fra interrupt

NOP // Behold denne på bunnen av fila
