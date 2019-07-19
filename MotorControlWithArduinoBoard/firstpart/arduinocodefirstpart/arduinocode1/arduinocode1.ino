
const int EN1 = 9;
const int buttonPin = 8;
int buttonSituation = 0;

const int IN1 = 11 ;
const int IN2 = 10;
   



void setup() 

  {
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(buttonPin, INPUT);
 
    
  
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
}
