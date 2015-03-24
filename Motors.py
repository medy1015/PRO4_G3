''''
Created on Oct 6, 2013

@author: slavegnuen
'''
#from TMC222Status import TMC222Status
import smbus
import time as time
import math
from random import randint



'class variables:'
i2c=smbus.SMBus(1)

#Motor commands:        ByteCode:    Description:
cmdGetFullStatus1     = 0x81       # Returns complete status of the chip
cmdGetFullStatus2     = 0xFC       # Returns actual, target and secure position
cmdGetOTPParam        = 0x82       # Returns OTP parameter
cmdGotoSecurePosition = 0x84       # Drives motor to secure position
cmdHardStop           = 0x85       # Immediate full stop
cmdResetPosition      = 0x86       # Sets actual position to zero
cmdResetToDefault     = 0x87       # Overwrites the chip RAM with OTP contents
cmdRunInit            = 0x88       # Reference Search
cmdSetMotorParam      = 0x89       # Sets motor parameter
cmdSetOTPParam        = 0x90       # Zaps the OTP memory
cmdSetPosition        = 0x8B       # Programmers a target and secure position
cmdSoftStop           = 0x8F       # Motor stopping with deceleration phase
minVelocity           = 2
stepModeByte          = 15
currentByte           = 0x92

class Motor:
'
    
    def __init__(self,devAddress):
        self.devAddress=devAddress
        self.bus = smbus.SMBus(1)

       # '''Status of circuit and stepper motor'''no
    def getFullStatus1(self):

        response = self.bus.read_i2c_block_data(self.devAddress, cmdGetFullStatus1, 9)
        return response

        #'''Status of the position of the stepper motor'''
    def getFullStatus2(self):
        response = self.bus.read_i2c_block_data(self.devAddress, cmdGetFullStatus2,9)
        return response

        #'''Read OTP *One-Time Programmable) memory'''
    def getOTPParam(self):
        return self.bus.write_byte(self.devAddress, cmdGetOTPParam)

        #'''The method is used for the rover to make a hard stop'''
    def hardStop(self):
        self.bus.write_byte(self.devAddress, cmdHardStop)

   # '''The method is called so the rover able to move'''
    def RDL(self):
        global motor1
        global motor2
	motor1 = Motor(0x61)
	motor2 = Motor(0x69)	
	motor1.getFullStatus1()
	motor2.getFullStatus1()	
    #'''The method is called for reseting the position of the rover'''
    def resetPosition(self):
        self.bus.write_byte(self.devAddress, cmdResetPosition)
    
        '''Set the stepper motor parameters in the RAM:

           Byte 1: 0xFF
           Byte 2: 0xFF
           Byte 3: 7-4=Coil peak current value (Irun), 3-0=Coil hold current value (Ihold)
           Byte 4: 7-4=Max velocity, 3-0=Min velocity
           Byte 5: 7-5=Secure position, 4=Motion direction, 3-0=Acceleration
           Byte 6: 7-0=Secure position of the stepper motor
           Byte 7: 4=Acceleration shape, 3-2=Stepmode    '''
        
    #'''The method is used to set all of the motors parameter'''
    def setMotorParam(self,direction,maxVelocity):
        byte3=0b10100100#currentByte0x92
        byte4=0b10100010#0b10100010 maxVelocity << 4 | minVelocity<<0#12
        byte5=0b10100010#0b10100010
        byte6=0b00000010# 0b00000010
        byteCode = [0xFF, 0xFF,byte3, byte4, byte5, byte6, stepModeByte]
        self.bus.write_i2c_block_data(self.devAddress, cmdSetMotorParam, byteCode)

    #'''The method is used for changing the acceleration of the rover'''
    def setAcceleration(self, direction, acc):
        byte5=((0x80 & 0xF0) | direction << 4 | acc )
        byteCode = [0xFF, 0xFF, currentByte, 0x11, byte5, 0x00, stepModeByte]
        self.bus.write_i2c_block_data(self.devAddress, cmdSetMotorParam, byteCode)

     #'''The method is the one which is used for the rover to move'''
    def setPosition(self,newPosition):
        byte3,byte4=divmod(newPosition,0x100)
        byteCode = [0xFF, 0xFF, byte3, byte4]
        self.bus.write_i2c_block_data(self.devAddress, cmdSetPosition, byteCode)
    #'''The method is used for the rover to make a soft stop'''
    def softStop(self):
        self.bus.write_byte(self.devAddress, cmdSoftStop)
    #'''The method is used for writing to the motor'''
    def writeToMotor(self, value):
        self.bus.write_i2c_block_data(self.devAddress, 0x00, 0x00)
