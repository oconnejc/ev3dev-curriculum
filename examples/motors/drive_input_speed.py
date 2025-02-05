#!/usr/bin/env python3
"""
This demo lets you see how to use an input prompt to test different drive speeds.

Author: David Fisher.
"""

import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print("  Drive using input")
    print("--------------------------------------------")
    ev3.Sound.speak("Drive using input").wait()

    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    # Check that the motors are actually connected
    assert left_motor.connected
    assert right_motor.connected

    time_s = 1  # Any value other than 0.
    while time_s != 0:
        left_sp = 800
        right_sp = 800
        time_s = 5
        left_motor.run_forever(speed_sp=left_sp)
        right_motor.run_forever(speed_sp=right_sp)
        time.sleep(time_s)
        left_motor.stop()
        right_motor.stop(stop_action="brake")
        time_s = 0

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
