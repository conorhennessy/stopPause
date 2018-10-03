// Spotify Conductor project - an Arduino project for an emergency stop button to control & pause media playback
#include <Keyboard.h>

//Set pins
const int buttonPin = 2;
const int ledPin = 17;

int buttonState = 0;


void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the button pin as an input:
  pinMode(buttonPin, INPUT);
  
  Keyboard.begin();
}


void loop() {
  // read and check state of push button pin
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    Keyboard.press('a');
    delay(100);
    Keyboard.releaseAll();
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
}
