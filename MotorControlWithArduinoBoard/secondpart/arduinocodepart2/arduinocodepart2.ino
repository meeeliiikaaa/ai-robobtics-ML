#include<SoftwareSerial.h>
const int EN1 = 9;
const int buttonPin = 8;
int buttonSituation = 0;

const int IN1 = 11 ;
const int IN2 = 10;
   
const int encoder0PinA=2;

long period=0;
unsigned long t1;
unsigned long t0 = 0;
int cnt=0;
int rpm;
long p=0;



void setup() 

  {
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(buttonPin, INPUT);
    pinMode(encoder0PinA, INPUT);
    attachInterrupt (0, ISRHandler , RISING);
    Serial.begin (9600);
    
  
}

void loop() {



   
    int Gvalue = analogRead(A3);
    int output= map(Gvalue, 0 , 1023 , 0 , 255);
    analogWrite( EN1 , output);

    
    //clockwise rotation
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);


    //anticlockwise rotation if the button is pressed by digitalRead
    buttonSituation = digitalRead(buttonPin);
     if (buttonSituation == HIGH) {
      digitalWrite(IN2, LOW);
      digitalWrite(IN1, HIGH);
      }
      
Serial.print("speed= ");
p=24*period;
rpm=60000/p;
Serial.println(rpm);



}
void ISRHandler ()
{
  t1= millis();
  period = t1 - t0;
  t0=t1;
}
