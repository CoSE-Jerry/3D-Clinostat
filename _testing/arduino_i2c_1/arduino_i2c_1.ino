/*
  I2C Pinouts

  SDA -> A4
  SCL -> A5
*/

//Import the library required
#include <Wire.h>

//Slave Address for the Communication
#define SLAVE_ADDRESS 0x08

char data[50];
int commands[5];
boolean newCommand = false;


//Code Initialization
void setup() {
  // initialize i2c as slave
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  //  Wire.onRequest(sendData);
}

void loop() {
  delay(100);
  if (newCommand)
  { processCMD();
    printCMD();
    newCommand = false;
  }
} // end loop

// callback for received data
void receiveData(int byteCount) {
  int i = 0;
  while (Wire.available()) {
    data[i] = Wire.read();
    i++;
  }
  data[i] = '\0';
  Serial.println(data);
  newCommand = true;
}

void processCMD() {
  int current = 0;
  char *p = data;
  char *str;
  while ((str = strtok_r(p, "~", &p)) != NULL)
  {
    int temp;
    temp = atoi(str);
    commands[current] = temp;
    current++;
  }


}

void printCMD() {
  for (int i = 0; i < 4; i++)
  { 
    Serial.println(commands[i]);
  }

}
