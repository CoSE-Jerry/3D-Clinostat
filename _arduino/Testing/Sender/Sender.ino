#include <SoftwareSerial.h>
SoftwareSerial mySerial(5, 6);// RX, TX

void setup() {
  // Begin the Serial at 9600 Baud
  Serial.begin(9600);

  mySerial.begin(19200);
}

void loop() {
  mySerial.write("Hello");
  delay(2000);
  
  Serial.write("test"); //Write the serial data
  delay(2000);
}
