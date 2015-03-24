
#-----------------------------------------------------------------------#
#-This class is responsible for reading IR sensor and it handles converting
#-milivolts into cm using a formula

import smbus
import time as time
import math


ConfigurationRegister      = 0x02

Channel_1                  = 0x08
Channel_2                  = 0x09
Channel_3                  = 0x0A
Channel_4                  = 0x0B
Channel_5                  = 0x0C
Channel_6                  = 0x0D
a=99.12
b=-0.00519
c=23.38
d=-0.0007634
robot_width=11.5
cell_width=34

i2c=smbus.SMBus(1)

class IRSensor:

    a=99.12
    b=-0.00519
    c=23.38
    d=-0.0007634
    
    
    def __init__(self):
        self.bus=smbus.SMBus(1)


    def readIRSensor(self,channel):
        self.register=(channel<<4)

        try:

            self.reading=self.bus.read_i2c_block_data(0x20,self.register,2)
            self.value=(self.reading[0] & 0b00001111)<<8 | self.reading[1]<<0
        except IOError:
            print 'Failed to read from sensor'

        return self.value

    def converter(self,miliVolt):
        value=0.0
        
        if(miliVolt>300): 
            value=a*math.exp(b*miliVolt) + c*math.exp(d*miliVolt)

        else:
            value =301

        return value


    def get_right_sensor(self):
        sr=0
        if(self.readRightSensor() < 33):
            sr =sr + self.readRightSensor()  
        else:
            sr = 33
        return sr
        
    def get_left_sensor(self):
        sl=0
        if(self.readLeftSensor() < 33):
            sl =sl + self.readLeftSensor()  
        else:
            sl = 33
        return sl

    def get_front_sensor(self):
        sf=0
        if(self.readFrontSensor() < 33):
            sf =sf + self.readFrontSensor()  
        else:
            sf = 33
        return sf


    def readRightSensor(self):
        miliV=self.readIRSensor(Channel_4)
        resultInCm=self.converter(miliV)
        if(resultInCm > 33 or resultInCm =='invalid'):
            resultInCm = 33
        return resultInCm

    def readLeftSensor(self):
        miliV=self.readIRSensor(Channel_1)
        resultInCm=self.converter(miliV)
        if(resultInCm > 33 or resultInCm =='invalid'):
            resultInCm = 33
        return resultInCm

    def readFrontSensor(self):

        miliV=self.readIRSensor(Channel_2)
        resultInCm=self.converter(miliV)
        if(resultInCm > 33 or resultInCm =='invalid'):
            resultInCm = 33
        return resultInCm




	
            
                               
