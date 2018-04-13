import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from typing import List

import logging
log: logging = logging.getLogger(__name__)


class SerialVisualizer(Gtk.Stack):

    __left_indicators: List[Gtk.DrawingArea] = None
    __right_indicators: List[Gtk.DrawingArea] = None

    def __init__(self):
        Gtk.Stack.__init__(self, expand=True, homogeneous=True, interpolate_size=True,
            transition_type=Gtk.StackTransitionType.OVER_LEFT_RIGHT)

        encompassing_grid = Gtk.Grid(column_spacing=50,
            row_homogeneous=True, row_spacing=20)

        left_grid = Gtk.Grid(column_homogeneous=True, column_spacing=50, expand=True,
            row_spacing=40)
        left_grid.attach(Gtk.Label("<b><big><u>Left</u></big></b>", use_markup=True), 0, 0, 5, 1)
        left_grid.attach(Gtk.Label("<b>Pinky</b>", use_markup=True), 0, 1, 1, 1)
        left_grid.attach(Gtk.Label("<b>Ring</b>", use_markup=True), 1, 1, 1, 1)
        left_grid.attach(Gtk.Label("<b>Middle</b>", use_markup=True), 2, 1, 1, 1)
        left_grid.attach(Gtk.Label("<b>Index</b>", use_markup=True), 3, 1, 1, 1)
        left_grid.attach(Gtk.Label("<b>Thumb</b>", use_markup=True), 4, 1, 1, 1)

        self.__left_indicators = []
        for i in range(5):
            area = Gtk.Box()
            area.set_size_request(-1, 30)
            area.get_style_context().add_class("finger-pressed")
            area.get_style_context().add_class("rounded-box")
            self.__left_indicators.append(area)

        for index, area in enumerate(self.__left_indicators):
            left_grid.attach(area, index, 2, 1, 1)

        right_grid = Gtk.Grid(column_homogeneous=True, column_spacing=50, expand=True,
            row_spacing=40)
        right_grid.attach(Gtk.Label("<b><big><u>Right</u></big></b>", use_markup=True), 0, 0, 5, 1)
        right_grid.attach(Gtk.Label("<b>Thumb</b>", use_markup=True), 0, 1, 1, 1)
        right_grid.attach(Gtk.Label("<b>Index</b>", use_markup=True), 1, 1, 1, 1)
        right_grid.attach(Gtk.Label("<b>Middle</b>", use_markup=True), 2, 1, 1, 1)
        right_grid.attach(Gtk.Label("<b>Ring</b>", use_markup=True), 3, 1, 1, 1)
        right_grid.attach(Gtk.Label("<b>Pinky</b>", use_markup=True), 4, 1, 1, 1)

        self.__right_indicators = []
        for i in range(5):
            area = Gtk.Box()
            area.set_size_request(-1, 30)
            area.get_style_context().add_class("finger-not-pressed")
            area.get_style_context().add_class("rounded-box")
            self.__right_indicators.append(area)

        for index, area in enumerate(self.__right_indicators):
            right_grid.attach(area, index, 2, 1, 1)

        encompassing_grid.attach(left_grid, 0, 0, 1, 1)
        encompassing_grid.attach(Gtk.Separator.new(Gtk.Orientation.VERTICAL), 1, 0, 1, 1)
        encompassing_grid.attach(right_grid, 2, 0, 1, 1)

        self.add_titled(encompassing_grid, "hand_visualizer", "Hand Visualizer")

        # 2 grids, one for left, one for right, helper function to decrease duplication
