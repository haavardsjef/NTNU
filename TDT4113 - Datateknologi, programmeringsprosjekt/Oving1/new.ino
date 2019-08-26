const int ledGreen = 2;
const int ledRed = 4;
const int buttonPin = 12;

int buttonState = 0;
int dash = 0;
unsigned long pauseTime = 0;
unsigned long timePressed = 0;
unsigned long startTime = 0;

int T = 200;

void setup() {
    Serial.begin(9600);
    pinMode(ledGreen, OUTPUT);
    pinMode(ledRed, OUTPUT);
    pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
    // Check if button is being pressed and act accordingly
    if (digitalRead(buttonPin) == LOW){
        if (buttonState == false){
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
            if (dash == true){
                dash = false;
                digitalWrite(ledGreen, LOW);
                Serial.print("-");

            }
            else{
                digitalWrite(ledRed, LOW);
                Serial.print("*");
            }
            buttonState = false;
        }
    }
}
