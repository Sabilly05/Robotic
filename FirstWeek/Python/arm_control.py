from smart_grasping_sandbox.smart_grasper import SmartGrasper
from tf.transformations import quaternion_from_euler
from math import pi
import time

sgs = SmartGrasper()

sgs.pick()

sgs.reset_world()

#Introduction robotic w/ python grasper. [Sabilly Artowibowo - 1103204057]