// ============================================================================
// Piezo Flora Detection
// Setup Sending Flora: https://learn.adafruit.com/adafruit-arduino-ide-setup/overview
// ============================================================================
// ============================================================================
// Threshold for detection
// ============================================================================
const int THRESHOLD = 100;

// ============================================================================
// Data rate in bits per second (baud) for serial data transmission
// https://www.arduino.cc/en/Serial/Begin
// ============================================================================
const int BAUD = 115200;

// ============================================================================
// Pins to finger mapping
// ============================================================================

// Left Hand
const int PIN_LEFT_THUMB = 12;
const int PIN_LEFT_INDEX = 6;
const int PIN_LEFT_MIDDLE = 9;
const int PIN_LEFT_RING = 10;
const int PIN_LEFT_PINKY = 11;

const int PINS_LEFT[5] = {PIN_LEFT_THUMB, PIN_LEFT_INDEX, PIN_LEFT_MIDDLE, PIN_LEFT_RING, PIN_LEFT_PINKY};

// Right Hand
const int PIN_RIGHT_THUMB = 10;
const int PIN_RIGHT_INDEX = 9;
const int PIN_RIGHT_MIDDLE = 6;
const int PIN_RIGHT_RING = 12;
const int PIN_RIGHT_PINKY = 11;

const int PINS_RIGHT[5] = {PIN_RIGHT_THUMB, PIN_RIGHT_INDEX, PIN_RIGHT_MIDDLE, PIN_RIGHT_RING, PIN_RIGHT_PINKY};

// ============================================================================
// Values to finger mapping
// ============================================================================

// Left Hand
const char VAL_LEFT_THUMB[3] = "00";
const char VAL_LEFT_INDEX[3] = "01";
const char VAL_LEFT_MIDDLE[3] = "02";
const char VAL_LEFT_RING[3] = "03";
const char VAL_LEFT_PINKY[3] = "04";

const char* VALS_LEFT[5] = {VAL_LEFT_THUMB, VAL_LEFT_INDEX, VAL_LEFT_MIDDLE, VAL_LEFT_RING, VAL_LEFT_PINKY};

// Right Hand
const char VAL_RIGHT_THUMB[3] = "10";
const char VAL_RIGHT_INDEX[3] = "11";
const char VAL_RIGHT_MIDDLE[3] = "12";
const char VAL_RIGHT_RING[3] = "13";
const char VAL_RIGHT_PINKY[3] = "14";

const char* VALS_RIGHT[5] = {VAL_RIGHT_THUMB, VAL_RIGHT_INDEX, VAL_RIGHT_MIDDLE, VAL_RIGHT_RING, VAL_RIGHT_PINKY};

// ============================================================================
// Pressed and released signals
// ============================================================================
const char PRESSED[2] = "1";
const char RELEASED[2] = "0";


// LEFT OR RIGHT HAND
// const int* pins = PINS_RIGHT;
// const char** letterVals = VALS_RIGHT;
const int* pins = PINS_LEFT;
const char** letterVals = VALS_LEFT;


// Container for determing if a finger was pressed in the last cycle
bool currentPressed[] = {false, false, false, false, false};

void setup()
{
	Serial.begin(BAUD);
  Serial.println("Starting Glove");
  for (int i = 0; i < 4; i++)
    pinMode(pins[i], INPUT_PULLUP);
}// const char** letterVals = VALS_RIGHT;


void loop()
{
	long dataVal;
	for (int i = 0; i < 4; i++) {
		dataVal =  digitalRead(pins[i]);

		if (!currentPressed[i] && dataVal == HIGH) {
			Serial.print(letterVals[i]);
			Serial.println(PRESSED);
			currentPressed[i] = true;
		} else if (currentPressed[i] && dataVal == LOW) {
			Serial.print(letterVals[i]);
			Serial.println(RELEASED);
			currentPressed[i] = false;
		}
		delay(10);
	}
}
