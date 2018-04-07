import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import logging
log: logging = logging.getLogger(__name__)


class HeaderBar(Gtk.HeaderBar):
    """
    Headerbar for the main window
    """

    __reset = None
    __save = None

    def __init__(self):
        Gtk.HeaderBar.__init__(self, title="Digit-al Tunes", show_close_button=True,
            has_subtitle=True, subtitle="New Configuration")

        self.__reset = Gtk.Button.new_with_label("Reset")
        self.__reset.connect("clicked", self.__reset_cb)
        self.__reset.get_style_context().add_class("destructive-action")
        self.pack_end(self.__reset)

        self.__save = Gtk.Button.new_with_label("Save")
        self.__save.connect("clicked", self.__save_cb)
        self.__save.get_style_context().add_class("suggested-action")
        self.pack_start(self.__save)

    def __reset_cb(self, button: Gtk.Button):
        print("Reset Callback")

    def __save_cb(self, button: Gtk.Button):
        print("Save Callback")
