//                                                           //
//                                                         //
//    Program       : Brainsense with Arduino              //
//    Interfacing   : HC-05 Bluetooth module               //
//    Output        : LED Control using Attention          //

#define BAUDRATE 57600
#define LED 13

byte payloadData[32] = {0};
byte Attention[5]={0};
byte checksum=0;
byte generatedchecksum=0;
int  Plength,Temp;
int  Att_Avg=0,On_Flag=1,Off_Flag=0;
int  k=0;
signed int  j=0;


void setup() 
{
  Serial.begin(BAUDRATE);           // USB
  pinMode(LED, OUTPUT);
}

byte ReadOneByte()           // One Byte Read Function
{
  int ByteRead;
  while(!Serial.available());
  ByteRead = Serial.read();
  return ByteRead;
}

void loop()                     // Main Function
{
  while (1)
  {
    if(ReadOneByte() == 170)        // AA 1 st Sync data
    {
      if(ReadOneByte() == 170)      // AA 2 st Sync data
      {
        Plength = ReadOneByte();
        if(Plength == 32)   // Big Packet
        { 
          generatedchecksum = 0;
          for(int i = 0; i < Plength; i++) 
          {  
            payloadData[i]     = ReadOneByte();      //Read payload into memory
            generatedchecksum  += payloadData[i] ;
          }
          generatedchecksum = 255 - generatedchecksum;
          checksum  = ReadOneByte();
        
          if(checksum == generatedchecksum)        // Varify Checksum
          {             
            if (payloadData[28]==4)
            { 
              if (j<4)
               {
                 Attention [k] = payloadData[29];
                 Temp += Attention [k];
                 j++;
               }
               else
               {
                 Att_Avg = Temp/4;
                 
                 if (Att_Avg>80)
                 {
                   if(On_Flag==1)
                   {
                     digitalWrite(LED, HIGH);
                     On_Flag=0;
                     Off_Flag=1;
                   }
                   else if(Off_Flag==1)
                   {
                     digitalWrite(LED, LOW);
                     On_Flag=1;
                     Off_Flag=0;
                   }
                 }
                 j=0;
                 Temp=0;
               }
            }
           } 
         }
       }
     }         
   } 
}
