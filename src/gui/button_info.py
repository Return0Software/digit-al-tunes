import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import logging
log: logging = logging.getLogger(__name__)


class ButtonFunction():
    NONE = "None"
    SOUND = "Sound"
    LOOP = "Loop"


class ButtonInfo(Gtk.Frame):
    """
    Widget to display info on buttons
    """

    __combo = None
    __grid = None
    __name_entry = None

    def __init__(self):
        Gtk.Frame.__init__(self, label="Button Information", label_xalign=0.25,
                           shadow_type=Gtk.ShadowType.ETCHED_OUT)

        self.__grid = Gtk.Grid(column_homogeneous=True, column_spacing=10,
                               row_homogeneous=True, row_spacing=10)

        # Creating the button function combobox
        self.__combo = Gtk.ComboBoxText()
        self.__combo.append_text(ButtonFunction.NONE)
        self.__combo.append_text(ButtonFunction.SOUND)
        self.__combo.append_text(ButtonFunction.LOOP)
        self.__combo.set_active(0)
        self.__combo.connect("changed", self.__combo_changed_cb)

        self.__name_entry = Gtk.Entry(editable=True, has_frame=True)

        self.__grid.attach(Gtk.Label("Name", xalign=Gtk.Align.START), 0, 0, 1, 1)
        self.__grid.attach(self.__name_entry, 1, 0, 1, 1)
        self.__grid.attach(Gtk.Label("Function", xalign=Gtk.Align.START), 0, 1, 1, 1)
        self.__grid.attach(self.__combo, 1, 1, 1, 1)

        self.add(self.__grid)

    def __combo_changed_cb(self, combo: Gtk.ComboBoxText) -> None:
        print(combo.get_active_text())
