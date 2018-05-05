import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject, Gtk

import logging
log: logging = logging.getLogger(__name__)


class ButtonInfo(Gtk.Grid):
    """
    Widget to display info on buttons
    """

    __gsignals__ = {
        "close-revealer": (GObject.SIGNAL_RUN_FIRST, None, ()),
        "done-editing": (GObject.SIGNAL_RUN_FIRST, None, (str, str))
    }

    __action_bar: Gtk.ActionBar = None
    __close: Gtk.Button = None
    __done: Gtk.Button = None
    __grid: Gtk.Grid = None
    __label: Gtk.Label = None
    __path_button: Gtk.FileChooserButton = None
    __win: Gtk.ApplicationWindow = None

    enabled: bool = None

    def __init__(self, win: Gtk.ApplicationWindow):
        Gtk.Grid.__init__(self, column_spacing=50, row_spacing=10)

        self.__win = win

        # Creating the action bar
        self.__label = Gtk.Label()
        self.__done = Gtk.Button.new_with_label("Done")
        self.__done.get_style_context().add_class("suggested-action")
        self.__done.connect("clicked", self.__done_editing)
        self.__close = Gtk.Button.new_from_icon_name("window-close-symbolic", Gtk.IconSize.BUTTON)
        self.__close.connect("clicked", lambda button: self.emit("close-revealer"))
        self.__action_bar = Gtk.ActionBar()
        self.__action_bar.get_style_context().add_class("frame")
        self.__action_bar.pack_start(self.__done)
        self.__action_bar.set_center_widget(self.__label)
        self.__action_bar.pack_end(self.__close)

        self.attach(self.__action_bar, 0, 0, 2, 1)

        self.__path_button = Gtk.Button.new_with_label("None")
        self.__path_button.connect("clicked", self.__update_path_cb)
        self.__path_button.set_margin_bottom(10)
        self.__path_button.set_margin_right(10)

        self.attach(Gtk.Label("Path", halign=Gtk.Align.START, margin_bottom=10, margin_left=10),
            0, 1, 1, 1)
        self.attach(self.__path_button, 1, 1, 1, 1)

        self.get_style_context().add_class("border-pls")

        self.disable()

    def __done_editing(self, button: Gtk.Button) -> None:
        self.emit("done-editing", self.__label.get_text(),
            self.__path_button.get_title())

    def __update_path_cb(self, button: Gtk.Button) -> None:
        dialog = Gtk.FileChooserNative.new("Open file", self.__win,
        Gtk.FileChooserAction.OPEN, "_Open", "_Cancel")

        response = dialog.run()
        if response == Gtk.ResponseType.ACCEPT:
            file_name = dialog.get_filename()
        dialog.destroy()

        if file_name is not None:
            self.__path_button.set_label(file_name)

    def disable(self) -> None:
        self.enabled = False
        self.__done.set_sensitive(False)
        self.__path_button.set_sensitive(False)

    def enable(self) -> None:
        self.enabled = True
        self.__done.set_sensitive(True)
        self.__path_button.set_sensitive(True)

    def set_info(self, label: str, **kwargs) -> None:
        if not self.enabled:
            self.enable()
        self.__label.set_label(label)
        if "path" in kwargs.keys() and kwargs["path"] is not None:
            self.__path_button.set_label(kwargs["path"])
        else:
            self.__path_button.set_label("None")
