#include "Arduino.h"
#include <Adafruit_NeoPixel.h>
#define PIN 8
#define NUM_LEDS 30
#define BRIGHTNESS 50
#define QUARTER NUM_LEDS/4
#define COMMANDSIZE 7


int serial_CMD;
boolean IR = false;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRBW + NEO_KHZ800);
#include <SoftwareSerial.h>

int commands[COMMANDSIZE];
String serialResponse = "";

boolean newCommand = false;
char sz[] = "0~000~000~000~000~000~000";

SoftwareSerial innerSerial(4, 5); // RX, TX
SoftwareSerial outterSerial(6, 7); // RX, TX

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(5);

  pinMode(10, OUTPUT);
  digitalWrite(10, HIGH);

  pinMode(10, OUTPUT);
  digitalWrite(10, HIGH);

  outterSerial.begin(19200);
  innerSerial.begin(38400);

  strip.setBrightness(BRIGHTNESS);
  strip.begin();
  strip.show();

  colorWipe(strip.Color(100, 50, 50, 50), 3);
  colorWipe(strip.Color(50, 100, 50, 50), 3);
  colorWipe(strip.Color(50, 50, 100, 50), 3);
  colorWipe(strip.Color(50, 50, 50, 100), 3);
  colorWipe(strip.Color(0, 0, 0, 0), 1);
}

void loop() {
  readInput();

  if (newCommand)
  {
    if (commands[0] == 1)
      stripUpdate();
    else if (commands[0] == 2)
      brightnessUpdate();
    else if (commands[0] == 3)
      digitalWrite(10, LOW);
    else if (commands[0] == 4)
      digitalWrite(10, HIGH);
    else if (commands[0] == 5)
    {
      
      String temp = String(commands[1]);
      Serial.print("1~" + temp);
      outterSerial.print("1~" + temp);
    }
    else if (commands[0] == 6)
    {
      
      String temp = String(commands[1]);
      Serial.print("1~" + temp);
      innerSerial.print("1~" + temp);
    }
    newCommand = false;

  }

  //  if (serial_CMD == 53)
  //  {
  //    digitalWrite(2, HIGH);
  //  }
  //
  //  if (serial_CMD == 54)
  //  {
  //    digitalWrite(2, LOW);
  //  }
  //
  //  if (serial_CMD == 55)
  //  {
  //
  //    Serial.println("sent");
  //  }
  //  outterSerial.write("13");
  //  delay(1000);

}


void readInput()
{
  int current = 0;
  if ( Serial.available()) {
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
}

void stripUpdate() {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    if (i >= commands[1] && i < commands[2]) {
      strip.setPixelColor(i, commands[3], commands[4], commands[5], commands[6]);
    }
    strip.show();
  }
}

void stripReset() {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, 0, 0, 0);
  }
  strip.show();
}

void brightnessUpdate() {
  strip.setBrightness(commands[1]);
  strip.show();
}

void colorWipe(uint32_t c, uint8_t wait) {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
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
