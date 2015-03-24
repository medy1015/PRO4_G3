#show redinf from a text file
import time
from Controller import Control

class traverse:
    
    def __init__(self):
        self.con = Control()
    
    def traverse(self):
        text_file = open("filename.txt","r")
        lines = (text_file.readlines())
        F = "F"
        L = "L"
        R = "R"

        print 'lines'
        for line in lines:
            print 'line'
            if line.startswith(F):
                self.con.traverse("forward")
                time.sleep(3)
            elif line.startswith(R):
                self.con.traverse("right")
                time.sleep(3)
            elif line.startswith(L):
                self.con.traverse("left")
                time.sleep(3)
            else:
                print "Do nothing"
        text_file.close()
