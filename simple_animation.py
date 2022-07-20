import time

from gengine import Animation, Obj, State, Shape

if __name__ == "__main__":
    saman = Obj(
        name="saman",
        active_state="stand",
        states={
            "stand": State(
                name="stand",
                shapes=[
                    Shape(
                        """
 0
/?\\
 |)
    """
                    ),
                    Shape(
                        """
 O
/?\\
 |)
    """
                    ),
                ],
            ),
            "by": State(
                name="by",
                shapes=[
                    Shape(
                        """
 0 /
/?
/|
    """
                    ),
                    Shape(
                        """
 O)
/?
/|
    """
                    ),
                ],
            ),
            "walk-right": State(
                name="walk-right",
                shapes=[
                    Shape(
                        """
 0
/?\\
 |
    """
                    ),
                    Shape(
                        """
 O
(?
 |\\
    """
                    ),
                ],
            ),
            "walk-left": State(
                name="walk-right",
                shapes=[
                    Shape(
                        """
 0
/?\\
 |
    """
                    ),
                    Shape(
                        """
 O
 \?)
 /|
    """
                    ),
                ],
            ),
        },
    )

    animation = Animation(
        template_x=50, template_y=5, sleep_time=0.2, background_material=" "
    )
    animation.add_object(saman)
    animation.start_main_screen_loop()

    time.sleep(2)
    # 02

    saman.active_state = "by"
    time.sleep(1)
    # 03

    saman.active_state = "stand"
    time.sleep(0.2)
    # 03.2

    saman.active_state = "walk-right"
    for _ in range(50):
        saman.x += 1
        time.sleep(0.1)
    # 08.2

    saman.active_state = "walk-left"
    for _ in range(20):
        saman.x += -1
        time.sleep(0.05)
    # 09.2

    saman.active_state = "by"
    time.sleep(2)
    # 11.2

    saman.active_state = "walk-right"
    for _ in range(30):
        saman.x += 1
        time.sleep(0.05)
    # 12.7

    animation.stop(clear=True, print_all_time=True)
