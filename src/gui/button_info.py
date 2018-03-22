import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import logging
log: logging = logging.getLogger(__name__)


class ButtonInfo(Gtk.Frame):
    """
    Widget to display info on buttons
    """

    __grid = None

    def __init__(self):
        Gtk.Frame.__init__(self)
