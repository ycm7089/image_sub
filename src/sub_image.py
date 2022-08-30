#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageConvert :
    def __init__(self):
        print("!")
        self.bridge = CvBridge()
        
        self.color_sub = rospy.Subscriber("/cm3/image_color", Image, self.color_callback)
        self.thermal_sub = rospy.Subscriber("/thermal/image_raw", Image, self.thermal_callback)

    def color_callback(self, color_msg):
        # Convert your ROS Image message to OpenCV2
        self.color_cv2_img = self.bridge.imgmsg_to_cv2(color_msg, "bgr8")
        # print(self.color_cv2_img.shape)

        # resize image 
        self.color_resize_img = cv2.resize(self.color_cv2_img,(800, 600))

        # cv2.imshow('Color window', self.color_resize_img)
        # cv2.waitKey(0)

    def thermal_callback(self, thermal_msg):
        self.thermal_cv2_img = self.bridge.imgmsg_to_cv2(thermal_msg, "mono8")
        print(self.thermal_cv2_img.shape)

        # resize image 
        self.thermal_resize_img = cv2.resize(self.thermal_cv2_img,(800, 600))
        cv2.imshow('Thermal window',self.thermal_resize_img)
        # self.show_img()
        cv2.waitKey(0)

if __name__ == '__main__':
    rospy.init_node('camera_listener')
    try:
        cm_image_sub = ImageConvert()

        rospy.spin()
    except :
        print("NO")
