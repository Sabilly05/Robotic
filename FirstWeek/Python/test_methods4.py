from robot_control_class import RobotControl

robotcontrol = RobotControl(robot_name="summit")

robotcontrol.turn("counter-clockwise", 0.3, 4)#berjalan lawan jarum jam 4 detik
robotcontrol.move_straight_time("forward", 0.3, 6)#berjalan maju 6 detik
robotcontrol.turn("counter-clockwise", 0.3, 4)#berjalan 4 detik lawan jarum jam
robotcontrol.move_straight_time("forward", 0.3, 7)#berjalan maju kembali 7 detik