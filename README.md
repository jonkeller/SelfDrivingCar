# SelfDrivingCar

This is a work in progress.
So far it's just some scripts to test isolated components.

runtRover.py will be the main script, but it currently does nothing.

I'll add photos and circuit diagrams. The car currently consists of:
* 4 motors to control the wheels. The left wheels operate together, and the right wheels operate together. The motors are controlled by an L293D chip.
* A LIDAR. This was previously on a metal mast that was rotated by a stepper motor, and the code still reflects that. But to save weight I recently removed the mast and stepper, and replaced them with a small servo-controlled pan/tilt. I have not written code for that yet.
* A 10-DOF IMU. I haven't written code for that yet, either. I'm not sure if I will...my drone project probably needs the IMU more than the car does.
* 2 ultrasonic rangefinders. Ditto re: drone.

