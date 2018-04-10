import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from .button_grid import ButtonGrid
from .button_info import ButtonInfo
from .headerbar import HeaderBar

import logging
log: logging = logging.getLogger(__name__)


class MainWindow(Gtk.ApplicationWindow):
    """
    The main application window
    """

    __button_grid: ButtonGrid = None
    __button_info: ButtonInfo = None
    __grid: Gtk.Grid = None
    __headerbar: HeaderBar = None
    __revealer: Gtk.Revealer = None

    def __init__(self):
        Gtk.ApplicationWindow.__init__(self)

        self.set_border_width(10)

        self.__headerbar = HeaderBar()
        self.set_titlebar(self.__headerbar)

        main_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        main_box.set_property("margin", 10)

        self.__button_grid = ButtonGrid()

        self.__button_info = ButtonInfo()
        self.__revealer = Gtk.Revealer(transition_type=Gtk.RevealerTransitionType.SLIDE_LEFT)
        self.__revealer.add(self.__button_info)
        self.__revealer.set_reveal_child(True)

        main_box.pack_start(self.__button_grid, True, True, 0)
        main_box.pack_end(self.__revealer, False, True, 0)

        self.add(main_box)
