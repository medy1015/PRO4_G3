from multiprocessing import Process
import RPi.GPIO as gpio
import time
from Controller import Control

#process1=Process(target=self.controller.isPressed, args=('ashwinth3.log',))
class Init_button:

  

   def __init__(self):
      print 'i am constructor'
      self.control=Control()
      self.a = False
      print 'a value: ' , self.a
      self.p=Process(target=self.control.move_robot)
      self.mapped = False;
      
   def runMe(self):
      print 'runMe called'
      self.control.move_robot()
      

   def method(self,namelog):
    while True:
        with open(namelog,'a') as filelog:
            time.sleep(0.1)
            filelog.write('test log anything \n')

   def getInput(self):
      
      #p=Process(target=self.control.move_robot(), args=('ashwinth3.log',))
      #p=Process(target=self.control.move_robot())
      #p=Process(target=self.runMe(), args=('ashwinth3.log',))
      #print 'button: ', gpio.input(15)
      
      gpio.setwarnings(False)
      # Set the mode of numbering the pins.
      gpio.setmode(gpio.BOARD)
      # GPIO pin 12 is the output. 
      gpio.setup(12, gpio.OUT)
      gpio.setup(21, gpio.OUT)
      #GPIO pin 15 is the input. 
      gpio.setup(15, gpio.IN)
      while True:
         var=gpio.input(15)
         if(var):
            if(self.mapped):
               print("mapped")
               
            elif(self.a != True):
               #p=Process(target=self.control.move_robot()).join()   
               print 'The button is pressed'
               print 'Now i am forking a child'
               gpio.output(21, False)
               self.p.start()
               print 'Start process'
               self.a=True
               #while(a):
                 # self.control.move_robot()

            else:
               self.mapped = True
               print 'The button is pressed'
               print 'Now i am going to kill the child'
               self.p.terminate()
               self.p.join()
               #Process.kill(p)
               b=self.p.is_alive()
               self.a = False
               print 'is alive: ' , b
                    
            #var = input("Enter a number:  ")

            #if(var>60):
                ##print 'The var value is greater than 60'
                ##print 'Now i am forking a child'
                
                ##p.start()
                ##print "start process"
                
            ##if(var==15):
              ##  print 'Now i am going to kill'
                ##p.terminate()
                ##v=p.is_alive()
               ## print 'v value' , v

            ##if(var==40):
              ##  print 'The number is less than 40'
               ## print 'Sorry cant fork a child for you'

            ##if(var==



         time.sleep(0.6)

# if __name__ == '__main__':

 #   self.getInput()

