int potPin = A1;    // select the input pin for the potentiometer
//int ledPin = 13/;   // select the pin for the LED
int val = 0;       // variable to store the value coming from the sensor
int en=7;

void setup() {
    Serial.begin(9600);
    pinMode(en, OUTPUT);
}

void loop() {
  val = analogRead(potPin);    // read the value from the sensor
//////  digitalWrite(ledPin, HIGH);  // turn the ledPin on
  delay(val);                  // stop the program for some time
  Serial.println(val);
  analogWrite(en,val);
}
 
