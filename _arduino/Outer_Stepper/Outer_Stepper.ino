/* This example shows basic use of the AMIS-30543 stepper motor
  driver.

  It shows how to initialize the driver, set the current limit, set
  the micro-stepping mode, and enable the driver.  It shows how to
  send pulses to the NXT/STEP pin to get the driver to take steps
  and how to switch directions using the DIR pin.  The DO pin is
  not used and does not need to be connected.

  Before using this example, be sure to change the
  setCurrentMilliamps line to have an appropriate current limit for
  your system.  Also, see this library's documentation for
  information about how to connect the driver:

    http://pololu.github.io/amis-30543-arduino/
*/

#include <SPI.h>
#include <AMIS30543.h>
#define STEPS_PER_OUTPUT_REVOLUTION 400
#define COMMANDSIZE 2

const uint8_t amisStepPin = 5;
const uint8_t amisDirPin = 6;
const uint8_t amisSlaveSelect = 7;

int micro = 128;
int RPM = 0;
int wait = 320;
int currentLimit = 400;
int dir = 0;
int pulseWidth = 2;

boolean sysRunning = false;

int commands[COMMANDSIZE];
String serialResponse = "";

boolean newCommand = false;
char sz[] = "0~000~000~000~000~000";
AMIS30543 stepper;

void setup()
{
  Serial.begin(19200);
  Serial.setTimeout(5);

  SPI.begin();
  stepper.init(amisSlaveSelect);

  // Drive the NXT/STEP and DIR pins low initially.
  digitalWrite(amisStepPin, LOW);
  pinMode(amisStepPin, OUTPUT);
  digitalWrite(amisDirPin, LOW);
  pinMode(amisDirPin, OUTPUT);

  // Give the driver some time to power up.
  delay(1);
  // Reset the driver to its default settings.
  stepper.resetSettings();

  // Set the current limit.  You should change the number here to
  // an appropriate value for your particular system.
  stepper.setCurrentMilliamps(currentLimit);

  // Set the number of microsteps that correspond to one full step.
  stepper.setStepMode(128);
}

void loop()
{

  if (Serial.available()) {
    readInput();

    if (commands[0] == 0)
    {
      if (!sysRunning)
      {
        stepper.enableDriver();
        setDirection(dir);
      }
      else
        stepper.disableDriver();
      sysRunning = !sysRunning;
    }

    if (commands[0] == 1)
      updateRPM();

    else if (commands[0] == 2)
      updateDir();

    else if (commands[0] == 3)
    {
      stepper.setCurrentMilliamps(currentLimit + commands[1]);
      pulseWidth = commands[2];
      wait = commands[3];
      stepper.setStepMode(commands[4]);
    }



  }

  step();


}

void readInput()
{
  clearCommands();
  int current = 0;


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

// Sends a pulse on the NXT/STEP pin to tell the driver to take
// one step, and also delays to control the speed of the motor.
void step()
{
  // The NXT/STEP minimum high pulse width is 2 microseconds.
  digitalWrite(amisStepPin, HIGH);
  delayMicroseconds(pulseWidth);
  digitalWrite(amisStepPin, LOW);
  delayMicroseconds(pulseWidth);

  // The delay here controls the stepper motor's speed.  You can
  // increase the delay to make the stepper motor go slower.  If
  // you decrease the delay, the stepper motor will go fast, but
  // there is a limit to how fast it can go before it starts
  // missing steps.
  delayMicroseconds(wait - 8);
}

// Writes a high or low value to the direction pin to specify
// what direction to turn the motor.
void setDirection(bool dir)
{
  // The NXT/STEP pin must not change for at least 0.5
  // microseconds before and after changing the DIR pin.
  delayMicroseconds(1);
  digitalWrite(amisDirPin, dir);
  delayMicroseconds(1);
}

void updateRPM()
{
  RPM = commands[1];
  wait = int(60 / (0.0004 * micro * RPM));
}

void updateDir()
{
  setDirection(commands[1]);
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
