import serial

from enum import IntEnum, unique

from .Constants import SERIAL_PORT, SERIAL_RATE

import logging
log: logging = logging.getLogger(__name__)


@unique
class Hand(IntEnum):
    """Represents the hand used"""

    LEFT = 0
    RIGHT = 1


@unique
class Finger(IntEnum):
    """Represents the finger used"""

    THUMB = 0
    INDEX = 1
    MIDDLE = 2
    RING = 3
    PINKY = 4


@unique
class Action(IntEnum):
    """Represents either a press or release"""

    PRESS = 0
    RELEASE = 1


class SerialData():
    """Python representation of data read from the SerialPort"""

    HAND: Hand = None
    FINGER: Finger = None
    ACTION: Action = None

    def __init__(self, data: str):
        if len(data) != 3:
            raise ValueError("Length of data in incorrect")

        # parse hand
        for hand in Hand:
            if data[0] == hand:
                self.HAND = hand
                break

        if self.HAND is None:
            raise ValueError("Hand value could not be parsed")

        # parse finger
        for finger in Finger:
            if data[1] == finger:
                self.FINGER = finger
                break

        if self.FINGER is None:
            raise ValueError("Finger value could not be parsed")

        # parse action
        for action in Action:
            if data[2] == action:
                self.ACTION = action
                break

        if self.ACTION is None:
            raise ValueError("Action value could not be parsed")


def read_port():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    while True:
        data = SerialData(ser.readline().decode("utf-8"))
        print("{}, {}, {}".format(data.HAND, data.FINGER, data.ACTION))
