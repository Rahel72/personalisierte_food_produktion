from pydobot import Dobot

port = "/dev/ttyACM0"
device = Dobot(port=port)

pose = device.get_pose()
print(pose)
position = pose.position
print(position)
