from robot_control_class import RobotControl
import time

robotcontrol = RobotControl(robot_name="summit")

def move_x_seconds(secs):
    robotcontrol.move_straight()#robot akan maju lurus
    time.sleep(secs)#berdasarkan detik
    robotcontrol.stop_robot()#rboto akan berhenti


move_x_seconds(5)
#robot akan bergerak dalam 5 detik saja.