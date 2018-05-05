from threading import Thread
from typing import List, Tuple

from serial import Serial

from enum import IntEnum, unique, EnumMeta

import logging

log: logging.Logger = logging.getLogger(__name__)

ACTIVE_FLORAS: List[str] = []


class CommonEnum(EnumMeta):
    def __getitem__(self, key):
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
    __order__ = "RELEASED PRESSED"
    RELEASED = 0
    PRESSED = 1


"""Serial port reading utils"""


def find_specific_port(name: str) -> str:
    """
    Find a port that has {name} in the description
    :param name: name that port should include
    :return: name of the port desired
    """
    import warnings
    import serial.tools.list_ports

    ports: List = [
        {"device": p.device, "name": p.description}
        for p in serial.tools.list_ports.comports()
        if name in p.description.lower()
    ]
    if not ports:
        raise IOError("No {} found".format(name))
    if len(ports) > 1:
        for port in ports:
            if port["device"] not in ACTIVE_FLORAS:
                ACTIVE_FLORAS.append(port["device"])
                print("Found and Connected to {}({})".format(port["name"], port["device"]))
                return port["device"]
        raise IOError("No {} found".format(name))

    print("Found and Connected to {}({})".format(ports[0]["name"], ports[0]["device"]))
    return ports[0]["device"]


def find_flora() -> str:
    """
    Find which port the a Flora is on
    :return: Port name
    """
    return find_specific_port('flora')


def handle_data(data: str) -> Tuple[str, str, str] or None:
    """
    Cleansing of data from the port
    :param data: line from Serial port
    :return: None
    """
    if data not in ['', None]:  # data can be empty string quite often
        data = data.rstrip()
        try:
            if len(data) == 3:
                return (
                    Hand[int(data[0])],
                    Finger[int(data[1])],
                    Action[int(data[2])]
                )
        except (ValueError, IndexError) as e:
            # Should never reach here
            log.error(e, end="")  # Serial port already has new line
            print(e, end="")
    return None


def read_from_port(ser: Serial, cb) -> None:
    """
    Read data from provided Serial object
    :param ser: Serial object
    :param cb: callback
    :return: None
    """
    global connected

    # Ensure not locked
    while not connected:
        connected = True

        while True:
            reading: str = ser.readline().decode()
            data = handle_data(reading)

            if data:
                cb(data)


class GloveReader:
    def __init__(self, cb):
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
        thread: Thread = Thread(target=read_from_port, args=(serial_port, cb), daemon=True)
        thread.start()


if __name__ == "__main__":
    g1 = GloveReader(print)
    g2 = GloveReader(print)
