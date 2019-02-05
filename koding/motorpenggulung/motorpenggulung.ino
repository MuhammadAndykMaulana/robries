//Motor penggulung
int en1 = 3;   // en motor 1
//int motor1M = 3;  // pin  on L29D untuk maju
//int motor1m = 4;  // pin  on L298D u/ mundur
//char chrV[5];
int pot=A1;
int V=255;  

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
//  Serial.println("kec4 = 255 // hecepatan 100% nilai 255");
//  Serial.println("kec3 = 191 // Kecepatan 75% nilai 191");
//  Serial.println("kec2 = 127 // Kecepatan 50% nilai 127");
//  Serial.println("int kec1 = 64 // Kecepatan 25% nilai 64");
  pinMode(en1, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    //default arah motor penggulung CCW
//    digitalWrite(motor1m, HIGH);
//    digitalWrite(motor1M, LOW);
//    V=analogRead(pot);
    while(V<256)
    {
      Serial.println(V);
      analogWrite(en1,V);
//      digitalWrite(motor1m, LOW);
//      digitalWrite(motor1M, HIGH);
    }
//    delay(10000);
//    V=100;
//    //default arah motor penggulung CCW

//    analogWrite(en1,V);
//    delay(5000);
}
