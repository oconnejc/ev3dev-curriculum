import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    mqtt_client.send_message("print", ['possible stab wound, pt is a clear bottle'])
    root = tkinter.Tk()
    root.title("Pt Movement")
    frame1 = ttk.Frame(root, padding=20)
    frame1.grid()
    lift_pt = ttk.Button(frame1, text="Lift pt", command=lambda: mqtt_client.send_message("arm_up"))
    lift_pt.grid(row=0, column=0)
    lower_pt = ttk.Button(frame1, text="Lower pt", command=lambda: mqtt_client.send_message("arm_down"))
    lower_pt.grid(row=0, column=1)
    #lift_pt['command'] = lambda: mqtt_client.send_message("arm_up")
    #lower_pt['command'] = lambda: mqtt_client.send_message("arm_down")
    root.mainloop()





main()