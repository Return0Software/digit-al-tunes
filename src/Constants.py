import logging

# Logging data
LOG_DEFAULT_FILENAME = "log.out"
LOG_FORMAT = '%(levelname)s | %(asctime)-15s | %(message)s'
LOG_CONFIG = {
    "format": LOG_FORMAT,
    "level": logging.DEBUG,
    "filename": LOG_DEFAULT_FILENAME
}

# Gtk data
DIGIT_AL_TUNES_APP_ID = "com.github.return0software.Digit-al-Tunes"
FINGER_PRESSED = "finger-pressed"
FINGER_NOT_PRESSED = "finger-not-pressed"

# """
# Instantiate an ultrasonic sensor with the board

# :param trig_pin: Trigger Pin Number
# :param echo_pin: Echo Pin Number
# :param cb: Callback
# :return: None
# """
