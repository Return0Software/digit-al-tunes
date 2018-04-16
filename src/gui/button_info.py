import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject, Gtk

import logging
log: logging = logging.getLogger(__name__)


class ButtonFunction():
    NONE = "None"
    SOUND = "Sound"
    LOOP = "Loop"


class ButtonInfo(Gtk.Grid):
    """
    Widget to display info on buttons
    """

    __gsignals__ = {
        "close-revealer": (GObject.SIGNAL_RUN_FIRST, None, ())
    }

    __action_bar: Gtk.ActionBar = None
    __close: Gtk.Button = None
    __combo: Gtk.ComboBoxText = None
    __done: Gtk.Button = None
    __grid: Gtk.Grid = None
    __label: Gtk.Label = None
    __name_entry: Gtk.Entry = None

    enabled: bool = None

    def __init__(self):
        Gtk.Grid.__init__(self, column_homogeneous=True, row_spacing=10)

        # Creating the action bar
        self.__label = Gtk.Label()
        self.__done = Gtk.Button.new_with_label("Done")
        self.__done.get_style_context().add_class("suggested-action")
        self.__done.connect("clicked", lambda button: print("Done")) # save
        self.__close = Gtk.Button.new_from_icon_name("window-close-symbolic", Gtk.IconSize.BUTTON)
        self.__close.connect("clicked", lambda button: self.emit("close-revealer"))
        self.__action_bar = Gtk.ActionBar()
        self.__action_bar.get_style_context().add_class("frame")
        self.__action_bar.pack_start(self.__done)
        self.__action_bar.set_center_widget(self.__label)
        self.__action_bar.pack_end(self.__close)

        self.attach(self.__action_bar, 0, 0, 2, 1)

        # Creating the editable info for a finger combination
        self.__combo = Gtk.ComboBoxText(margin_right=10)
        self.__combo.append_text(ButtonFunction.NONE)
        self.__combo.append_text(ButtonFunction.SOUND)
        self.__combo.append_text(ButtonFunction.LOOP)
        self.__combo.set_active(0)
        self.__combo.connect("changed", self.__combo_changed_cb)

        self.__name_entry = Gtk.Entry(editable=True, has_frame=True, margin_right=10)

        self.attach(Gtk.Label("Name", halign=Gtk.Align.START, margin_left=10), 0, 1, 1, 1)
        self.attach(self.__name_entry, 1, 1, 1, 1)
        self.attach(Gtk.Label("Function", halign=Gtk.Align.START, margin_left=10), 0, 2, 1, 1)
        self.attach(self.__combo, 1, 2, 1, 1)

        self.get_style_context().add_class("border-pls")

        self.disable()

    def __combo_changed_cb(self, combo: Gtk.ComboBoxText) -> None:
        print(combo.get_active_text())

    def disable(self) -> None:
        self.enabled = False
        self.__name_entry.set_sensitive(False)
        self.__combo.set_sensitive(False)

    def enable(self) -> None:
        self.enabled = True
        self.__name_entry.set_sensitive(True)
        self.__combo.set_sensitive(True)

    def set_info(self, key: str, **kwargs) -> None:
        if not self.enabled:
            self.enable()
        self.__label.set_label(key)
