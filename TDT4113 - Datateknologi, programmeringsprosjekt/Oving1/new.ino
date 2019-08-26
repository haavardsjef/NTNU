const int ledGreen = 2;
const int ledRed = 4;
const int buttonPin = 11;

int buttonState = 0;
int dash = 0;
unsigned long pauseTimer = 0;
unsigned long startTime = 0;
int T = 200; // 200ms

void setup() {
    Serial.begin(9600);
    pinMode(ledGreen, OUTPUT);
    pinMode(ledRed, OUTPUT);
    pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
    delay(10);
    // Check if button is being pressed and act accordingly
    if (digitalRead(buttonPin) == LOW){
        if (buttonState == false){ // New press
            pauseTimer = millis()-pauseTimer; // Keeps track of how long since last pres
            if(pauseTimer >= 5*T && pauseTimer < 10*T){ // Symbol pause
                Serial.print(2);
            }
            else if(pauseTimer >= 10*T){ // Word pause.
                Serial.print(3);
            }
            buttonState = true;
            digitalWrite(ledRed, HIGH);
            startTime = millis();
        }

        if (millis()-startTime >= 3*T && dash == false){
            dash = true;
            digitalWrite(ledRed, LOW);
            digitalWrite(ledGreen, HIGH);
        }
    }
    else{
        if(buttonState == true){
            buttonState = false;
            pauseTimer = millis();
            if (dash == true){
                dash = false;
                digitalWrite(ledGreen, LOW);
                Serial.print(1);

            }
            else{
                digitalWrite(ledRed, LOW);
                Serial.print(0);
            }
        }
    }
}
