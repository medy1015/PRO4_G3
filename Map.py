x=0
y=0
tx=0
ty=0
dfs=[]
VisitedStack=[]
olddir = 'North'
obj = object
class Mapping:
        #The method is used to write to a file
        def writeToFile(self,sensRight,sensLeft,sensFront, x,y,direction):
                file = open("test.txt", "r+")##### x,y,N,E,W,S,Direction
                boolean = False
                wall = 0
                i=0
                b = str(x)+""+ str(y)
                while True:
                        line = file.readline()
                        if not line:
                                if(i ==0):
                                        wall = 1
                                break
                        i+=1
                        aaa = line.split(" ")
                        a = aaa[0] + "" + aaa[1]
                        if(a == b):
                                boolean=True
                                return
                        else:
                                boolean = False
                if(boolean == True):
                        print("+")
                else:
                        if(direction == "North"):
                                file.write(str(str(x) + " " + str(y)+" " + str(sensFront)+ " " + str(sensRight) + " " + str(sensLeft) + " "+str(wall)+"\n"))
                        elif(direction == "West"):
                                file.write(str(str(x) + " " + str(y)+" " + str(sensRight)+ " "+str(wall)+" " + str(sensFront) + " " + str(sensLeft) +"\n"))
                        elif(direction == "East"):
                                file.write(str(str(x) + " " + str(y)+" " + str(sensLeft)+ " " + str(sensFront) + " "+str(wall) + " " + str(sensRight) + "\n"))
                        else:
                                file.write(str(str(x) + " " + str(y)+" " + str(wall)+ " " + str(sensLeft)+ " " + str(sensRight) + " " + str(sensFront) + "\n"))
                file.close()
        #The method is doing mapping, it checks if there are walls, and then when it returns the turn the rover should do'''
        def map_maze(self,snr,snf,snl):
                sr = snr#SRI()
                sl = snl#SLE()
                sf = snf
                direction = ""
                global VisitedStack 
                global x
                global y
                global olddir
                if len(VisitedStack) == 0:
                        VisitedStack.append((0,0))
                        dfs.append((0,0))
                if len(VisitedStack)== 49:
                        direction ="stop"
                else:
                        if sr == 0:
                            nextpos = self.getNextDirection("right")
                            if(nextpos in  VisitedStack):    
                                    if(sf == 0):
                                            nextpos = self.getNextDirection("forward")
                                            if(nextpos in  VisitedStack): 
                                                    if(sl == 0):
                                                            nextpos = self.getNextDirection("left")
                                                            if(nextpos in  VisitedStack): 
                                                                    dfs.pop()
                                                                    a=dfs[-1]
                                                                    b = self.gobacktrack(a)
                                                                    self.setaxis(b)
                                                                    direction = b
                                                                    
                                                            else:
                                                                    self.writeToFile(sr,sl,sf,x,y,olddir)
                                                                    VisitedStack.append(nextpos)
                                                                    dfs.append(nextpos) 
                                                                    self.setaxis("left")
                                                                    direction = "left"
                                                    else:                                                
                                                           dfs.pop()
                                                           a=dfs[-1]
                                                           b = self.gobacktrack(a)
                                                           self.setaxis(b)
                                                           direction = b
                                            else:
                                                    self.writeToFile(sr,sl,sf,x,y,olddir)
                                                    VisitedStack.append(nextpos)
                                                    dfs.append(nextpos)
                                                    self.setaxis("forward")
                                                    direction = "forward"
                                    elif(sl == 0):
                                            nextpos = self.getNextDirection("left")
                                            if(nextpos in  VisitedStack): 
                                                    dfs.pop()
                                                    a=dfs[-1]
                                                    b = self.gobacktrack(a)
                                                    self.setaxis(b)
                                                    direction = b
                                            else:
                                                    self.writeToFile(sr,sl,sf,x,y,olddir) 
                                                    VisitedStack.append(nextpos)
                                                    dfs.append(nextpos)
                                                    self.setaxis("left")
                                                    direction = "left"
                                    else:
                                            self.writeToFile(sr,sl,sf,x,y,olddir)
                                            dfs.pop()
                                            a=dfs[-1]
                                            b = self.gobacktrack(a)
                                            self.setaxis(b)
                                            direction = b
                            else:
                                    self.writeToFile(sr,sl,sf,x,y,olddir)                              
                                    VisitedStack.append(nextpos)
                                    dfs.append(nextpos)
                                    self.setaxis("right")
                                    direction = "right"
                           
                        elif(sf == 0):
                                nextpos = self.getNextDirection("forward")
                                if(nextpos in  VisitedStack): 
                                        if(sl == 0):
                                                nextpos = self.getNextDirection("left")
                                                if(nextpos in  VisitedStack):                            
                                                        dfs.pop()
                                                        a=dfs[-1]
                                                        b = self.gobacktrack(a)
                                                        self.setaxis(b)
                                                        direction = b
                                                else:
                                                        self.writeToFile(sr,sl,sf,x,y,olddir) 
                                                        VisitedStack.append(nextpos)
                                                        dfs.append(nextpos)
                                                        self.setaxis("left")
                                                        direction = "left"
                                        else:
                                                dfs.pop()
                                                a=dfs[-1]
                                                b = self.gobacktrack(a)
                                                self.setaxis(b)
                                                direction = b
                                else:
                                        self.writeToFile(sr,sl,sf,x,y,olddir) 
                                        VisitedStack.append(nextpos)
                                        dfs.append(nextpos)
                                        self.setaxis("forward")
                                        direction = "forward"

                        elif(sl == 0):
                                nextpos = self.getNextDirection("left")
                                if(nextpos in  VisitedStack): 
                                        
                                        dfs.pop()
                                        a=dfs[-1]
                                        b = self.gobacktrack(a)
                                        self.setaxis(b)
                                        direction = b
                                else:
                                        self.writeToFile(sr,sl,sf,x,y,olddir)
                                        VisitedStack.append(nextpos)
                                        dfs.append(nextpos)
                                        self.setaxis("left")
                                        direction = "left"
                                        
                        else:
                                self.writeToFile(sr,sl,sf,x,y,olddir)
                                dfs.pop()
                                a=dfs[-1]
                                b = self.gobacktrack(a)
                                self.setaxis(b)
                                direction = b
                return direction
        #The method is used to return the next coordinate according to the Direction '''
        def getNextDirection(self,bearings):
                global olddir
                global ty
                global tx
                if(olddir == 'North'):          #Noorth
                    if(bearings=='right'):
                        tx = x+1
                        ty = y
                    elif(bearings == 'forward'):
                        ty = y+1
                        tx = x
                    elif(bearings == 'left'):
                        tx = x-1
                        ty = y
                    else:
                        ty = y-1
                        tx = x
                        
                elif(olddir == 'East'):         #Eeaast
                    if(bearings=='right'):
                        ty = y-1
                        tx = x
                    elif(bearings == 'forward'):
                        tx = x+1
                        ty = y
                    elif(bearings == 'left'):
                        ty = y+1
                        tx = x
                    else:
                        tx = x-1
                        ty = y
                        
                elif(olddir == 'West'):         #Weest
                    if(bearings=='right'):
                        ty = y+1
                        tx = x
                    elif(bearings == 'forward'):
                        tx = x-1
                        ty = y
                    elif(bearings == 'left'):
                        ty = y-1
                        tx = x
                        
                    else:
                        tx = x+1
                        ty = y
                        
                elif(olddir == 'South'):        #Souuth  
                    if(bearings=='right'):
                        tx = x-1
                        ty = y
                    elif(bearings == 'forward'):
                        ty = y-1
                        tx = x
                    elif(bearings == 'left'):
                        tx = x+1
                        ty = y
                    else:
                        ty = y+1
                        tx = x
                
                return tx,ty                       
           
         #The method is responsible for doing backtracking for the rover'''  
        def gobacktrack(self,aa):
                pos = self.getNextDirection("forward")
                pos1 = self.getNextDirection("right")
                pos2 = self.getNextDirection("left")
                pos3 = self.getNextDirection("back")
                nextdir =""
                if(aa == pos):
                        nextdir = "forward"
                elif(aa == pos1):
                        nextdir = "right"
                elif(aa == pos2):
                        nextdir = "left"
                elif(aa == pos3):
                        nextdir = "back"
                return nextdir
        #The method is used to change the coordinates depending on which direction the rover have to go, and the turn it have to do'''
        def setaxis(self,bearings):
                global olddir
                global x
                global y
                if(olddir == 'North'):          #Noorth
                    if(bearings=='right'):
                        x += 1
                        olddir = 'East'
                    elif(bearings == 'forward'):
                        y += 1
                        olddir = 'North'
                    elif(bearings == 'left'):
                        x -= 1
                        olddir = 'West'
                    else:
                        y -= 1
                        olddir = 'South'
                elif(olddir == 'East'):         #Eeaast
                    if(bearings=='right'):
                        y = y-1
                        olddir = 'South'
                    elif(bearings == 'forward'):
                        x += 1
                        olddir = 'East'
                    elif(bearings == 'left'):
                        y += 1
                        olddir = 'North'
                    else:
                        x -= 1
                        olddir = 'West'
                elif(olddir == 'West'):         #Weest
                    if(bearings=='right'):
                        y += 1
                        olddir = 'North'
                    elif(bearings == 'forward'):
                        x -= 1
                        olddir = 'West'
                    elif(bearings == 'left'):
                        y -= 1
                        olddir = 'South'
                    else:
                        x += 1
                        olddir = 'East'
                elif(olddir == 'South'):        #Souuth  
                    if(bearings=='right'):
                        x -= 1
                        olddir = 'West'
                    elif(bearings == 'forward'):
                        y -= 1
                        olddir = 'South'
                    elif(bearings == 'left'):
                        x += 1
                        olddir = 'East'
                    else:
                        y += 1
                        olddir = 'North'
