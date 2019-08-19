import ev3dev.ev3 as ev3
import time
import robot_controller as robo
import mqtt_remote_method_calls as com

class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True



def main():
    print("--------------------------------------------")
    print("IR Remote")
    print(" - Use IR remote channel 1 to drive around")
    print("--------------------------------------------")
    robot = robo.Snatch3r()
    color_sensor = ev3.ColorSensor()
    color_sensor.MODE_COL_COLOR
    ir_sensor = ev3.InfraredSensor()
    beacon_seeker = ev3.BeaconSeeker(channel=1)
    assert color_sensor
    dc = DataContainer()
    my_delegate = MyDelegate()
    rc1 = ev3.RemoteControl(channel=1)
    rc1.on_red_up = lambda state: my_delegate.run_left(state, 1)
    rc1.on_red_down = lambda state: my_delegate.run_left(state, -1)
    rc1.on_blue_up = lambda state: my_delegate.run_right(state, 1)
    rc1.on_blue_down = lambda state: my_delegate.run_right(state, -1)
    rc2 = ev3.RemoteControl(channel=2)
    rc2.on_red_up = lambda state: my_delegate.arm_up()
    mqtt_client = com.MqttClient(my_delegate)
    my_delegate.mqtt_client = mqtt_client
    mqtt_client.connect_to_pc()





    while dc.running:
        rc1.process()
        rc2.process()
        color = color_sensor.color
        if color_sensor.color == 5:
            my_delegate.stop()

        time.sleep(0.01)




class MyDelegate(object):
    def __init__(self):
        self.robot = robo.Snatch3r()
        self.mqtt_client = None


    def loop_forever(self):
        btn = ev3.Button()
        while not btn.backspace:
            time.sleep(0.01)
        if self.mqtt_client:
            self.mqtt_client.close()
        self.robot.shutdown()

    def run_right(self, state, p_or_n):
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        if state:
            right_motor.run_forever(speed_sp=p_or_n * 800)
        else:
            right_motor.stop(stop_action='coast')

    def run_left(self, state, p_or_n):
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        if state:
            left_motor.run_forever(speed_sp=p_or_n * 800)
        else:
            left_motor.stop(stop_action='coast')

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

    def print(self, s):
        print(s)

    def stop(self):
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        left_motor.stop(stop_action='brake')
        right_motor.stop(stop_action='brake')
        ev3.Sound.speak('I see red stop').wait()

    def speak(self, s):
        ev3.Sound.speak(s).wait()

main()