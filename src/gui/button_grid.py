import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject, Gtk

from typing import List

import logging
log: logging = logging.getLogger(__name__)


class ButtonGrid(Gtk.Grid):
    """
    Grid of buttons that represent the fingers
    """

    __gsignals__ = {
        "button-clicked": (GObject.SIGNAL_RUN_FIRST, None, (str,))
    }

    def __init__(self, keys: List[str]):
        Gtk.Grid.__init__(self, expand=True, column_homogeneous=True, row_homogeneous=True)

        # grid placement
        col: int = 0
        row: int = 0
        for key in keys:
            if row % 4 == 0:
                col += 1
                row = 0
            b = Gtk.Button.new_with_label(key)
            b.connect("clicked", lambda button: self.emit("button-clicked", button.get_label()))
            self.attach(b, row, col, 1, 1)
            row += 1
