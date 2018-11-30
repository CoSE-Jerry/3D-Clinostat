#include <Adafruit_NeoPixel.h>
#define PIN 6
#define NUM_LEDS 30
#define BRIGHTNESS 50
#define QUARTER NUM_LEDS/4


int serial_CMD;
boolean IR_STAT = false;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRBW + NEO_KHZ800);


void setup() {

  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);
  Serial.begin(9600);

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

  serial_read();
  if (serial_CMD == 48)
  {
    reset();
  }

  if (serial_CMD == 49)
  {
    top_white();
  }

  if (serial_CMD == 50)
  {
    left_white();
  }

  if (serial_CMD == 51)
  {
    right_white();
  }

  if (serial_CMD == 52)
  {
    bottom_white();
  }

  if (serial_CMD == 53)
  { if (!IR_STAT)
    {
      digitalWrite(2, HIGH);
      IR_STAT = true;
      Serial.println("false");
    }
    else
    {
      digitalWrite(2, LOW);
      IR_STAT = false;
      Serial.println("true");
    }

  }
}


void serial_read()
{
  if (Serial.available())
  {
    serial_CMD = (int)Serial.read();
  }
}

void colorWipe(uint32_t c, uint8_t wait) {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
}

void reset() {

  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, 0, 0, 0, 0);
  }
  strip.show();

}

void top_white() {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    if (i > QUARTER - 1 && i < 2 * QUARTER + 1)
      strip.setPixelColor(i, 0, 0, 0, 255);
  }
  strip.show();
}


void left_white() {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    if (i < QUARTER)
      strip.setPixelColor(i, 0, 0, 0, 255);
  }
  strip.show();
}


void right_white() {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    if (i > 2 * QUARTER - 1 && i < 3 * QUARTER + 1)
      strip.setPixelColor(i, 0, 0, 0, 255);
  }
  strip.show();
}


void bottom_white() {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    if (i > 3 * QUARTER - 1)
      strip.setPixelColor(i, 0, 0, 0, 255);
  }
  strip.show();
}
