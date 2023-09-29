from robot_control_class import RobotControl

num = int(input("Select a number between 0 and 719: "))
# meminta user untuk input angka antara 0 sampai 719

rc = RobotControl()
a = rc.get_laser(num)
#metode dapat data laser beam berdasarkan angka user sbg parameter

print ("The laser value received is: ", a)