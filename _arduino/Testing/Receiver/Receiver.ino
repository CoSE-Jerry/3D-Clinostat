char mystr[10]; //Initialized variable to store recieved data

void setup() {
  // Begin the Serial at 9600 Baud
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available()>0)
  {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.read();
  }
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);

}
