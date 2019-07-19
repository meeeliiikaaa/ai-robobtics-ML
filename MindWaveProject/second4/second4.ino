boolean check;
boolean start;
unsigned int angle = 5;   //angle moved per encoder tick
unsigned long volatile time1;
unsigned long volatile time_11;
unsigned long interrupt_time;

void setup() {
  Serial.begin(9600);
  while (!Serial) ;
  pinMode(21, INPUT);  //Pin#21=interrupt pin, matched to interrupt#2
  attachInterrupt(digitalPinToInterrupt(2), speed, FALLING);
  time1 = 0;
  time_11 = 0;
  interrupt_time = 0;
  check = true;
  start = false;
  time_11 = millis(); //Start Clock
}

void loop() {
  if(time1 == interrupt_time && start) //Both times same , hence bool start.
  {
    if(check)
    {
      Serial.print(millis());  //Time taken to rise to steady speed.
      check = false;
    }
    Serial.println((angle/time1)*1000);   //Display Speed.
  }
  interrupt_time = time1;
  start = false;
  while(!start)
    {}
}
void speed(void) {
  start = true;
  time1 = millis()-time_11;
  time_11 = millis();
}
