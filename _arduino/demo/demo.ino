#include "Arduino.h"
#include <Adafruit_NeoPixel.h>
#define PIN 8
#define NUM_LEDS 30
#define BRIGHTNESS 50
#define QUARTER NUM_LEDS/4
#define COMMANDSIZE 7

const int c = 261;
const int d = 294;
const int e = 329;
const int f = 349;
const int g = 391;
const int gS = 415;
const int a = 440;
const int aS = 455;
const int b = 466;
const int cH = 523;
const int cSH = 554;
const int dH = 587;
const int dSH = 622;
const int eH = 659;
const int fH = 698;
const int fSH = 740;
const int gH = 784;
const int gSH = 830;
const int aH = 880;

const int buzzerPin = 3;
const int ledPin1 = 12;
const int ledPin2 = 13;

int counter = 0;


int serial_CMD;
boolean IR = false;
boolean FAN = true;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRBW + NEO_KHZ800);
#include <SoftwareSerial.h>

int commands[COMMANDSIZE];
String serialResponse = "";

boolean newCommand = false;
char sz[] = "0~000~000~000~000~000~000";

SoftwareSerial innerSerial(4, 5); // RX, TX
SoftwareSerial outterSerial(6, 7); // RX, TX

void setup() {

  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);

  Serial.begin(9600);
  Serial.setTimeout(5);

  pinMode(10, OUTPUT);
  digitalWrite(10, HIGH);

  pinMode(9, OUTPUT);
  digitalWrite(9, LOW);

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

    Serial.print(commands[0]);
    if (commands[0] == 1)
      stripUpdate();
    else if (commands[0] == 2)
      brightnessUpdate();

    else if (commands[0] == 3)
      firstSection();

    else if (commands[0] == 4)
      secondSection();

    else if (commands[0] == 5)
    {
      if (!IR)
      {
        digitalWrite(10, LOW);
      }
      else
      {
        digitalWrite(10, HIGH);
      }
      IR = !IR;
    }


    else if (commands[0] == 6)
    {
      if (!FAN)
      {
        digitalWrite(9, LOW);
      }
      else
      {
        digitalWrite(9, HIGH);
      }
      FAN = !FAN;
    }


    else if (commands[0] == 7)
    {
      String temp = String(commands[1]);
      Serial.print(String(commands[1]) + "~" + String(commands[2]) + "~" + String(commands[3]) + "~" + String(commands[4]) + "~" + String(commands[5])+ "~" + String(commands[6]));
      outterSerial.print(String(commands[1]) + "~" + String(commands[2]) + "~" + String(commands[3]) + "~" + String(commands[4]) + "~" + String(commands[5])+ "~" + String(commands[6]));
    }
    else if (commands[0] == 8)
    {
      String temp = String(commands[1]);
      
      innerSerial.print("1~" + temp);
    }
    newCommand = false;

  }


  if (outterSerial.available()) {
    Serial.write(outterSerial.read());
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

void beep(int note, int duration)
{
  //Play tone on buzzerPin
  tone(buzzerPin, note, duration);

  //Play different LED depending on value of 'counter'
  if (counter % 2 == 0)
  {
    digitalWrite(ledPin1, HIGH);
    delay(duration);
    digitalWrite(ledPin1, LOW);
  } else
  {
    digitalWrite(ledPin2, HIGH);
    delay(duration);
    digitalWrite(ledPin2, LOW);
  }

  //Stop tone on buzzerPin
  noTone(buzzerPin);

  delay(50);

  //Increment counter
  counter++;
}

void firstSection()
{
  beep(a, 500);
  beep(a, 500);
  beep(a, 500);
  beep(f, 350);
  beep(cH, 150);
  beep(a, 500);
  beep(f, 350);
  beep(cH, 150);
  beep(a, 650);

  delay(500);

  beep(eH, 500);
  beep(eH, 500);
  beep(eH, 500);
  beep(fH, 350);
  beep(cH, 150);
  beep(gS, 500);
  beep(f, 350);
  beep(cH, 150);
  beep(a, 650);

  delay(500);
}

void secondSection()
{
  beep(aH, 500);
  beep(a, 300);
  beep(a, 150);
  beep(aH, 500);
  beep(gSH, 325);
  beep(gH, 175);
  beep(fSH, 125);
  beep(fH, 125);
  beep(fSH, 250);

  delay(325);

  beep(aS, 250);
  beep(dSH, 500);
  beep(dH, 325);
  beep(cSH, 175);
  beep(cH, 125);
  beep(b, 125);
  beep(cH, 250);

  delay(350);
}
