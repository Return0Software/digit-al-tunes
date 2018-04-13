from threading import Thread
from typing import List

from serial import Serial
from time import sleep

from enum import IntEnum, unique, EnumMeta

# from .Constants import SERIAL_PORT, SERIAL_RATE

import logging

log: logging.Logger = logging.getLogger(__name__)


class CommonEnum(EnumMeta):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except (TypeError, KeyError):
            return self._value2member_map_[key]


@unique
class Hand(IntEnum, metaclass=CommonEnum):
    """Represents the hand used"""
    __order__ = "LEFT RIGHT"
    LEFT = 0
    RIGHT = 1


@unique
class Finger(IntEnum, metaclass=CommonEnum):
    """Represents the finger used"""
    __order__ = "THUMB INDEX MIDDLE RING PINKY"
    THUMB = 0
    INDEX = 1
    MIDDLE = 2
    RING = 3
    PINKY = 4


@unique
class Action(IntEnum, metaclass=CommonEnum):
    """Represents either a press or release"""
    __order__ = "PRESS RELEASE"
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


"""Serial port reading utils"""


def handle_data(data: str) -> None:
    """
    Thread callback func
    :param data: line from Serial port
    :return: None
    """
    if data:  # data can be empty string quite often
        print(data, end="")  # Serial port already has new line


def read_from_port(ser: Serial) -> None:
    """
    Read data from provided Serial object
    :param ser: Serial object
    :return: None
    """
    global connected

    # Ensure not locked
    while not connected:
        connected = True

        while True:
            reading: str = ser.readline().decode()
            handle_data(reading)


def find_specific_port(name: str) -> str:
    """
    Find a port that has {name} in the description
    :param name: name that port should include
    :return: name of the port desired
    """
    import warnings
    import serial.tools.list_ports

    ports: List = [
        p.device
        for p in serial.tools.list_ports.comports()
        if name in p.description.lower()
    ]
    if not ports:
        raise IOError("No Arduino found")
    if len(ports) > 1:
        # TODO: handle multible arduinos
        warnings.warn('Multiple Arduinos found - using the first')
    return ports[0]


def find_flora() -> str:
    """
    Find which port the a Flora is on
    :return: Port name
    """
    return find_specific_port('flora')


def multithread_test() -> None:
    """
    Test and show threaded reading of a Serial port. Not sure if asynio is a better option.
    :return: None
    """
    # Instantiate as globals so threads has access
    # TODO: move to a better place for actual use
    global connected, serial_port

    # connected is acting like a thread lock
    connected = False

    # Port is unique to computer
    port: str = find_flora()

    # Should be the same as the arduino
    baud: int = 115200

    serial_port = Serial(port, baud, timeout=0)

    # Able to make custom subclass Thread but not sure if needed
    # http://www.bogotobogo.com/python/Multithread/python_multithreading_subclassing_creating_threads.php
    thread: Thread = Thread(target=read_from_port, args=(serial_port,))
    thread.start()

    # Print vals to visually show multithreading
    for i in range(100):
        print(i)
        sleep(1)


if __name__ == "__main__":
    h = Hand
    print(h[1])
