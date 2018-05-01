import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import json
import logging
import sys
import vlc

from typing import Any, Dict, Set, Tuple, Union, List

sys.path.append(sys.path[0] + "/..")

from .button_grid import ButtonGrid
from .button_info import ButtonInfo
from .event_set import EventSet
from glove_interpreter import Hand, Action
from .headerbar import HeaderBar
from .serial_visualizer import SerialVisualizer

log: logging = logging.getLogger(__name__)

# SOUNDS = {
#     0: "/home/joseph/Downloads/music/386721_5999918-lq.mp3",
#     1: "/home/joseph/Downloads/music/386722_5999918-lq.mp3",
#     2: "/home/joseph/Downloads/music/386723_5999918-lq.mp3",
#     3: "/home/joseph/Downloads/music/386724_5999918-lq.mp3",
#     4: "/home/joseph/Downloads/music/386725_5999918-lq.mp3",
#     5: "/home/joseph/Downloads/music/386726_5999918-lq.mp3",
#     6: "/home/joseph/Downloads/music/386727_5999918-lq.mp3",
# }

SOUNDS = {
    0: "/home/joseph/Downloads/piano/68437__pinkyfinger__piano-a.wav",
    1: "/home/joseph/Downloads/piano/68438__pinkyfinger__piano-b.wav",
    2: "/home/joseph/Downloads/piano/68439__pinkyfinger__piano-bb.wav",
    3: "/home/joseph/Downloads/piano/68440__pinkyfinger__piano-c.wav",
    4: "/home/joseph/Downloads/piano/68441__pinkyfinger__piano-c.wav",
    5: "/home/joseph/Downloads/piano/68442__pinkyfinger__piano-d.wav",
    6: "/home/joseph/Downloads/piano/68443__pinkyfinger__piano-e.wav",
    7: "/home/joseph/Downloads/piano/68444__pinkyfinger__piano-eb.wav",
    8: "/home/joseph/Downloads/piano/68445__pinkyfinger__piano-f.wav",
    9: "/home/joseph/Downloads/piano/68446__pinkyfinger__piano-f.wav",
    10: "/home/joseph/Downloads/piano/68447__pinkyfinger__piano-g.wav",
    11: "/home/joseph/Downloads/piano/68448__pinkyfinger__piano-g.wav",
}


class MainWindow(Gtk.ApplicationWindow):
    """
    The main application window
    """

    __left_button_grid: ButtonGrid = None
    __right_button_grid: ButtonGrid = None
    __left_event_set: Set[int] = None
    __right_event_set: Set[int] = None
    __button_info: ButtonInfo = None
    __data: Dict[str, Any] = None
    __file_filter: Gtk.FileFilter = None
    __serial_visualizer: SerialVisualizer = None
    __grid: Gtk.Grid = None
    __headerbar: HeaderBar = None
    __revealer: Gtk.Revealer = None
    __reveal_button: Gtk.Button = None
    __reveal_image: Gtk.Image = None

    # VLC players
    __vlc_instance: vlc.Instance = vlc.Instance()
    __player_left: vlc.MediaPlayer = __vlc_instance.media_player_new()
    __player_right: vlc.MediaPlayer = __vlc_instance.media_player_new()
    __left_active_fingers: List[int] = []
    __right_active_fingers: List[int] = []

    def __init__(self):
        Gtk.ApplicationWindow.__init__(self)

        self.__file_filter = Gtk.FileFilter()
        self.__file_filter.set_name("JSON files")
        self.__file_filter.add_mime_type("application/json")

        # Create Media sounds TODO: fix me for json
        self.__left_sounds: List[vlc.Media] = [self.__vlc_instance.media_new(SOUNDS[x]) for x in
            SOUNDS]  # TODO: make this dict again
        self.__right_sounds: List[vlc.Media] = []

        with open("./config/default.json") as f:
            self.__data = json.load(f)

        self.__left_event_set = set()
        self.__right_event_set = set()

        self.set_border_width(10)

        self.__headerbar = HeaderBar()
        self.__headerbar.connect("save", self.__save_cb)
        self.set_titlebar(self.__headerbar)

        main_grid = Gtk.Grid(column_spacing=20, row_spacing=20, margin=10)

        self.__left_button_grid = ButtonGrid([self.__data[x]["name"] for x in list(self.__data.keys())[:16]])
        self.__left_button_grid.connect("button-clicked", self.__setup_button_info_cb)
        self.__right_button_grid = ButtonGrid([self.__data[x]["name"] for x in list(self.__data.keys())[16:32]])
        self.__right_button_grid.connect("button-clicked", self.__setup_button_info_cb)
        self.__reveal_image = Gtk.Image.new_from_icon_name("pan-start-symbolic",
            Gtk.IconSize.BUTTON)
        self.__reveal_button = Gtk.Button()
        # self.__reveal_button.get_style_context().add_class("not-rounded-button")
        self.__reveal_button.set_image(self.__reveal_image)
        self.__reveal_button.connect("clicked", self.__revealer_cb)
        self.__button_info = ButtonInfo()
        self.__button_info.connect("close-revealer", self.__revealer_cb)
        self.__button_info.connect("done-editing", self.__update_data_cb)
        self.__revealer = Gtk.Revealer(transition_type=Gtk.RevealerTransitionType.SLIDE_LEFT)
        self.__revealer.add(self.__button_info)
        self.__serial_visualizer = SerialVisualizer()
        self.__serial_visualizer.connect("button-pressed", self.__update_sound)

        main_grid.attach(Gtk.Label("<big>Left Hand Combinations</big>", use_markup=True),
            0, 0, 1, 1)
        main_grid.attach(Gtk.Label("<big>Right Hand Combinations</big>", use_markup=True),
            1, 0, 1, 1)
        main_grid.attach(self.__left_button_grid, 0, 1, 1, 1)
        main_grid.attach(self.__right_button_grid, 1, 1, 1, 1)
        main_grid.attach(self.__reveal_button, 2, 1, 1, 1)
        main_grid.attach(self.__revealer, 3, 1, 1, 1)
        main_grid.attach(Gtk.Label("Button labels are binary representations of finger "
            "combinations:\nThumb: 2^0, Index: 2^1, Middle: 2^2, Ring: 2^3",
            justify=Gtk.Justification.CENTER), 0, 2, 4, 1)
        main_grid.attach(self.__serial_visualizer, 0, 3, 4, 1)

        self.add(main_grid)

    def __revealer_cb(self, object: Union[ButtonInfo, Gtk.Button]) -> None:
        """Close the revealer"""
        # Refactor into 2 different methods? open_revealer and close_revealer
        if self.__revealer.get_child_revealed():
            self.__revealer.set_reveal_child(False)
            self.__reveal_image.set_from_icon_name("pan-start-symbolic", Gtk.IconSize.BUTTON)
        else:
            self.__revealer.set_reveal_child(True)
            self.__reveal_image.set_from_icon_name("pan-end-symbolic", Gtk.IconSize.BUTTON)

    def __save_cb(self, header: HeaderBar, file_name: str) -> None:
        if file_name is None:
            dialog = Gtk.FileChooserNative.new("Choose file to save to", self,
            Gtk.FileChooserAction.SAVE, "_Save", "_Cancel")
            dialog.set_do_overwrite_confirmation(True)
            dialog.add_filter(self.__file_filter)

            response = dialog.run()
            if response == Gtk.ResponseType.ACCEPT:
                file_name = dialog.get_filename()
                if file_name[:4] != ".json":
                    file_name = file_name + ".json"

            dialog.destroy()

        if file_name is not None:
            with open(file_name, "w") as f:
                json.dump(self.__data, f, indent=2)
            self.__headerbar.set_subtitle(file_name)

    def __setup_button_info_cb(self, button_grid: ButtonGrid, label: str) -> None:
        if not self.__revealer.get_child_revealed():
            self.__revealer.set_reveal_child(True)
            self.__reveal_image.set_from_icon_name("pan-end-symbolic", Gtk.IconSize.BUTTON)
        hand = Hand.LEFT if button_grid is self.__left_button_grid else Hand.RIGHT
        key = "{}{:004b}".format(hand.value, int(label))
        self.__button_info.set_info("{} {}".format(hand.name.title(), label), **self.__data[key])

    def __update_data_cb(self, button_info: ButtonInfo, label: str, path: str):
        label_split = label.split()
        hand = label_split[0].lower()
        key = "{}{:004b}".format(Hand.LEFT if hand == Hand.LEFT.name.lower() else Hand.RIGHT,
            int(label_split[1]))
        print(key)
        self.__data[key]["path"] = path

    def __update_sound(self, sv: SerialVisualizer, hand: int, finger: int, action: int):
        player = self.__player_left if hand == Hand.LEFT else self.__player_right
        active_fingers = self.__left_active_fingers if hand == Hand.LEFT else self.__right_active_fingers
        sounds = self.__left_sounds if hand == Hand.LEFT else self.__right_sounds

        finger += 1
        if finger not in active_fingers and action == Action.PRESSED:
            active_fingers.append(finger)
        elif action == Action.RELEASED:
            del active_fingers[active_fingers.index(finger)]

        print(Hand[hand], sum(active_fingers), active_fingers)
        if len(active_fingers) > 0:
            sound = sounds[sum(active_fingers)]
            player.set_media(sound)
            player.play()
        else:
            player.stop()
            # event_set.mp.pause()
            # FIXME pause and loop back when done
            # FIXME does a thread help this
