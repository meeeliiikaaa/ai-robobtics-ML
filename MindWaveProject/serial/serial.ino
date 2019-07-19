//hit Enter after typing AT

#include <SoftwareSerial.h>
#define rxPin 10
#define txPin 11
SoftwareSerial mySerial(rxPin, txPin); // RX, TX
char myChar ;
void setup() {
  Serial.begin(9600); 
  Serial.println("AT");
  mySerial.begin(38400);
  mySerial.println("AT");
}
void loop() {
  while (mySerial.available()) {
    myChar = mySerial.read();
    Serial.print(myChar);
  }
 while (Serial.available()) {
    myChar = Serial.read();
    Serial.print(myChar); //echo
    mySerial.print(myChar);
  }
}
