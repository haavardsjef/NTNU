#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT); // Bil Grønn
  pinMode(12, OUTPUT); // Bil Gul
  pinMode(11, OUTPUT); // Bil Rød

  pinMode(9, OUTPUT); // Fotgjenger Grønn
  pinMode(8, OUTPUT);// Fotgjenger Rødt
  pinMode(7, INPUT); // KNAPP

   myservo.attach(3);  // attaches the servo on pin 3 to the servo object
  

}



void loop() {
  // put your main code here, to run repeatedly:
  myservo.write(90);
  digitalWrite(13, HIGH);
  digitalWrite(12, LOW);
  digitalWrite(11, LOW);
  digitalWrite(9, LOW);
  digitalWrite(8, HIGH);
  if (digitalRead(7) == HIGH){
      delay(1000);
      digitalWrite(13, LOW);  // GRØNT LYS AV
      digitalWrite(12, HIGH); //GULT LYS PÅ
      delay(1000);
      digitalWrite(11, HIGH); //RØDT LYS PÅ
      digitalWrite(12, LOW);  //GULT LYS AV
      delay(2000);
      digitalWrite(9, HIGH);  //FOTGJENGER GRØNT
      digitalWrite(8, LOW);
      myservo.write(180);
      delay(5000);
      digitalWrite(9, LOW);   // FOTGJENGER RØDT
      digitalWrite(8, HIGH);
      myservo.write(90);
      delay(2000);
      digitalWrite(12, HIGH); // GULT LYS PÅ
      delay(1000);
  }

  
  

}
