import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, GObject, Gtk

import sys
import threading
from typing import List, Tuple

sys.path.append(sys.path[0] + "/..")
from Constants import FINGER_PRESSED, FINGER_NOT_PRESSED
from glove_interpreter import GloveReader, Hand, Finger, Action

import logging
log: logging = logging.getLogger(__name__)


class SerialVisualizer(Gtk.Box):

    __gsignals__ = {
        "button-pressed": (GObject.SIGNAL_RUN_FIRST, None, (int, int, int))
    }

    __left_fingers: List[Gtk.Box] = None
    __right_fingers: List[Gtk.Box] = None
    __store: Gtk.ListStore = None
    __sw: Gtk.ScrolledWindow = None
    __tree: Gtk.TreeView = None

    def __init__(self):
        Gtk.Box.__init__(self, spacing=20, orientation=Gtk.Orientation.HORIZONTAL)

        left_grid = Gtk.Grid(column_homogeneous=True, column_spacing=50, expand=True,
            row_spacing=40)
        left_grid.attach(Gtk.Label("<b><big><u>Left</u></big></b>", use_markup=True), 0, 0, 4, 1)
        left_grid.attach(Gtk.Label("<b>Ring</b>", use_markup=True), 0, 1, 1, 1)
        left_grid.attach(Gtk.Label("<b>Middle</b>", use_markup=True), 1, 1, 1, 1)
        left_grid.attach(Gtk.Label("<b>Index</b>", use_markup=True), 2, 1, 1, 1)
        left_grid.attach(Gtk.Label("<b>Thumb</b>", use_markup=True), 3, 1, 1, 1)

        self.__left_fingers = []
        for i in range(4):
            area = Gtk.Box()
            area.set_size_request(-1, 35)
            area.get_style_context().add_class("finger-not-pressed")
            area.get_style_context().add_class("rounded-box")
            self.__left_fingers.append(area)

        for index, area in enumerate(self.__left_fingers):
            left_grid.attach(area, index, 2, 1, 1)

        right_grid = Gtk.Grid(column_homogeneous=True, column_spacing=50, expand=True,
            row_spacing=40)
        right_grid.attach(Gtk.Label("<b><big><u>Right</u></big></b>", use_markup=True), 0, 0, 4, 1)
        right_grid.attach(Gtk.Label("<b>Thumb</b>", use_markup=True), 0, 1, 1, 1)
        right_grid.attach(Gtk.Label("<b>Index</b>", use_markup=True), 1, 1, 1, 1)
        right_grid.attach(Gtk.Label("<b>Middle</b>", use_markup=True), 2, 1, 1, 1)
        right_grid.attach(Gtk.Label("<b>Ring</b>", use_markup=True), 3, 1, 1, 1)

        self.__right_fingers = []
        for i in range(4):
            area = Gtk.Box()
            area.set_size_request(-1, 35)
            area.get_style_context().add_class("finger-not-pressed")
            area.get_style_context().add_class("rounded-box")
            self.__right_fingers.append(area)

        for index, area in enumerate(self.__right_fingers):
            right_grid.attach(area, index, 2, 1, 1)

        middle_grid = Gtk.Grid(column_homogeneous=True, row_spacing=20)

        self.__store = Gtk.ListStore(str, str, str, str)
        self.__tree = Gtk.TreeView.new_with_model(self.__store)
        sel = self.__tree.get_selection()
        sel.set_mode(Gtk.SelectionMode.MULTIPLE)
        self.__tree.connect("size-allocate", self.__treeview_changed_cb)
        for index, header in enumerate(("Serial Data", "Hand", "Finger", "Action")):
            c = Gtk.TreeViewColumn(header, Gtk.CellRendererText(), text=index)
            c.set_expand(True)
            self.__tree.append_column(c)

        self.__sw = Gtk.ScrolledWindow(hscrollbar_policy=Gtk.PolicyType.NEVER, expand=True,
            kinetic_scrolling=True, vscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
            shadow_type=Gtk.ShadowType.ETCHED_OUT)
        self.__sw.add(self.__tree)

        bbox = Gtk.ButtonBox.new(Gtk.Orientation.HORIZONTAL)
        bbox.set_layout(Gtk.ButtonBoxStyle.EXPAND)
        bbox.get_style_context().add_class("linked")

        # replay = Gtk.Button.new_with_label("Replay")
        # replay.set_hexpand(True)
        clear = Gtk.Button.new_with_label("Clear")
        clear.set_hexpand(True)
        clear.connect("clicked", lambda button: self.__store.clear())
        save = Gtk.Button.new_with_label("Save")
        save.set_hexpand(True)
        save.connect("clicked", self.__save_cb)

        # bbox.pack_start(replay, True, True, 0)
        bbox.pack_start(clear, True, True, 0)
        bbox.pack_end(save, True, True, 0)

        middle_grid.attach(self.__sw, 0, 0, 1, 1)
        middle_grid.attach(bbox, 0, 1, 1, 1)

        self.pack_start(left_grid, True, True, 0)
        self.pack_start(Gtk.Separator.new(Gtk.Orientation.VERTICAL), False, True, 0)
        self.pack_start(middle_grid, True, True, 0)
        self.pack_start(Gtk.Separator.new(Gtk.Orientation.VERTICAL), False, True, 0)
        self.pack_end(right_grid, True, True, 0)

        self.set_view((0, 1, 1))

        # def create_gloves():
        #     g1 = GloveReader(self.set_view)
        #     g2 = GloveReader(self.set_view)

        # threading.Thread(name="glove-init", target=create_gloves, daemon=True).start()

    def __left_clear(self) -> None:
        for finger in self.__left_fingers:
            finger.get_style_context().add_class("finger-not-pressed")

    # def __replay_cb(self, button: Gtk.Button) -> None:

    def __right_clear(self) -> None:
        for finger in self.__right_fingers:
            finger.get_style_context().add_class("finger-not-pressed")

    def __save_cb(self, button: Gtk.Button) -> None:
        ts: Gtk.TreeSelection = self.__tree.get_selection()
        tree_model, tree_path = ts.get_selected_rows()

        for row in tree_path:
            print(tree_model[row])

    def __treeview_changed_cb(self, tree: Gtk.TreeView, rect: Gdk.Rectangle) -> None:
        adj = self.__sw.get_vadjustment()
        adj.set_value(adj.get_upper() - adj.get_page_size())

    # def replay_actions(self, actions: List[Tuple[int, int, int]]) -> None

    def set_view(self, data: Tuple[int, int, int]) -> None:
        # self.emit("button-pressed", data[0], data[1], data[2])

        if data[2] == 0:
            add_style_class = FINGER_NOT_PRESSED
            remove_style_class = FINGER_PRESSED
            action = Action.PRESSED.name.title()
        else:
            add_style_class = FINGER_PRESSED
            remove_style_class = FINGER_NOT_PRESSED
            action = Action.RELEASED.name.title()

        if data[0] == 0:
            finger = self.__left_fingers[3 - data[1]]
            finger.get_style_context().remove_class(remove_style_class)
            finger.get_style_context().add_class(add_style_class)
            hand = Hand.LEFT.name.title()
        else:
            finger = self.__right_fingers[data[1]]
            finger.get_style_context().remove_class(remove_style_class)
            finger.get_style_context().add_class(add_style_class)
            hand = Hand.RIGHT.name.title()

        self.__store.append(("({}, {}, {})".format(data[0], data[1], data[2]), hand,
            Finger[data[1]].name.title(), action))
