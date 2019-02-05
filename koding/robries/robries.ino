//Motor pengarah kanan kiri
int en1 = 6;
int motor1M = 7;  // pin  on L29D untuk maju
int motor1m = 8;  // pin  on L298D u/ mundur
int en2 = 3;   // en motor 2 penggulung
int V1=0,V2=0; // variable to store the value coming from the sensor
int V=0;
int Vkal=200;
int pot1=A1;
//int pot2=A1;
int ls1=10;
int ls2=11;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(en1, OUTPUT);
  pinMode(motor1M, OUTPUT);
  pinMode(motor1m, OUTPUT);
  pinMode(ls1,INPUT);
  pinMode(ls2,INPUT);
  pinMode(en2, OUTPUT);
  kalibrasi_motor();
}

void loop() {
  // put your main code here, to run repeatedly:
    V1=analogRead(pot1);
    V=V1/3;
    analogWrite(en2,V1);
    Serial.println(V1);
    if (!digitalRead(ls1))
    {
      digitalWrite(motor1m, LOW);
      digitalWrite(motor1M, HIGH);
      analogWrite(en1,V);
      Serial.println("Tombol ls 1 ditekan");
    } 
    if (!digitalRead(ls2))
    {
      digitalWrite(motor1m, HIGH);
      digitalWrite(motor1M, LOW);
      analogWrite(en1,V);
      Serial.println("Tombol ls 2 ditekan");
    }  
}
void kalibrasi_motor()
{
    while (digitalRead(ls1))
    { 
      analogWrite(en1,Vkal);
      Serial.println("Kalibrasi menuju ls1");
      digitalWrite(motor1m, HIGH);
      digitalWrite(motor1M, LOW);
    }
    Serial.println("kalibrasi selesai, motor berhenti!.");
}
