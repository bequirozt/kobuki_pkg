#!/usr/bin/env python
import rospy
import time
import curses
import numpy as np
from geometry_msgs.msg import Twist
from rospy.numpy_msg import numpy_msg


def main(stdscr):

    global cmd

    rospy.init_node('keyboard_input', anonymous=True)

    pub = rospy.Publisher('kobuki/cmd_vel', numpy_msg(Twist))
    rate = rospy.Rate(50)

    stdscr.nodelay(True)
    key=""
    stdscr.clear()
    stdscr.scrollok(1)
    stdscr.addstr("Menu:\n")
    stdscr.addstr("Press S to stop the robot \n")
    stdscr.addstr("Press A to spin to the left \n")
    stdscr.addstr("Press D to spin to the right \n")
    stdscr.addstr("Press W to move forward \n")
    stdscr.addstr("Press S to move backwards \n")
    stdscr.addstr("Press Q to quit KeyOp \n")

    while not rospy.is_shutdown():
        try:
            key = str(stdscr.getkey())
            print key
            processKey(stdscr, key)
            # print cmd
            if key == '\n':
                break
        except Exception as e:
        # No input
            pass
            pub.publish(cmd)
            rate.sleep()

    # rospy.spin() 
    


def processKey(stdscr, key):
    global cmd
    stdscr.addstr("Detected key:")
    stdscr.addstr(key)
    stdscr.addstr("nn")
    if key == ' ' or key == 's' or key == 'S':
        stop(stdscr)
    elif key == 'q' or key == 'Q':
        quit(stdscr)
    elif key == 'KEY_LEFT' or key == 'KEY_RIGHT':
        changingAngular(stdscr, key)
    elif key == 'KEY_UP' or key == 'KEY_DOWN':
        changingLinear(stdscr, key)

def stop(stdscr):
    global cmd
    stdscr.addstr("Robot is stopping now\n")
    cmd.linear.x = 0.0
    cmd.angular.z = 0.0

def quit(stdscr):
    stdscr.addstr("Exiting node\n")
    rospy.signal_shutdown("Manual shutdown\n")

def changingAngular(stdscr, key):
    global cmd
    stdscr.addstr("Changing angular speed\n")
    if key == 'KEY_LEFT':
        cmd.angular.z = cmd.angular.z + angularStep
    if cmd.angular.z > 180:
        cmd.angular.z = 180.0
    elif key == 'KEY_RIGHT':
        cmd.angular.z = cmd.angular.z - angularStep
    if cmd.angular.z < -180:
        cmd.angular.z = -180.0

def changingLinear(stdscr, key):
    global cmd
    stdscr.addstr("Changing linear speed\n")
    if key == 'KEY_UP':
        cmd.linear.x = cmd.linear.x + linearStep
    if cmd.linear.x > 1:
        cmd.linear.x = 1.0
    elif key == 'KEY_DOWN':
        cmd.linear.x = cmd.linear.x - linearStep
    if cmd.linear.x < -1:
        cmd.linear.x = -1.0

cmd = Twist()
cmd.linear.x = 0.0
cmd.linear.y = 0.0
cmd.linear.z = 0.0
cmd.angular.x = 0.0
cmd.angular.y = 0.0
cmd.angular.z = 0.0
linearStep = 1
angularStep = np.pi*.7
curses.wrapper(main)
