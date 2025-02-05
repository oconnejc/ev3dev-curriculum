"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time

class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""
    
    # : Implement the Snatch3r class as needed when working the sandox exercises
    # (and delete these comments)

    def drive_inches(self, inc ,sp):
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

        # Check that the motors are actually connected
        assert left_motor.connected
        assert right_motor.connected

        stop_action = "brake"
        degrees_per_inch = 90
        motor_turns_needed_in_degrees = inc * degrees_per_inch
        position_sp = motor_turns_needed_in_degrees

        while position_sp != 0:

            left_motor.run_to_rel_pos(speed_sp=sp, position_sp=position_sp, stop_action=stop_action)
            right_motor.run_to_rel_pos(speed_sp=sp, position_sp=position_sp, stop_action=stop_action)

            left_motor.wait_while(ev3.Motor.STATE_RUNNING)
            ev3.Sound.beep().wait()
            position_sp = 0

    def turn_degrees(self, degrees_to_turn, turn_speed_sp):
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

        # Check that the motors are actually connected
        assert left_motor.connected
        assert right_motor.connected

        stop_action = "brake"

        while degrees_to_turn != 0:

            left_motor.run_to_rel_pos(speed_sp=turn_speed_sp, position_sp=-degrees_to_turn * 90/17, stop_action=stop_action)
            right_motor.run_to_rel_pos(speed_sp=turn_speed_sp, position_sp=degrees_to_turn * 90/17, stop_action=stop_action)

            left_motor.wait_while(ev3.Motor.STATE_RUNNING)
            ev3.Sound.beep().wait()
            degrees_to_turn = 0

    def drive_polygon(self,number_of_sides, length, speed):
        for k in range(number_of_sides):
            self.drive_inches(length,speed)
            self.turn_degrees(360/ number_of_sides, speed)

    def arm_calibration(self):
        touch_sensor = ev3.TouchSensor()
        MAX_SPEED = 900
        arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        assert arm_motor.connected
        assert touch_sensor
        arm_motor.run_forever(speed_sp=MAX_SPEED)
        while not touch_sensor.is_pressed:
            time.sleep(0.01)
        arm_motor.stop()
        print('arm is up')
        ev3.Sound.beep().wait()

        arm_revolutions_for_full_range = 14.2 * 360
        arm_motor.run_to_rel_pos(position_sp=-arm_revolutions_for_full_range, speed_sp=MAX_SPEED)
        arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

        arm_motor.position = 0
        print('arm calibrated')

    def arm_up(self):
        MAX_SPEED = 900
        arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        assert arm_motor.connected

        touch_sensor = ev3.TouchSensor()
        assert touch_sensor
        arm_motor.run_forever(speed_sp=MAX_SPEED)
        while not touch_sensor.is_pressed:
            time.sleep(0.01)
        arm_motor.stop()
        print('arm is up')

    def arm_down(self):
        MAX_SPEED = 900
        arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        assert arm_motor.connected

        touch_sensor = ev3.TouchSensor()
        assert touch_sensor
        arm_motor.run_to_abs_pos(position_sp=0, speed_sp=MAX_SPEED)
        arm_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def shutdown(self):
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        left_motor.stop()
        right_motor.stop()
        arm_motor.stop()
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        print('goodbye')
        ev3.Sound.speak("Goodbye").wait()

