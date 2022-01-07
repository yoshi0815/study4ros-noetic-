#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from subprocess import call, Popen

flag = 0
def callback(data):
    global flag
    rospy.loginfo("recieved %s", data.data)
    now = rospy.Time.now()
    rospy.loginfo("now: %f", now.to_sec())
    flag = flag + 1
    print(flag)
    if flag == 10:
        call("rosnode kill /listener", shell=True)

def listener():
    rospy.init_node('listener')
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    print("fin")