import time
from gengine.animation import Animation, BaseObj, State, Shape

if __name__ == "__main__":
    MAIN_SCREEN_X = 50
    MAIN_SCREEN_Y = 8

    # create new object, his name is saman!
    saman = BaseObj(
        name="saman",
        active_state="stand",
        priority=1,
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
                name="walk-left",
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
                        """ [Go to Portal animation]

            |=======|                         (-|
            |       |                        ( -|
            |   |-| |                       (|._|
____________|   |'| |_____-."%`;__________ ("."\|
"""
                    ),
                    Shape(
                        """  Go to Portal animation

            |=======|                         ('|
            |       |                        (" |
            |   |-| |                       ( - |
____________|   |'| |_____-."%`;__________ (""; |
"""
                    ),
                    Shape(
                        """ [Go to Portal animation]

            |=======|                         (.|
            |       |                        (_ |
            |   |-| |                       (-._|
____________|   |'| |_____-."%`;__________ (-: .|
"""
                    ),
                    
                ],
            )
        },
    )

    # create main window
    animation = Animation(
        template_x=MAIN_SCREEN_X, template_y=MAIN_SCREEN_Y, sleep_time=0.2, background_material=" "
    )

    # add our object to main window
    animation.add_object(saman)
    animation.add_object(background)

    # start main screen
    animation.start_main_screen_loop()
    
    # move object saman 2 line sub
    saman.y += 2

    time.sleep(2)
    # 02

    # change state
    saman.active_state = "by"
    time.sleep(1)
    # 03

    # change state
    saman.active_state = "stand"
    time.sleep(0.2)
    # 03.2

    # change state and move object to right
    saman.active_state = "walk-right"
    for _ in range(50):
        saman.x += 1
        time.sleep(0.1)
    # 08.2

    # change state and move object to left
    saman.active_state = "walk-left"
    for _ in range(20):
        saman.x += -1
        time.sleep(0.05)
    # 09.2

    # change state
    saman.active_state = "by"
    time.sleep(2)
    # 11.2

    # change state and move object to right
    saman.active_state = "walk-right"
    for _ in range(30):
        saman.x += 1
        time.sleep(0.05)
    # 12.7

    # stop main loop and remove screen
    animation.stop(clear=True, print_all_time=True)
