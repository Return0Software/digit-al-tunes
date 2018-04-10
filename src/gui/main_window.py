import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from .headerbar import HeaderBar
from .button_info import ButtonInfo

import logging
log: logging = logging.getLogger(__name__)


class MainWindow(Gtk.ApplicationWindow):
    """
    The main application window
    """

    __button_info = None
    __grid = None
    __headerbar = None
    __revealer = None

    def __init__(self):
        Gtk.ApplicationWindow.__init__(self)

        self.set_border_width(10)

        self.__headerbar = HeaderBar()
        self.set_titlebar(self.__headerbar)

        self.__button_info = ButtonInfo()
        self.__revealer = Gtk.Revealer(transition_type=Gtk.RevealerTransitionType.SLIDE_LEFT)
        self.__revealer.add(self.__button_info)
        self.__revealer.set_reveal_child(True)

        self.add(self.__revealer)
