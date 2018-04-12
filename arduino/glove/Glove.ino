// ============================================================================
// Piezo Flora Detection
// Setup Sending Flora: https://learn.adafruit.com/adafruit-arduino-ide-setup/overview
// ============================================================================
#include "constants.h"

const int* pins = PINS_LEFT;
// const int* pins = PINS_RIGHT;

const char** letterVals = VALS_LEFT;
// const char** letterVals = VALS_RIGHT;

// Container for determing if a finger was pressed in the last cycle
bool currentPressed[] = {false, false, false, false, false};

void setup()
{
	//while (!Serial)
	Serial.begin(BAUD);
	Serial.println("Starting Glove");
}


void loop()
{
	long dataVal;
	for (int i = 0; i < 5; i++) {
		dataVal =  analogRead(pins[i]);

		if ((dataVal > THRESHOLD) && !currentPressed[i]) {
			Serial.print(letterVals[i]);
			Serial.println(PRESSED);
			currentPressed[i] = true;
		} else if ((dataVal <= THRESHOLD) && (currentPressed[i])) {
			Serial.print(letterVals[i]);
			Serial.println(RELEASED);
			currentPressed[i] = false;
		}
		delay(1);
	}
}
