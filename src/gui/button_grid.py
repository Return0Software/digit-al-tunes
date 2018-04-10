import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import json

from typing import Any, Dict

import logging
log: logging = logging.getLogger(__name__)


class ButtonGrid(Gtk.Grid):
    """
    Grid of buttons that represent the fingers
    """

    __data: Dict[str, Any] = None

    def __init__(self):
        Gtk.Grid.__init__(self, column_homogeneous=True, row_homogeneous=True)

        with open("./config/default.json") as f:
            self.__data = json.load(f)

        col: int = 0
        row: int = 0
        for key in self.__data.keys():
            if row % 5 == 0:
                col += 1
                row = 0
            b = Gtk.Button.new_with_label(key)
            b.connect("clicked", lambda button: print("ButtonGrid callback"))
            self.attach(b, row, col, 1, 1)
            row += 1
