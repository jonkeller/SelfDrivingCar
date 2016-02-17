from lidar_lite import Lidar_Lite

lidar = Lidar_Lite()
connected = lidar.connect(1)

if connected <= -1:
    print "Not Connected"
    exit(1)

print "Connected"
print "Distance:", lidar.getDistance(), "cm"
print "Velocity:", lidar.getVelocity()
