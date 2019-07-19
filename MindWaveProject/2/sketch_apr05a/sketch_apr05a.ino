
unsigned long duration;
volatile unsigned int pulseCount = 0;
int cnt=0;
void setup()
{
 Serial.begin(9600);
 pinMode(2, INPUT);
 attachInterrupt(0, encoderPulseInterrupt, RISING);
}

void loop()
{
 duration =  pulseIn(2, LOW);

 Serial.print(cnt++);
 Serial.print(',');
 Serial.print(pulseCount);
 Serial.print(',');
 Serial.print(millis());
 Serial.print(',');
 Serial.println(duration);
}

void encoderPulseInterrupt()
{
 pulseCount++;  
}
