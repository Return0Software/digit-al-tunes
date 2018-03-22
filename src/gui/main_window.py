import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from .headerbar import HeaderBar

import logging
log: logging = logging.getLogger(__name__)


class MainWindow(Gtk.ApplicationWindow):
    """
    The main application window
    """

    __headerbar = None

    def __init__(self):
        Gtk.ApplicationWindow.__init__(self)

        self.__headerbar = HeaderBar()
        self.set_titlebar(self.__headerbar)
        self.add(Gtk.Label("Hello World"))
