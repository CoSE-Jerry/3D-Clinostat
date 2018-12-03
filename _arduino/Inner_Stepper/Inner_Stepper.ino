#include <Arduino.h>

// Motor steps per revolution. Most steppers are 200 steps or 1.8 degrees/step
#define MOTOR_STEPS 400
#define COMMANDSIZE 2

#define DIR 8
#define STEP 9
#define ENABLE 13 // optional (just delete ENABLE from everywhere if not used)

#include "DRV8825.h"
#define MODE0 10
#define MODE1 11
#define MODE2 12
DRV8825 stepper(MOTOR_STEPS, DIR, STEP, ENABLE, MODE0, MODE1, MODE2);

int RPM = 3;
int wait = 320;
int dir = 1;

int commands[COMMANDSIZE];
String serialResponse = "";

boolean newCommand = false;
char sz[] = "0~000";

void setup() {

  Serial.begin(38400);
  Serial.setTimeout(5);
  stepper.begin(RPM);
  stepper.enable();
  stepper.setMicrostep(32);
}

void loop() {



  if ( Serial.available()) {
    readInput();
    if (commands[0] == 1)
      updates();
    if (commands[0] == 2)
      updateDir();
  }
  delayMicroseconds(wait-8);
  stepper.move(dir*1);
}

void readInput()
{
  int current = 0;

  clearCommands();
  newCommand = true;
  serialResponse = Serial.readStringUntil('\r\n');

  // Convert from String Object to String.
  char buf[sizeof(sz)];
  serialResponse.toCharArray(buf, sizeof(buf));
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

void updates()
{
  RPM = commands[1];
  wait = 60 / (0.0512 * RPM);
}

void updateDir()
{
  dir = commands[1];
}

void printCommands() {
  for (int i = 0; i < COMMANDSIZE; i++)
  {
    Serial.println(commands[i]);
  }
}

void clearCommands() {
  for (int i = 0; i < COMMANDSIZE; i++)
  {
    commands[i] = 0;
  }
}
