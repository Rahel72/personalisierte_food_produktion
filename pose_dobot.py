from dobotapi import Dobot

port = "/dev/ttyACM0"
device = Dobot(port=port, verbose=False)

# device.pose()

# pose = device.get_pose()
# position = pose.position
# print(position)
(x, y, z, r, j1, j2, j3, j4) = device.pose()
print(f"Aktuelle Position: x={x}, y={y}, z={z}, r={r}")
#device.move_to(200, 0, 30, 0, wait=True)

# device.suck(True)
# device.suck(False)


