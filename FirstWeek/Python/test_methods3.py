from robot_control_class import RobotControl

robotcontrol = RobotControl(robot_name="summit")

robotcontrol.move_straight_time("forward", 0.3, 5) #robot berjalan selama 5 detik kedepan dengan kecepatan 0,3m/s
robotcontrol.turn("clockwise", 0.3, 7)# robot akan berputar searah jarum jam selama 7 detik di kecepatan 0,3 rad/s