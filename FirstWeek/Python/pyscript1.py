from robot_control_class import RobotControl
#import class python bernama RobotControl [SabillyArtowibowo-1103204057]

rc = RobotControl()
#membuat variable rc untuk menyimpan type RobotControl

a = rc.get_laser(360)
#get_laser() merupakan cara yang sudah ada di class RobotControl
#360 adalah parameter
#output disimpan di variabel a

print ("The distance measured is: ", a, " m.")