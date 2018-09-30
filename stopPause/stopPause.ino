
#include <Keyboard.h>

//Set pins
const int buttonPin = 2;
const int ledPin = 17;

int buttonState = 0;


void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Keyboard.begin();
}


// the loop function runs over and over again forever
void loop() {
  // read state of push button pin

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
