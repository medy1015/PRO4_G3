''''
Created on May 24, 2014

@author: Ayman Zaki
'''

import smbus
import time as time
import math

from random import randint
from IRSensors import IRSensor
from MotorsController import Motors_Controllers
from Map import Mapping


theta =0

#This class corrects the position of the rvoer when it is needed, and it also initializes the sensors and motors-controllers classes
class AutoCorrect:
    def __init__(self):
        self.sensor=IRSensor()
        self.motors = Motors_Controllers(0x61,0x69)
# This method implements the chosen model for correcting the rover's position  
    def auto_correct(self,against_r,against_l):
        global d
        global theta
        global actualDist
        leftdist = 0
        rightdist = 0

        if(against_r > 0.0):
            leftdist=1
        if(against_l > 0.0):
            rightdist=1
        left= self.sensor.get_left_sensor()   
        right=self.sensor.get_right_sensor()
        error=(left + right + 11)
        a=33
        
        if(error > a):
            theta = (math.degrees(math.acos(a/error)))*0.9
            if(theta < 0):
                theta= theta * -1
            frac=math.cos(theta)
            actualDist= 10 * frac                                          
            if(actualDist<0):
                actualDist=actualDist*-1
           
            if(leftdist == 1 and rightdist !=1):          
                self.motors.turnRightDegree(theta)
                time.sleep(0.01)
                time.sleep(1.5)

 
            elif(leftdist !=1 and rightdist ==1):
                self.motors.turnLeftDegree(theta)
                time.sleep(0.01)
                time.sleep(1.5)
        return theta
    
#This method gets the reading from right sensor
    def get_right_sensor(self):
        sr=0
        if(self.sensor.readRightSensor() < 33):
            sr =sr + self.sensor.readRightSensor()  
        else:
            sr = 33
        return sr
#This method gets the reading from left sensor        
    def get_left_sensor(self):
        sl=0
        if(self.sensor.readLeftSensor() < 33):
            sl =sl + self.sensor.readLeftSensor()  
        else:
            sl = 33
        return sl
    
#This method gets the reading from front sensor
    def get_front_sensor(self):
        sf=0
        if(self.sensor.readFrontSensor() < 33):
            sf =sf + self.sensor.readFrontSensor()  
        else:
            sf = 33
        return sf
    
#This method calcultes the total measured distance from wall to wall included the rover width
#and calculates the difference between the measured value and the ideal value   
    def get_sensors_reading(self):
        robot_width = 11
        cell_width = 33
        left=self.get_left_sensor()
        right=self.get_right_sensor()
        reading = left + right
        diff = (reading+robot_width) - cell_width
        return diff

    def get_motors(self):
        return self.motors

    def get_theta(self):
        return theta







