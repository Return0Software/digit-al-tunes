import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

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

    __action_bar: Gtk.ActionBar = None
    __combo: Gtk.ComboBoxText = None
    __done: Gtk.Button = None
    __grid: Gtk.Grid = None
    __label: Gtk.Label = None
    __name_entry: Gtk.Entry = None
    __close: Gtk.Button = None

    def __init__(self):
        Gtk.Grid.__init__(self, column_homogeneous=True, row_spacing=10)

        # Creating the action bar
        self.__label = Gtk.Label()
        self.__done = Gtk.Button.new_with_label("Done")
        self.__done.get_style_context().add_class("suggested-action")
        self.__done.connect("clicked", lambda button: print("Done")) # save
        self.__close = Gtk.Button.new_from_icon_name("window-close-symbolic", Gtk.IconSize.BUTTON)
        self.__close.connect("clicked", lambda button: print("close")) # hide revealer
        self.__action_bar = Gtk.ActionBar()
        self.__action_bar.get_style_context().add_class("titlebar")
        self.__action_bar.pack_start(self.__done)
        self.__action_bar.set_center_widget(self.__label)
        self.__action_bar.pack_end(self.__close)

        self.attach(self.__action_bar, 0, 0, 2, 1)

        # Creating the button function combobox
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

    def __combo_changed_cb(self, combo: Gtk.ComboBoxText) -> None:
        print(combo.get_active_text())

    def set_info(self, label: str, **kwargs) -> None:
        self.__label.set_label(label)
