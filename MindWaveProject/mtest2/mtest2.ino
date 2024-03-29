///////////////////////////////////////////////////////////////
// Arduino Bluetooth Interface with Mindwave
// Sophi Kravitz edit 11-4
// Shane Clements edit 11-5
//////////////////////////////////////////////////////////////////////// 
#include <SoftwareSerial.h>     // library for software serial
SoftwareSerial mySerial(5, 6);  // RX, TX
int LED = 8;                    // yellow one
int LED1 = 3;                   //white one
int BAUDRATE = 57600;

// checksum variables
byte payloadChecksum = 0;
byte CalculatedChecksum;
byte checksum = 0;              //data type byte stores an 8-bit unsigned number, from 0 to 255
int payloadLength = 0;
byte payloadData[64] = {0};
byte poorQuality = 0;
byte attention = 0;
byte meditation = 0;

// system variables
long lastReceivedPacket = 0;
boolean bigPacket = false;
boolean brainwave = false;
void setup() {
  pinMode(LED, OUTPUT);
  pinMode(LED1, OUTPUT);
  digitalWrite(LED, HIGH);   // hello sequence
  delay(100);
  digitalWrite(LED, LOW);
  delay(100);
  Serial.begin(57600);       // Bluetooth
  delay(500);
  mySerial.begin(4800);      // software serial
  delay(500);
  mySerial.print("Communicating... ");
  mySerial.println();
}
byte ReadOneByte() {
   int ByteRead;
  // Wait until there is data
  while(!Serial.available());
  //Get the number of bytes (characters) available for reading from the serial port.
  //This is data that's already arrived and stored in the serial receive buffer (which holds 64 bytes)
  ByteRead = Serial.read();
  return ByteRead; // read incoming serial data
  }

unsigned int delta_wave = 0;
unsigned int theta_wave = 0;
unsigned int low_alpha_wave = 0;
unsigned int high_alpha_wave = 0;
unsigned int low_beta_wave = 0;
unsigned int high_beta_wave = 0;
unsigned int low_gamma_wave = 0;
unsigned int mid_gamma_wave = 0;

void read_waves(int i) {
  delta_wave = read_3byte_int(i);
  i+=3;
  theta_wave = read_3byte_int(i);
  i+=3;
  low_alpha_wave = read_3byte_int(i);
  i+=3;
  high_alpha_wave = read_3byte_int(i);
  i+=3;
  low_beta_wave = read_3byte_int(i);
  i+=3;
  high_beta_wave = read_3byte_int(i);
  i+=3;
  low_gamma_wave = read_3byte_int(i);
  i+=3;
  mid_gamma_wave = read_3byte_int(i);
}

int read_3byte_int(int i) {
  return ((payloadData[i] << 16) + (payloadData[i+1] << 8) + payloadData[i+2]);
}

void loop() {
  // Look for sync bytes
  // Byte order: 0xAA, 0xAA, payloadLength, payloadData,
  // Checksum (sum all the bytes of payload, take lowest 8 bits, then bit inverse on lowest
if(ReadOneByte() == 0xAA) {
if(ReadOneByte() == 0xAA) {
payloadLength = ReadOneByte();
if(payloadLength > 169) //Payload length can not be greater than 169
return;
payloadChecksum = 0;
      for(int i = 0; i < payloadLength; i++) {      //loop until payload length is complete
        payloadData[i] = ReadOneByte();             //Read payload
        payloadChecksum += payloadData[i];
      }
      checksum = ReadOneByte();                     //Read checksum byte from stream
      payloadChecksum = 255 - payloadChecksum;      //Take one’s compliment of generated checksum
      if(checksum == payloadChecksum) {
        poorQuality = 200;
        attention = 0;
        meditation = 0;
 }
     brainwave = false;
     for(int i = 0; i < payloadLength; i++) { // Parse the payload
          switch (payloadData[i]) {
          case 02:
            i++;
            poorQuality = payloadData[i];
            bigPacket = true;
            break;
          case 04:
            i++;
            attention = payloadData[i];
            break;
          case 05:
            i++;
            meditation = payloadData[i];
            break;
          case 0x80:
            i = i + 3;
            break;
          case 0x83:                         // ASIC EEG POWER INT
            i++;
            brainwave = true;
            byte vlen = payloadData[i];
            //mySerial.print(vlen, DEC);
            //mySerial.println();
            read_waves(i+1);
            i += vlen; // i = i + vlen
            break;
          }                                 // switch
        }                                   // for loop

        if(bigPacket) {
          if(poorQuality == 0){
          }
          else{                             // do nothing
           }
         }


            if(brainwave && attention > 0 && attention < 100) {
            mySerial.print("Attention value is: ");
            mySerial.print(attention, DEC);
            mySerial.println();
            mySerial.print("Delta value is: ");
            mySerial.print(delta_wave, DEC);
            mySerial.println();
            mySerial.print("Theta value is: ");
            mySerial.print(theta_wave, DEC);
      mySerial.println();
            mySerial.print("Low Alpha value is: ");
            mySerial.print(low_alpha_wave, DEC);
            mySerial.println();
            mySerial.print("High Alpha value is: ");
            mySerial.print(high_alpha_wave, DEC);
            mySerial.println();            
            mySerial.print("Alertness value1 is: ");
            mySerial.print(low_beta_wave, DEC);
            mySerial.println();
            mySerial.print("Alertness value2 is: ");
            mySerial.print(high_beta_wave, DEC);
            mySerial.println();           
            mySerial.print(low_gamma_wave, DEC);
            mySerial.println();
            mySerial.print(mid_gamma_wave, DEC);
            mySerial.println();
         }

          if(attention > 40){
            digitalWrite(LED1, HIGH);
          }
          else
            digitalWrite(LED1, LOW);
        } 
        }
      }
