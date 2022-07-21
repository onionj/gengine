import time
from gengine.animation import Animation, BaseObj, State, Shape, BackColor, ForeColor


if __name__ == "__main__":
    MAIN_SCREEN_X = 50
    MAIN_SCREEN_Y = 10

    # create simple background
    background = BaseObj(
        name="background",
        active_state="light",
        priority=0,
        states={
            "light": State(
                name="light",
                shapes=[
                    Shape(
                        """ 
            /-------\\
            |=======|                     
            |#######|                     
            |###|-|#|                     
____________|###|'|#|_____-."%`;_________________

[Go to Portal animation]
"""
                    )
                ],
            )
        },
    )

    # create new object, his name is saman!
    saman = BaseObj(
        name="saman",
        active_state="stand",
        priority=3,
        x=2,
        y=3,
        states={
            "stand": State(
                name="stand",
                fore_color=ForeColor.RED,
                shapes=[
                    Shape(
                        """
 0
/.\\
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
                fore_color=ForeColor.RED,
                shapes=[
                    Shape(
                        """  by
 0 /
/?
/|
    """
                    ),
                    Shape(
                        """  By
 O)
/?
/|
    """
                    ),
                ],
            ),
            "walk-right": State(
                name="walk-right",
                fore_color=ForeColor.RED,
                shapes=[
                    Shape(
                        """
 0
/?\\
/
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
                name="walk-left",
                fore_color=ForeColor.RED,
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

    # create simple portal
    portal = BaseObj(
        name="portal",
        active_state="open",
        priority=4,
        x=MAIN_SCREEN_X - 6,
        y=2,
        show=False,
        states={
            "open": State(
                name="open",
                back_color=BackColor.CYAN,
                shapes=[
                    Shape(
                        """
   |-|
  (--)
 |=|_|
|"."\)
"""
                    ),
                    Shape(
                        """
   (') 
  ("/| 
 (--') 
("";-)
"""
                    ),
                    Shape(
                        """
   (.)
  |_*) 
 (-.-)
(-:*.| 
"""
                    ),
                ],
            )
        },
    )

    # create main window
    animation = Animation(
        template_x=MAIN_SCREEN_X,
        template_y=MAIN_SCREEN_Y,
        sleep_time=0.15,
        background_material=" ",

    )

    # add our object to main window
    animation.add_object(background)
    animation.add_object(portal)
    animation.add_object(saman)

    # start main screen
    animation.start_main_screen_loop()

    time.sleep(1)

    # change state
    saman.active_state = "stand"
    time.sleep(0.2)

    # open portal!
    portal.show = True

    # change state and move object to right
    saman.active_state = "walk-right"
    for _ in range(50):
        saman.x += 1
        time.sleep(0.1)

    # close portal
    portal.show = False
    time.sleep(0.5)

    # open portal!
    portal.show = True

    # change state and move object to left
    saman.active_state = "walk-left"
    for _ in range(20):
        saman.x += -1
        time.sleep(0.02)

    # change state
    saman.active_state = "by"
    time.sleep(1)

    # change state and move object to right
    saman.active_state = "walk-right"
    for _ in range(25):
        saman.x += 1
        time.sleep(0.05)

    # close portal
    portal.show = False

    time.sleep(1)

    # stop main loop and remove screen
    animation.stop(clear=True, print_all_time=True)
