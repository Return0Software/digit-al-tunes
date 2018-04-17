import gi
gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gio, Gtk

from .main_window import MainWindow

import sys
sys.path.append(sys.path[0] + "/..")
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
        self.__init_css()
        self.connect("shutdown", lambda app: app.quit())

        log.debug("Application started")

    def __activate_cb(self, app: Gtk.Application) -> None:
        """
        Starts the application

        :param app: A Gtk.Application object referring to the current application
        """

        self.__init_css()
        self.__window_check()
        self.__window.show_all()
        self.__window.present()

    def __window_check(self) -> None:
        """Checks to make sure only one instance of the program is running"""

        if self.__window is None:
            self.__window = MainWindow()
            self.add_window(self.__window)
            log.debug("Main window created")

    def __init_css(self):
        """Set up the CSS before we throw any windows up"""

        try:
            f = Gio.File.new_for_path("./gui/css/styling.css")
            css = Gtk.CssProvider()
            css.load_from_file(f)
            screen = Gdk.Screen.get_default()
            prio = Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            Gtk.StyleContext.add_provider_for_screen(screen, css, prio)
        except Exception as e:
            print("Error loading CSS: {}".format(e))
