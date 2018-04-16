import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk

from typing import List

import logging
log: logging = logging.getLogger(__name__)


class SerialVisualizer(Gtk.Box):

    __left_indicators: List[Gtk.Box] = None
    __right_indicators: List[Gtk.Box] = None
    __store: Gtk.ListStore = None
    __sw: Gtk.ScrolledWindow = None

    def __init__(self):
        Gtk.Box.__init__(self, spacing=20, orientation=Gtk.Orientation.HORIZONTAL)

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

        self.__store = Gtk.ListStore(str, str, str, str)
        tree = Gtk.TreeView(self.__store)
        tree.connect("size-allocate", self.__treeview_changed)
        for index, header in enumerate(("Serial Data", "Hand", "Finger", "Action")):
            c = Gtk.TreeViewColumn(header, Gtk.CellRendererText(), text=index)
            c.set_expand(True)
            tree.append_column(c)
        for i in range(100):
            self.__store.append(("(0, 0, 0)", "Left", "Thumb", "Pressed"))

        self.__sw = Gtk.ScrolledWindow(hscrollbar_policy=Gtk.PolicyType.NEVER,
            kinetic_scrolling=True, vscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
            shadow_type=Gtk.ShadowType.ETCHED_OUT)
        self.__sw.add(tree)

        self.pack_start(left_grid, True, True, 0)
        self.pack_start(Gtk.Separator.new(Gtk.Orientation.VERTICAL), False, True, 0)
        self.pack_start(self.__sw, True, True, 0)
        self.pack_start(Gtk.Separator.new(Gtk.Orientation.VERTICAL), False, True, 0)
        self.pack_end(right_grid, True, True, 0)

    def __treeview_changed(self, tree: Gtk.TreeView, rect: Gdk.Rectangle) -> None:
        adj = self.__sw.get_vadjustment()
        adj.set_value(adj.get_upper() - adj.get_page_size())
