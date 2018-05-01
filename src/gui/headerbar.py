import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject, Gtk

import logging
log: logging = logging.getLogger(__name__)


class HeaderBar(Gtk.HeaderBar):
    """
    Headerbar for the main window
    """

    __gsignals__ = {
        "open": (GObject.SIGNAL_RUN_FIRST, None, (str,)),
        "save": (GObject.SIGNAL_RUN_FIRST, None, (str,))
    }

    __new_config_name = "New Configuraton"
    __open: Gtk.Button = None
    __reset: Gtk.Button = None
    __save: Gtk.Button = None

    def __init__(self):
        Gtk.HeaderBar.__init__(self, title="Digit-al Tunes", show_close_button=True,
            has_subtitle=True, subtitle=self.__new_config_name)

        self.__reset = Gtk.Button.new_with_label("Reset")
        self.__reset.connect("clicked", self.__reset_cb)
        self.__reset.get_style_context().add_class("destructive-action")
        self.pack_end(self.__reset)

        self.__save = Gtk.Button.new_with_label("Save")
        self.__save.connect("clicked", self.__save_cb)
        self.__save.get_style_context().add_class("suggested-action")
        self.pack_start(self.__save)

        self.__open = Gtk.Button.new_with_label("Open")
        self.__open.connect("clicked", self.__open_cb)
        self.pack_start(self.__open)

    def __open_cb(self, button: Gtk.Button) -> None:
        subtitle = self.get_subtitle()
        self.emit("open", None if self.__new_config_name in subtitle else subtitle)

    def __reset_cb(self, button: Gtk.Button) -> None:
        print("Reset Callback")

    def __save_cb(self, button: Gtk.Button) -> None:
        subtitle = self.get_subtitle()
        self.emit("save", None if self.__new_config_name in subtitle else subtitle)
