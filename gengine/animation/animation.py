import time
import threading
from itertools import chain
from typing import Literal, Union, List, Dict

from ..utils.uid import _UID
from .obj import BaseObj, BackColor, ForeColor


class PrintTemplate:
    """Contorol Screen"""

    def __init__(self, page_template: str):
        self.page_template = page_template
        self.itrate_count = 0
        self._clear_screen_to_back = 0

    def clear_lines(self):
        """get template line count and clear lines."""

        lines_number = self.page_template.count("\n") + 1 + self._clear_screen_to_back

        LINE_UP = "\033[1A"  # The ANSI code that is assigned to LINE_UP indicates that the cursor should move up a single line.
        LINE_CLEAR = "\x1b[2K"  # The ANSI code that is assigned to `LINE_CLEAR` erases the line where the cursor is located.

        for _ in range(lines_number):
            print(LINE_UP, end=LINE_CLEAR)

    def print_lines(self, *args, **kwargs):
        """clear last page_template lines and print page_template by new args"""

        if self.itrate_count > 0:
            self.clear_lines()
        self.itrate_count += 1

        print(self.page_template.format(*args, **kwargs))


class Animation(PrintTemplate):
    """Animation Engine"""

    def __init__(
        self,
        *,
        template_x: int = 100,
        template_y: int = 100,
        sleep_time=0.5,
        background_material: str = " ",
        background_material_color: str = ForeColor.RESET,
        background_color: str = BackColor.RESET,
    ):
        self.template_x = template_x
        self.template_y = template_y
        self._objs: dict[int, "BaseObj"] = {}
        self.sleep_time = sleep_time

        self.background_material = background_material[0]
        self.background_material_color = background_material_color
        self.background_color = background_color

        self._main_window = self._new_main_window()

        self.__active_main_screen_loop_id = None
        self.__is_main_loop_run = False
        self.__start_time = time.time()

        super().__init__(page_template=self.__get_new_page_template())

    def __str__(self) -> str:
        return f"<Animation ({self.template_x = }, {self.template_y = })>"

    def __get_new_page_template(self) -> str:
        line = ("{}" * self.template_x) + "\n"
        lines = line * self.template_y
        return lines

    def _sorted_objs(self) -> List[BaseObj]:
        """sort `Obj` by priority and return a new list"""
        filtered_objs = filter(lambda x: x.show, self._objs.values())
        sorted_objs = sorted(filtered_objs, key=lambda x: x.priority)
        return sorted_objs

    def _new_main_window(self) -> List[List[str]]:
        return [
            [
                f"{self.background_material_color}{self.background_color}{self.background_material}"
            ]
            * self.template_x
            for _ in range(self.template_y)
        ]

    def add_object(self, obj: "BaseObj"):
        self._objs.update({obj.uid: obj})

    def stop(self, clear: bool = False, print_all_time=False):
        self.__is_main_loop_run = False

        if clear:
            self.clear_lines()

        if print_all_time:
            print(f"End after {time.time() - self.__start_time:2f} seconds.")

    def start_main_screen_loop(self):
        self.__is_main_loop_run = True
        self.__active_main_screen_loop_id = _UID.get_uid()
        threading.Thread(
            target=self._main_screen_loop, args=[self.__active_main_screen_loop_id]
        ).start()

    def _main_screen_loop(self, screem_id):
        while (
            self.__is_main_loop_run and self.__active_main_screen_loop_id == screem_id
        ):
            self.show_objects()
    

    def show_line(self, shape_lines, obj, state):
        for line_index, line in enumerate(shape_lines):
            for char_index, char in enumerate(line):

                if char in ["", " "]:
                    continue

                char_x_locaion = char_index + obj.x
                char_y_locaion = line_index + obj.y

                # if Out of page
                if (
                    char_x_locaion >= self.template_x
                    or char_y_locaion >= self.template_y
                ):
                    continue

                obj.body_locations.append((char_x_locaion, char_y_locaion))

                if state.back_color != BackColor.RESET:
                    char = f"{state.back_color}{char}"

                self._main_window[char_y_locaion][
                    char_x_locaion
                ] = f"{state.fore_color}{char}"


    def show_objects(self):
        for obj in self._sorted_objs():

            state = obj.get_active_state()
            shape = state.next_shape()

            if not shape:
                continue
            obj.body_locations = []
            shape_lines = shape.value.split("\n")
            self.show_line(shape_lines, obj, state)
            
        row = chain.from_iterable(self._main_window)
        self.print_lines(*row)
        time.sleep(self.sleep_time)

        self._main_window = self._new_main_window()
