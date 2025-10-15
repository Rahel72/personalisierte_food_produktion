from pydobot import Dobot

port = "/dev/ttyACM0"
device = Dobot(port=port)

pose = device.get_pose()
print(pose)
position = pose.position
print(position)

device.move_to(position.x + 20, position.y, position.z, position.r) 
device.move_to(position.x, position.y, position.z, position.r) # we wait until this movement is done before continuing 
device.move_to(position.x, position.y + 20, position.z, position.r) 
device.move_to(position.x, position.y, position.z, position.r) # we wait until this movement is done before continuing

device.close()
