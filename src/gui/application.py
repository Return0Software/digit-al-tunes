import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from .main_window import MainWindow

import sys
sys.path.append(sys.path[0] + "/..")
# from .. import Constants
from Constants import DIGIT_AL_TUNES_APP_ID

import logging
log: logging = logging.getLogger(__name__)


class Application(Gtk.Application):
    """
    Gtk.Application implementation for Digit-al Tunes
    """

    __window = None

    def __init__(self):
        Gtk.Application.__init__(self, application_id=DIGIT_AL_TUNES_APP_ID)

        self.connect("activate", self.__activate_cb)
        self.connect("shutdown", lambda app: app.quit())

        log.debug("Application started")

    def __activate_cb(self, app: Gtk.Application) -> None:
        """
        Starts the application

        :param app: A Gtk.Application object referring to the current application
        """
        self.__window_check()
        self.__window.show_all()
        self.__window.present()

    def __window_check(self) -> None:
        if self.__window is None:
            self.__window = MainWindow()
            self.add_window(self.__window)
            log.debug("Main window created")
