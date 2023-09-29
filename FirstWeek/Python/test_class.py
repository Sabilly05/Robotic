from robot_control_class import RobotControl

class MoveRobot:#buat kelas move robot
    def __init__(self, motion, clockwise, speed, time):#definisikan self, motion clockwise speed dan time
        self.robotcontrol = RobotControl(robot_name="summit")
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_turn = 7.0 # This is an estimate time in which the robot will rotate 90 degrees

    def do_square(self):#definisi untuk melakukan pergerakan kotak

        i = 0

        while (i < 4):
            self.move_straight()
            self.turn()
            i+=1

    def move_straight(self):
        self.robotcontrol.move_straight_time(self.motion, self.speed, self.time)

    def turn(self):
        self.robotcontrol.turn(self.clockwise, self.speed, self.time_turn)


mr1 = MoveRobot('forward', 'clockwise', 0.3, 4)#membuat robot bergerak maju dan searah jarum jam selama 4 detik
mr1.do_square()
mr2 = MoveRobot('forward', 'clockwise', 0.3, 8)#membuat robot bergerak maju dan searah jarum jam selama 8 detik
mr2.do_square()