from ..utils.uid import _UID


class Shape:
    """States Shape"""

    def __init__(self, shape: str):
        self.value = shape

    def __str__(self):
        return f"<class Shape, \n{self.shape}\n>"


class State:
    """Objects State"""

    def __init__(self, name: str, shapes: list[Shape], color_code: str = None):
        self.shapes = shapes
        self.color_code = color_code
        self.name = name

        self.__next_shape_idx = 0

    def __str__(self):
        return f"<class State, name: {self.name}, Color:{self.color}, Shapes count:{len(self.shapes)}>"

    def active_shape(self) -> Shape:
        """ring loop for return shape"""

        shapes_count = len(self.shapes)

        if shapes_count == 0:
            return False

        if self.__next_shape_idx == shapes_count:  # index out of range
            self.__next_shape_idx = 1
            return self.shapes[0]

        else:
            shape = self.shapes[self.__next_shape_idx]
            self.__next_shape_idx += 1
            return shape


class BaseObj:
    """Animation object"""

    def __init__(
        self,
        name: str,
        states: dict[str, State],
        active_state: str,
        x: int = 1,
        y: int = 1,
        priority: int = 0,
        show: bool = True,
    ):
        self.name = name
        self.states = states
        self.active_state = active_state
        self.x = x
        self.y = y
        self.priority = priority
        self.show = show

        self.body_locations: list[tuple[int, int]] = []  # [(x, y),]
        self.uid: int = _UID.get_uid()

    def __str__(self):
        return f"""<class BaseObj, uid:{self.uid}, x:{self.x}, y:{self.y}, show:{self.show}, priority:{self.priority}, states_count:{len(self.states)}, active_state:{self.active_state}>"""

    def state_names(self) -> list[str]:
        return self.states.keys()

    def get_shape(self) -> Shape:
        active_state = self.states.get(self.active_state)

        if active_state:
            return active_state.active_shape()
        return False
