#include <Wire.h>

//Slave Address for the Communication
#define SLAVE_ADDRESS 0x08
#define COMMANDSIZE 2

char number[50];
String CMD = "";
char sz[] = "0~000~000~000~000~000";
int commands[COMMANDSIZE];

//Code Initialization
void setup() {
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
}

void loop() {
  delay(1000);
  if (CMD != NULL)
  {
    readCMD();
    printCMD();
    CMD = "";
     Serial.println("called");
  }

}

void readCMD()
{
  int current = 0;
  clearCMD();

  char buf[sizeof(sz)];
  CMD.toCharArray(buf, sizeof(buf));
  char *p = buf;
  char *str;
  while ((str = strtok_r(p, "~", &p)) != NULL)
  {
    int temp;
    temp = atoi(str);
    commands[current] = temp;
    current++;
  }
  
}

void clearCMD()
{
  for (int i = 0; i < COMMANDSIZE; i++)
  {
    commands[i] = 0;
  }
}

void printCMD()
{
  for (int i = 0; i < COMMANDSIZE; i++)
  {
    Serial.println(commands[i]);
  }
}

void receiveData(int byteCount) {
  int i = 0;
  while (Wire.available()) {
    number[i] = Wire.read();
    CMD += number[i];
    i++;
  }
  number[i] = '\0';
}

