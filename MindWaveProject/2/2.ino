#include<SoftwareSerial.h>

const int EN1 = 9;
const int buttonPin = 8;
int buttonState = 0;

const int IN1 = 11 ;
const int IN2 = 10;

const int encoder0PinA=2;

long duration=0;
unsigned long newtime;
unsigned long oldtime = 0;
int cnt=0;
int rpm;
long d=0;

void setup() {
  // put your setup code here, to run once:
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(buttonPin, INPUT);
    pinMode(encoder0PinA, INPUT);
    attachInterrupt(0, doEncoder, RISING);  // encoDER ON PIN 2
    Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println("start11");


    //
    int GaugeValue = analogRead(A3);
    int outputValue= map(GaugeValue, 0 , 1023 , 0 , 255);
    analogWrite( EN1 , outputValue);

    
    //setting the initial values of IN1 and IN2 for clockwise rotation
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);


    //checking if the button is pressed, and if it was pressed then we will change the value of IN1 and IN2 to rotate anticlockwise
    buttonState = digitalRead(buttonPin);
     if (buttonState == HIGH) {
      digitalWrite(IN2, LOW);
      digitalWrite(IN1, HIGH);
      }

     //
     //Serial.println("start");
     d=24*duration;
     rpm=60000/d;
     Serial.println(rpm);

}
void doEncoder() {
  newtime=millis();
  duration=newtime-oldtime;
  oldtime=newtime;
 
  }
