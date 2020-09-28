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
    stdscr.addstr("Forward: KEY_UP \n")
    stdscr.addstr("Backward: KEY_DOWN \n")
    stdscr.addstr("Left: KEY_LEFT \n")
    stdscr.addstr("Right: KEY_RIGHT \n")
    stdscr.addstr("Stop: SPACE BAR \n")
    stdscr.addstr("Quit: Q \n")

    while not rospy.is_shutdown():
        try:
            key = str(stdscr.getkey())
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
    # stdscr.addstr("Detected key:")
    # stdscr.addstr(key)
    # stdscr.addstr("nn")
    if key == ' ':
        stop(stdscr)
    elif key == 'q' or key == 'Q':
        quit(stdscr)
    elif key == 'KEY_LEFT' or key == 'KEY_RIGHT':
        changingAngular(stdscr, key)
    elif key == 'KEY_UP' or key == 'KEY_DOWN':
        changingLinear(stdscr, key)

def stop(stdscr):
    global cmd
    # stdscr.addstr("Robot is stopping now\n")
    cmd.linear.x = 0.0
    cmd.angular.z = 0.0

def quit(stdscr):
    # stdscr.addstr("Exiting node\n")
    rospy.signal_shutdown("Manual shutdown\n")

def changingAngular(stdscr, key):
    global cmd
    # stdscr.addstr("Changing angular speed\n")
    if key == 'KEY_LEFT':
        cmd.angular.z = cmd.angular.z + angular_step
    if cmd.angular.z > angular_limit:
        cmd.angular.z = angular_limit
    elif key == 'KEY_RIGHT':
        cmd.angular.z = cmd.angular.z - angular_step
    if cmd.angular.z < -angular_limit:
        cmd.angular.z = -angular_limit

def changingLinear(stdscr, key):
    global cmd
    # stdscr.addstr("Changing linear speed\n")
    if key == 'KEY_UP':
        cmd.linear.x = cmd.linear.x + linear_step
    if cmd.linear.x > linear_limit:
        cmd.linear.x = linear_limit
    elif key == 'KEY_DOWN':
        cmd.linear.x = cmd.linear.x - linear_step
    if cmd.linear.x < -linear_limit:
        cmd.linear.x = -linear_limit

cmd = Twist()
cmd.linear.x = 0.0
cmd.linear.y = 0.0
cmd.linear.z = 0.0
cmd.angular.x = 0.0
cmd.angular.y = 0.0
cmd.angular.z = 0.0
linear_limit = 1
linear_step = linear_limit*.1
angular_limit = np.pi 
angular_step = angular_limit*.1
curses.wrapper(main)
