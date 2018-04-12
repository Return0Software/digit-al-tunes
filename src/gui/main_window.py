import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import json
from typing import Any, Dict, Union

from .button_grid import ButtonGrid
from .button_info import ButtonInfo
from .headerbar import HeaderBar

import logging
log: logging = logging.getLogger(__name__)


class MainWindow(Gtk.ApplicationWindow):
    """
    The main application window
    """

    __button_grid: ButtonGrid = None
    __button_info: ButtonInfo = None
    __data: Dict[str, Any] = None
    __grid: Gtk.Grid = None
    __headerbar: HeaderBar = None
    __revealer: Gtk.Revealer = None
    __reveal_button: Gtk.Button = None
    __reveal_image: Gtk.Image = None

    def __init__(self):
        Gtk.ApplicationWindow.__init__(self)

        with open("./config/default.json") as f:
            self.__data = json.load(f)

        self.set_border_width(10)

        self.__headerbar = HeaderBar()
        self.set_titlebar(self.__headerbar)

        main_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        main_box.set_property("margin", 10)

        self.__button_grid = ButtonGrid(self.__data.keys())
        self.__button_grid.connect("button-clicked", self.__setup_button_info_cb)
        self.__reveal_image = Gtk.Image.new_from_icon_name("pan-start-symbolic",
            Gtk.IconSize.BUTTON)
        self.__reveal_button = Gtk.Button()
        self.__reveal_button.set_image(self.__reveal_image)
        self.__reveal_button.connect("clicked", self.__revealer_cb)
        self.__button_info = ButtonInfo()
        self.__button_info.connect("close-revealer", self.__revealer_cb)
        self.__revealer = Gtk.Revealer(transition_type=Gtk.RevealerTransitionType.SLIDE_LEFT)
        self.__revealer.add(self.__button_info)

        main_box.pack_start(self.__button_grid, True, True, 0)
        main_box.pack_start(self.__reveal_button, False, True, 0)
        main_box.pack_end(self.__revealer, False, True, 0)

        self.add(main_box)

    def __revealer_cb(self, object: Union[ButtonInfo, Gtk.Button]) -> None:
        """Close the revealer"""
        # Refactor into 2 different methods? open_revealer and close_revealer
        if self.__revealer.get_child_revealed():
            self.__revealer.set_reveal_child(False)
            self.__reveal_image.set_from_icon_name("pan-start-symbolic", Gtk.IconSize.BUTTON)
        else:
            self.__revealer.set_reveal_child(True)
            self.__reveal_image.set_from_icon_name("pan-end-symbolic", Gtk.IconSize.BUTTON)

    def __setup_button_info_cb(self, button_grid: ButtonGrid, key: str) -> None:
        if not self.__revealer.get_child_revealed():
            self.__revealer.set_reveal_child(True)
            self.__reveal_image.set_from_icon_name("pan-end-symbolic", Gtk.IconSize.BUTTON)
        self.__button_info.set_info(key, **self.__data[key])
