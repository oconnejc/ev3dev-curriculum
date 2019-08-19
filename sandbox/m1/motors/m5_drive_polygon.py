#!/usr/bin/env python3
"""
This module lets you integrate your work on drive_inches and turn_degrees into a neat application.

You will ask the user for how many sides they would like in their polygon, the length of each side, and a speed.
Then your robot will drive that polygon shape.

Authors: David Fisher and Joe OConnell.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import robot_controller as robo
import time


def main():
    print("--------------------------------------------")
    print(" Drive polygon")
    print("--------------------------------------------")
    ev3.Sound.speak("Drive polygon").wait()
    robot = robo.Snatch3r()
    robot.drive_polygon(3, 40, 400)
    time.sleep(.5)
    robot.drive_polygon(4, 30, 800)
        # : 2. Individually implement the code here to use your drive_inches and turn_degrees library methods to
        # drive a polygon with the correct number of sides. (Hint: You will add 3 lines of code. What are they?).

        # : 3. Call over a TA or instructor to sign your team's checkoff sheet and do a code review.
        #   You are done with the Motors unit!
        #
        # Observations you should make, by making library functions you can make this program in only 3 lines of code.

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
