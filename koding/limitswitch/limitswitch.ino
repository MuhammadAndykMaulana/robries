int ls1=10;
int ls2=11;
void setup() {
  // put your setup code here, to run once:
  pinMode(ls1,INPUT);
  pinMode(ls2,INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(ls1)==LOW)
  {
    Serial.print("Tombol ls1 ditekan");
    delay(1000);
  }
  if (digitalRead(ls2)==LOW)
  {
    Serial.print("Tombol ls2 ditekan");
    delay(1000);
  }
  Serial.println("");
//  delay(500);
  
}
