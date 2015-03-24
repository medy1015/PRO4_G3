''''
Created on May 24, 2014

@author: Ayman Zaki
'''

import smbus
import time as time
import math
from random import randint
from Map import Mapping
from AutoCorrection import AutoCorrect 

against_right = 0
against_left = 0
i=1
# This class moves the rover according to the obtained direction from Mapping or traversing classes, moverover,
#it stores the motors and sensors log and call Auto_Correction class if the position of the rover needs to be corrected
class Control:
 
    def __init__(self):

        self.ACorrect = AutoCorrect()
        self.mapping=Mapping()

        
#This method stores sensors and motors log in text file called logs.txt
    def write_log(self,i,direction):
        self.ACorrect.get_left_sensor()
        log_file = open("logs.txt", "a")
        
        right_sensor=int(self.ACorrect.get_right_sensor())
        left_sensor=int(self.ACorrect.get_left_sensor())
        front_sensor=int(self.ACorrect.get_front_sensor())
        
        readings=["["+str(i)+"]"," : ", "[Right sensor : "+str(right_sensor)+"]"," : ", "[Left sensor : "+str(left_sensor)+"]"," : ", "[Front sensor : "+str(front_sensor)+"]"," : ","[Direction : "+direction+"]""\n"]
        log_file.writelines(readings)
        
        log_file.close()
        log_file=open("logs.txt","r")
        log_file.close()
#This method keeps track of readings from sensors before the rover turns, based on the readings
#it calculate the first distance to move after it turned in order to keep the rover always in the middle of the cells
    def getInTheMiddel(self, direction):
        front=self.ACorrect.get_front_sensor()
        left=self.ACorrect.get_left_sensor()
        right=self.ACorrect.get_right_sensor()
        go = 0
        if(direction == "right"):
            if(front > 33 or front == 33):
                if(left > 27):
                    go= 0
                else:
                    go = 11-left
            else:
                if(left > 27):
                    go= 0
                    d = front - 11
                    self.ACorrect.get_motors().go(d)
                    time.sleep(1)
                else:
                    go = 11-left
                    d = front -11
                    self.ACorrect.get_motors().go(d)
                    time.sleep(1)
        elif(direction=="left"):
            if(front > 33 or front == 33):
                if(right > 27):
                    go= 0
                else:
                    go = 11-right
            else:
                if(right > 27):
                    go= 0
                    d = front - 11
                    self.ACorrect.get_motors().go(d)
                    time.sleep(1)
                else:
                    go = 11-right
                    d = front - 11
                    self.ACorrect.get_motors().go(d)
                    time.sleep(1)
        elif(direction=="forward"):
            print("Forward")
        elif(direction == "stop"):
            go=0
            
        else:
            go = 11-front
        return go
 #This method takes the readins from sensors and stores them in a list.   
    def send_to_mapping(self):
        
        front=self.ACorrect.get_front_sensor()
        left=self.ACorrect.get_left_sensor()
        right=self.ACorrect.get_right_sensor()
        if(front >27):
            fr=0
        else:
            fr=1
            
        if(left >22):
            le=0
        else:
            le=1
        if(right >22):
            ri=0
        else:
            ri=1
        alist=[0,0,0]
        alist.insert(0,ri)
        alist.insert(1,fr)
        alist.insert(2,le)

        return alist
# This moethod sends sensors' readings to Mapping class in order to get the direction to move.
#it also calls Auto-Correction calss in order to send the direction to Motors Controller class or in order to correct the position of the robot
    def move_robot(self):
        global d
        global theta
        global against_right
        global against_left
        global actualDist
        a=8.75
        i=1
        j=0
        
	self.ACorrect.get_motors().RDL()
        self.ACorrect.get_motors().setMotorParam(1,3)
        self.ACorrect.get_motors().resetPosition()

        while(True):
            alist=self.send_to_mapping()
            
            direction=self.mapping.map_maze(alist[0],alist[1],alist[2])
            time.sleep(0.2)
            getting = self.getInTheMiddel(direction)
            self.write_log(str(i)+".0", direction)
            
            self.ACorrect.get_motors().move_direction(direction)
            time.sleep(1)
            
            against_left1 = self.ACorrect.get_left_sensor()
            against_right1 = self.ACorrect.get_right_sensor()
            
            self.ACorrect.get_motors().go(a + getting)
            time.sleep(1)
            self.write_log(str(i)+".1", direction)
            
            against_left2 = self.ACorrect.get_left_sensor()
            against_right2 = self.ACorrect.get_right_sensor()
            
            against_left = (against_left2) - (against_left1)
            against_right = (against_right2) - (against_right1)
            time.sleep(1)           
            for j in range(0,3):
                error=self.ACorrect.get_sensors_reading()
                if(self.ACorrect.get_front_sensor() < 17):
                    self.ACorrect.get_motors().softStop()
                elif(self.ACorrect.get_right_sensor()< 9):
                    self.ACorrect.get_motors().turnLeftDegree(7)
                    time.sleep(1)
                    self.ACorrect.get_motors().go(a)
                    time.sleep(1)   
                elif(self.ACorrect.get_left_sensor()< 9):
                    self.ACorrect.get_motors().turnRightDegree(7)
                    time.sleep(1)
                    self.ACorrect.get_motors().go(a)#go 2
                    time.sleep(1)

                elif(self.ACorrect.get_right_sensor()> 15 and self.ACorrect.get_right_sensor()!=33 and self.ACorrect.get_left_sensor() == 33):
                    self.ACorrect.get_motors().turnRightDegree(5)
                    time.sleep(1)
                    self.ACorrect.get_motors().go(a)
                    time.sleep(1)
                elif(self.ACorrect.get_left_sensor()> 15 and self.ACorrect.get_left_sensor()!=33 and self.ACorrect.get_right_sensor() == 33):
                    self.ACorrect.get_motors().turnLeftDegree(5)
                    time.sleep(1)
                    self.ACorrect.get_motors().go(a)
                    time.sleep(1)

                elif(error !=0 and error < 15):
                    if((against_left1 > 9 and against_left1 < 13) and (against_left2 > 9 and against_left2 <13) and (against_right1 > 9 and against_right1 < 13) and (against_right2 > 9 and against_right1 < 13)):
          
                        if(((against_right2 - against_right1) < 1.5) and ((against_right2 - against_right1) > -1.5)):
                            time.sleep(1)
                            self.ACorrect.get_motors().go(a)
                            time.sleep(1)
                                
                    elif(error > 5 and error < 15 and against_right2 > 13 and against_left2 > 13 and (against_right > 3 or against_right < -3) and (against_left > 3 or against_left < -3)):
                        self.ACorrect.auto_correct(against_right,against_left)
                        theta = self.ACorrect.get_theta()
                        if(theta < 0):
                            theta = (theta * -1)
                            
                        actualDist1= a * (math.cos(theta))
                        if(actualDist1 < 0):
                            actualDist1 = actualDist1 * -1
                        time.sleep(1.5)
                   
                        if((actualDist1) < 22):
                            dist= 2*a - (actualDist1)
                            if(against_right > 0):
                                self.ACorrect.get_motors().go(dist)
                                time.sleep(1)
                            else:
                                self.ACorrect.get_motors().go(dist)
                                time.sleep(1)
                                    
                        elif((self.ACorrect.get_right_sensor() - self.ACorrect.get_left_sensor())> 2):
                            self.ACorrect.get_motors().turnRightDegree(7)
                            time.sleep(1)
                            self.ACorrect.get_motors().go(a)
                            time.sleep(1)
                        elif((self.ACorrect.get_right_sensor() - self.ACorrect.get_left_sensor())< -2):
                            self.ACorrect.get_motors().turnLeftDegree(7)
                            time.sleep(1)
                            self.ACorrect.get_motors().go(a)
                            time.sleep(1)
                        
                    else:
                        self.ACorrect.get_motors().go(a)
                        time.sleep(1)
                else:
                    self.ACorrect.get_motors().go(a)
                    time.sleep(1)
                if(j==0):
                    self.write_log(str(i)+".2", direction)
                    i = i+1
                else:
                    print("anden gang")

#This method gets the direction from Traversing class in order to get tthe rover to travse the fastest path
    def traverse(self, direction):
        global d
        global theta
        global against_right
        global against_left
        global actualDist
        a=8.75
        i=1
        j=0

        
	self.ACorrect.get_motors().RDL()
        self.ACorrect.get_motors().setMotorParam(1,3)
        self.ACorrect.get_motors().resetPosition()
        if(a > 0):
            self.ACorrect.get_motors().move_direction(direction)
            time.sleep(1)
            
            against_left1 = self.ACorrect.get_left_sensor()
            against_right1 = self.ACorrect.get_right_sensor()
            
            self.ACorrect.get_motors().go(a) 
            time.sleep(1)
            self.write_log(str(i)+".1", direction)
            
            against_left2 = self.ACorrect.get_left_sensor()
            against_right2 = self.ACorrect.get_right_sensor()
            
            against_left = (against_left2) - (against_left1)
            against_right = (against_right2) - (against_right1)

            time.sleep(1)
           
            for j in range(0,3):
                error=self.ACorrect.get_sensors_reading()
                if(self.ACorrect.get_front_sensor() < 17):
                    self.ACorrect.get_motors().softStop()
                elif(self.ACorrect.get_right_sensor()< 9):
                    self.ACorrect.get_motors().turnLeftDegree(7)
                    time.sleep(1)
                    self.ACorrect.get_motors().go(a)
                    time.sleep(1)   
                elif(self.ACorrect.get_left_sensor()< 9):
                    self.ACorrect.get_motors().turnRightDegree(7)
                    time.sleep(1)
                    self.ACorrect.get_motors().go(a)#go 2
                    time.sleep(1)

                elif(self.ACorrect.get_right_sensor()> 15 and self.ACorrect.get_right_sensor()!=33 and self.ACorrect.get_left_sensor() == 33):
                    self.ACorrect.get_motors().turnRightDegree(5)
                    time.sleep(1)
                    self.ACorrect.get_motors().go(a)
                    time.sleep(1)
                elif(self.ACorrect.get_left_sensor()> 15 and self.ACorrect.get_left_sensor()!=33 and self.ACorrect.get_right_sensor() == 33):
                    self.ACorrect.get_motors().turnLeftDegree(5)
                    time.sleep(1)
                    self.ACorrect.get_motors().go(a)
                    time.sleep(1)

                elif(error !=0 and error < 15):
                    if((against_left1 > 9 and against_left1 < 13) and (against_left2 > 9 and against_left2 <13) and (against_right1 > 9 and against_right1 < 13) and (against_right2 > 9 and against_right1 < 13)):
          
                        if(((against_right2 - against_right1) < 1.5) and ((against_right2 - against_right1) > -1.5)):
                            time.sleep(1)
                            self.ACorrect.get_motors().go(a)
                            time.sleep(1)
                                
                    elif(error > 5 and error < 15 and against_right2 > 13 and against_left2 > 13 and (against_right > 3 or against_right < -3) and (against_left > 3 or against_left < -3)):
                        self.ACorrect.auto_correct(against_right,against_left)
                        theta = self.ACorrect.get_theta()
                        if(theta < 0):
                            theta = (theta * -1)
                            
                        actualDist1= a * (math.cos(theta))
                        if(actualDist1 < 0):
                            actualDist1 = actualDist1 * -1
                        time.sleep(1.5)
                   
                        if((actualDist1) < 22):
                            dist= 2*a - (actualDist1)
                            if(against_right > 0):
                                self.ACorrect.get_motors().go(dist)
                                time.sleep(1)
                            else:
                                self.ACorrect.get_motors().go(dist)
                                time.sleep(1)
                                    
                        elif((self.ACorrect.get_right_sensor() - self.ACorrect.get_left_sensor())> 2):
                            self.ACorrect.get_motors().turnRightDegree(7)
                            time.sleep(1)
                            self.ACorrect.get_motors().go(a)
                            time.sleep(1)
                        elif((self.ACorrect.get_right_sensor() - self.ACorrect.get_left_sensor())< -2):
                            self.ACorrect.get_motors().turnLeftDegree(7)
                            time.sleep(1)
                            self.ACorrect.get_motors().go(a)
                            time.sleep(1)
                        
                    else:
                        self.ACorrect.get_motors().go(a)
                        time.sleep(1)
                else:
                    self.ACorrect.get_motors().go(a)
                    time.sleep(1)
                if(j==0):
                    self.write_log(str(i)+".2", direction)
                    i = i+1
                else:
                    print("anden gang")
        
    def against_left(self):
        return against_left

    def against_right(self):
        return against_right

    def main(self):
        self.controll=Controller()
        self.mapping=Mapping()
        self.sensor=IRSensor()
        while(True):
            self.mapping.get_information()
            self.movedir()
 
        if __name__ == '__main__':     # if the function is the main function ...
            self.main()


