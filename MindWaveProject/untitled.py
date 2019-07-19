//Processing code to graph Attention values
//Comment out all of the lines after “if(brainwave && attention > 0 && attention < 100) {“
//Except for   
//mySerial.print(attention, DEC);
// mySerial.println();
//This will print out ONLY an Attention value and a new line afterwards

// Graphing sketch by Tom Igoe
// Sophi Kravitz edit 11/8

 import processing.serial.*; 
 Serial myPort;        // The serial port
 int xPos = 1;         // horizontal position of the graph 
 void setup () {
 // set the window size:
 size(400, 300);   
String portName = Serial.list()[1];         //[1]  println(Serial.list()) to find the ports 
 myPort = new Serial(this, "COM16", 4800);  // make sure the Baud rate matches the Arduino code
 myPort.bufferUntil('\n');                  // Wait for newline character:
 background(0);                             // set inital background color: 0 = black, 255 = white
 }

void draw () {                              // everything happens in the serialEvent()
 }

 void serialEvent (Serial myPort) {
 String inString = myPort.readStringUntil('\n');

   if (inString != null) {                  // trim whitespace:
   inString = trim(inString);               // convert to an int and map to the screen height:
   float inByte = float(inString); 
   inByte = map(inByte, 0, 100, 0, height); // take number from 0 to 100, and map it to 0 to height
   stroke(5,34,255);                        // draw the line:
   line(xPos, height, xPos, height - inByte);

   if (xPos >= width) {                     // at the edge of the screen, go back to the beginning:
   xPos = 0;
   background(0); 
   } 
   else { 
   xPos++;                                  // increment the horizontal position:
   }
 }
 }





