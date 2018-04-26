// ============================================================================
// Threshold for detection
// ============================================================================
const int THRESHOLD = 40;

// ============================================================================
// Data rate in bits per second (baud) for serial data transmission
// https://www.arduino.cc/en/Serial/Begin
// ============================================================================
const int BAUD = 115200;

// ============================================================================
// Pins to finger mapping
// ============================================================================

// Left Hand
const int PIN_LEFT_THUMB = 10;
const int PIN_LEFT_INDEX = 10;
const int PIN_LEFT_MIDDLE = 11;
const int PIN_LEFT_RING = 10;
const int PIN_LEFT_PINKY = 11;

const int PINS_LEFT[5] = {PIN_LEFT_THUMB, PIN_LEFT_INDEX, PIN_LEFT_MIDDLE, PIN_LEFT_RING, PIN_LEFT_PINKY};

// Right Hand
const int PIN_RIGHT_THUMB = 10;
const int PIN_RIGHT_INDEX = 10;
const int PIN_RIGHT_MIDDLE = 11;
const int PIN_RIGHT_RING = 10;
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