
  int speaker = 3;
  int C = 5;
  int D = 7;
  int E = 9;
  int F = 11;
  
  float C_4 = 261.63;
  float D_4 = 293.66;
  float E_4 = 329.63;
  float F_4 = 349.23;

void setup() {
  // put your setup code here, to run once:
  pinMode(C, INPUT_PULLUP);
  pinMode(D, INPUT_PULLUP);
  pinMode(E, INPUT_PULLUP);
  pinMode(F, INPUT_PULLUP);
  pinMode(speaker, OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(C) == LOW){
    tone(speaker, C_4); 
  }
  if (digitalRead(D) == LOW){
    tone(speaker, D_4); 
  }
  if (digitalRead(E) == LOW){
    tone(speaker, E_4); 
  }
  if (digitalRead(F) == LOW){
    tone(speaker, F_4); 
  }
  noTone(speaker);
}
