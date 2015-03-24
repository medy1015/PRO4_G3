from Motors import Motor
import time as time
import logging
import sys

class Motors_Controllers:
     #   controlling both stepper motors
    
    
    def __init__(self, add1, add2):        
        self.motor1 = Motor(add1)
        self.motor2 = Motor(add2)

   #     '''The method below is called when u wants the robot to turn to the left with 90 degree'''
    def l(self):
	turn = int(round(15.80 * 90))
	self.motor1.resetPosition()
	self.motor2.resetPosition()
	self.motor1.setPosition(turn)
	self.motor2.setPosition(turn)

  #  '''The method below is called when u wants the robot to turn 180 degree'''
    def back(self):
	turn = int(round(15.80 * 180))
	self.motor1.resetPosition()
        self.motor2.resetPosition()
	self.motor1.setPosition(turn)
	self.motor2.setPosition(turn)
	
    #'''The method calls RDL method in the motor class'''
    def RDL(self):
        self.motor1.RDL()
        self.motor2.RDL()

  #  '''The method calls softStop method in the motor class'''    
    def softStop(self):
        self.motor1.softStop()
        self.motor2.softStop()

  #  '''The method calls setMotorParam method in the motor class'''
    def setMotorParam(self,fnum, snum):
        self.motor1.setMotorParam(1,3)
        self.motor2.setMotorParam(1,3)

  #  '''The method calls resetPosition method in the motor class'''
    def resetPosition(self):
        self.motor1.resetPosition()
        self.motor2.resetPosition()
        
  #  '''The method below is called when u wants the robot to turn to the right with 90 degree'''
    def r(self):
	turn = int(round(15.80 * 90))
        self.motor1.resetPosition()
        self.motor2.resetPosition()
        self.motor1.setPosition(-turn)
        self.motor2.setPosition(-turn)

  #  '''The method below is used when someone wants the robot to move a special range in cm. '''
    def go(self,dest):
        go = int(round(dest * 185))
        self.motor1.resetPosition()
        self.motor2.resetPosition()
        self.motor1.setPosition(-go)
        self.motor2.setPosition(go)

  #  '''The method is used to turn one of the directions according to the wanted direction'''
    def move_direction(self, direction):
        if(direction == "right"):
            self.r()
            time.sleep(0.5)
        elif(direction == "left"):
            self.l()
	    time.sleep(0.5)
        elif(direction =="forward"):
            print("ligeud")
        else:
            self.back()
            time.sleep(1.5)

  #  '''The method is used to turn an accurate degree to the left'''
    def turnLeftDegree(self,degree):
        turn = int(round(15.80 * degree))
        self.motor1.resetPosition()
        self.motor2.resetPosition()
        self.motor1.setPosition(turn)
        self.motor2.setPosition(turn)
        
 #   '''The method is used to turn an accurate degree to the left'''
    def turnRightDegree(self, degree):
        turn = int(round(-15.80 * degree))
        self.motor1.resetPosition()
        self.motor2.resetPosition()
        self.motor1.setPosition(turn)
        self.motor2.setPosition(turn)
