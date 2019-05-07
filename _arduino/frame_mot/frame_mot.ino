//Import the library required
#include <Wire.h>
#include <SPI.h>
#include <AMIS30543.h>

//Slave Address for the Communication
#define SLAVE_ADDRESS 0x09
#define COMMANDSIZE 5

const uint8_t amisStepPin = 8;
const uint8_t amisDirPin = 9;
const uint8_t amisSlaveSelect = 10;
AMIS30543 stepper;

char data[50];
int commands[COMMANDSIZE];

int microStep = 128;
int RPM = 3;
int wait = 300;
int currentLimit = 300;
int dir = 0;
int pulseWidth = 2;
boolean sysRunning = false;


//Code Initialization
void setup() {
  SPI.begin();
  stepper.init(amisSlaveSelect);

  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);

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
  stepper.setStepMode(microStep);

}

void loop() {
  step();
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
  delayMicroseconds(wait);
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

// callback for received data
void receiveData(int byteCount) {
  int i = 0;
  if (Wire.read() == '^')
  {
    while (Wire.available()) {
      data[i] = Wire.read();
      i++;
    }
    data[i] = '\0';
    Serial.println(data);
    processCMD();
    exeCMD();
  }
}  // end while

void processCMD() {
  clearCMD();
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

void clearCMD() {
  for (int i = 0; i < COMMANDSIZE; i++)
  {
    commands[i] = 0;
  }
}

void exeCMD() {
  if (commands[0] == 1)
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

  if (commands[0] == 2)
  {
    wait = commands[1] - 11;
  }

  if (commands[0] == 3)
  {
    dir = commands[1];
    setDirection(dir);
  }
  if (commands[0] == 4)
  {
    stepper.enableDriver();
  }
  if (commands[0] == 5)
  {
    stepper.disableDriver();
  }
}
