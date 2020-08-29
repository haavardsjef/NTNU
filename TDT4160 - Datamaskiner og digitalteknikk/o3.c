// Imports
#include "o3.h"
#include "gpio.h"
#include "systick.h"

// Definer konstanter
//States
#define SET_SECONDS_STATE 0
#define SET_MINUTES_STATE 1
#define SET_HOURS_STATE 2

#define COUNTDOWN_STATE 3
#define ALARM_STATE 4

// Pins and Ports
#define LED_PIN 2
#define LED_PORT GPIO_PORT_E

#define BUTTON0_PIN 9
#define BUTTON1_PIN 10
#define BUTTON_PORT GPIO_PORT_B

// Structs
typedef struct {
	volatile word CTRL;
	volatile word MODEL;
	volatile word MODEH;
	volatile word DOUT;
	volatile word DOUTSET;
	volatile word DOUTCLR;
	volatile word DOUTTGL;
	volatile word DIN;
	volatile word PINLOCKN;
} gpio_port_map_t;

typedef struct {
	volatile gpio_port_map_t ports[6];
	volatile word unused_space[10];
	volatile word EXTIPSELL;
	volatile word EXTIPSELH;
	volatile word EXTIRISE;
	volatile word EXTIFALL;
	volatile word IEN;
	volatile word IF;
	volatile word IFS;
	volatile word IFC;
	volatile word ROUTE;
	volatile word INSENSE;
	volatile word LOCK;
	volatile word CTRL;
	volatile word CMD;
	volatile word EM4WUEN;
	volatile word EM4WUPOL;
	volatile word EM4WUCAUSE;
} gpio_map_t;


typedef struct {
	volatile word CTRL;
	volatile word LOAD;
	volatile word VAL;
	volatile word CALIB;
} systick_t;

// Definer variabler
int state = 0;
int seconds = 0;
int minutes = 0;
int hours = 0;
char time[7];

volatile gpio_map_t* GPIO;
volatile systick_t* SYSTICK;

//Funksjoner
/**************************************************************************//**
 * @brief Konverterer nummer til string
 * Konverterer et nummer mellom 0 og 99 til string
 *****************************************************************************/
void int_to_string(char *timestamp, unsigned int offset, int i) {
    if (i > 99) {
        timestamp[offset]   = '9';
        timestamp[offset+1] = '9';
        return;
    }

    while (i > 0) {
	    if (i >= 10) {
		    i -= 10;
		    timestamp[offset]++;

	    } else {
		    timestamp[offset+1] = '0' + i;
		    i=0;
	    }
    }
}

/**************************************************************************//**
 * @brief Konverterer 3 tall til en timestamp-string
 * timestamp-argumentet må være et array med plass til (minst) 7 elementer.
 * Det kan deklareres i funksjonen som kaller som "char timestamp[7];"
 * Kallet blir dermed:
 * char timestamp[7];
 * time_to_string(timestamp, h, m, s);
 *****************************************************************************/
void time_to_string(char *timestamp, int h, int m, int s) {
    timestamp[0] = '0';
    timestamp[1] = '0';
    timestamp[2] = '0';
    timestamp[3] = '0';
    timestamp[4] = '0';
    timestamp[5] = '0';
    timestamp[6] = '\0';

    int_to_string(timestamp, 0, h);
    int_to_string(timestamp, 2, m);
    int_to_string(timestamp, 4, s);
}

void add_hour(){
	hours++;
}

void add_minute(){
	minutes++;
	if (minutes == 60){
		minutes = 0;
		add_hour();
	}
}

void add_second(){
	seconds++;
	if (seconds == 60){
		seconds = 0;
		add_minute();
	}
}

void update_display(){
	time_to_string(time, hours, minutes, seconds);
	lcd_write(time);

}

void start_timer(){
	SYSTICK->VAL = FREQUENCY;
	SYSTICK->CTRL |= 0b001;
}

void stop_timer(){
	SYSTICK->CTRL &= ~(0b001);
}

void set_led(int value){
	if (value == 1){
		GPIO->ports[LED_PORT].DOUTSET = 0b0100;
	}
	else{
		GPIO->ports[LED_PORT].DOUTCLR = 0b0100;
	}

}

void GPIO_ODD_IRQHandler(void) { //Pushbutton PB0
	switch (state){
		case SET_SECONDS_STATE:
			add_second();
			update_display();
			break;

		case SET_MINUTES_STATE:
			add_minute();
			update_display();
			break;

		case SET_HOURS_STATE:
			add_hour();
			update_display();
			break;

		case COUNTDOWN_STATE:
			break;

		case ALARM_STATE:
			break;

		default:
			break;
	}
	GPIO->IFC = 1 << BUTTON0_PIN;
}

void GPIO_EVEN_IRQHandler(void) { //Pushbutton PB1
	switch (state){
		case COUNTDOWN_STATE:
			break;

		case ALARM_STATE:
			state = SET_SECONDS_STATE;
			set_led(0);
			break;

		case SET_SECONDS_STATE:
			state++;
			break;

		case SET_MINUTES_STATE:
			state++;
			break;
		case SET_HOURS_STATE:
			start_timer();
			state++;
			break;

		default:
			state++;
	}
	GPIO->IFC = 1 << BUTTON1_PIN;
}

void SysTick_Handler(void) {
	if (state == COUNTDOWN_STATE){
		if(seconds <= 0){
			if (minutes <= 0){
				if (hours <= 0){
					stop_timer();
					set_led(1);
					update_display();
					state = ALARM_STATE;
					return;
				}
				hours--;
				minutes = 60;
			}
			minutes--;
			seconds = 60;
		}
		seconds--;
		update_display();
	}
}

int main(void) {
    init();
    // Skriv din kode her...

	//Setup systick
	SYSTICK = (systick_t*) SYSTICK_BASE;
	SYSTICK->CTRL = 0b110;
	SYSTICK->LOAD = FREQUENCY;

	//Setup GPIO
    GPIO = (gpio_map_t*) GPIO_BASE;
	//First button
    GPIO->ports[BUTTON_PORT].DOUT = 0;
    GPIO->ports[BUTTON_PORT].MODEH = ((~(0b1111 << 4)) & GPIO->ports[BUTTON_PORT].MODEH) | (GPIO_MODE_INPUT << 4);
    GPIO->EXTIPSELH = ((~(0b1111 << 4)) & GPIO->EXTIPSELH) | (0b0001 << 4);
    GPIO->EXTIFALL = GPIO->EXTIFALL | (1 << BUTTON0_PIN);
    GPIO->IEN = GPIO->IEN | (1 << BUTTON0_PIN);
	// Second button
	GPIO->ports[BUTTON_PORT].MODEH = ((~(0b1111 << 8)) & GPIO->ports[BUTTON_PORT].MODEH) | (GPIO_MODE_INPUT << 8);
    GPIO->EXTIPSELH = ((~(0b1111 << 8)) & GPIO->EXTIPSELH) | (0b0001 << 8);
    GPIO->EXTIFALL = GPIO->EXTIFALL | (1 << BUTTON1_PIN);
    GPIO->IEN = GPIO->IEN | (1 << BUTTON1_PIN);

	//LED
	GPIO->ports[LED_PORT].DOUT = 0;
	GPIO->ports[LED_PORT].MODEL = ( (~(0b1111 << 8)) & GPIO->ports[LED_PORT].MODEL ) | (GPIO_MODE_OUTPUT << 8);

	update_display();
	while (true) {
	}

    return 0;
}
