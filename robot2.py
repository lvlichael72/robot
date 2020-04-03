import math
import sys

from itertools import islice 

sys.setrecursionlimit(99999)
#define n 
n=4

#Create 2D  intitak List
temp = [ 0 for x in range(n)]
Matrix = [temp for x in range(n)]


temp = [1 for x in range(n)]
routeCheck = [ temp for x in range(n)]


# 1D to 2D list convertor
def convert(lst, var_lst): 
    it = iter(lst) 
    return [list(islice(it, i)) for i in var_lst]


# list convertor pattern init
var_lst = [ n for x in range (n)]



#init pattern and roadMap
pattern = []
roadMap =[]
registered =[]
tempRoad = []
memory = []
c=1
for x in range(n*n):
    pattern.append(0)
    roadMap.append(c)
    c+=1


#first and last step 
step = (math.factorial((n-1)*2))/(math.factorial(n-1)*math.factorial(n-1))

pattern[0] = pattern [(n*n)-1] = step


#OTHER steps
for x in range(n):
    for y in range(n):
        if ((x==0 or y==0) and (x!=y)):
            step = math.factorial(2*n-2-x-y)/(math.factorial(n-1-x)*math.factorial(n-1-y))
            Matrix[x][y] = step 
            pattern [x*n + y]= step
           
        if (((x==n-1) or (y==n-1) or (x>0 and y>0)) and not(x==y==n-1)):
            s = math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
            tep = math.factorial(2*n-2-x-y)/(math.factorial(n-1-x)*math.factorial(n-1-y))
     
            step = s*tep
            pattern[x*n+y] = step



Matrix = convert(pattern , var_lst)
RoadMapMatrix = convert(roadMap , var_lst)
#pattern[5]=-1
#print(pattern)
#print(roadMap)

def CheckNext(x,y,direction):
    try:
        if(direction == 'R' and (n*x+y+1) < n*n):
            #print(n*x+y+1,'pattern index','x=',x,'y=',y)
            
            if(pattern[n*x+y+1]!=0 and pattern[n*x+y+1] != -1):
                pattern[x*n+y] = pattern[x*n+y]-1
                return True
            if(pattern[0]==0):
                pattern[len(pattern)-1]=0
                pattern[len(pattern)-2]=0
        elif(direction == 'U' and (n*x+y+1) < n*n):
            #print(pattern[n*x+y+1])
            if (pattern[n*x+y+n]!=0 and pattern[n*x+y+n] != -1 ):
                pattern[x*n+y] = pattern[x*n+y]-1
                return True
            elif(pattern[n*x+y+n] == -1):
                pattern[x*n+y] = 0
                return False
            
        else:
           # print('X=',x,'Y=',y)
            pattern[x*n+y] = pattern[x*n+y]-1
            return True
    except:
         pass
     #   return False

def printRegistered():
    print(registered)


def CheckRepeat(tempRoad):
    #print('PATTERNG',pattern)
    if (len(registered) != 0):
        if(len(memory) == 0): 
            return True
        #elif (list(memory[len(memory)-1]) != tempRoad ):
        elif (tuple(tempRoad) in list(memory)):
                    #print("CHECK REPEAT:",list(memory[len(memory)-1]) ,' and',tempRoad)
                    return False
        else:
           # print(memory[len(memory)-1],'memory')
            #print(tempRoad,'temproad')
            #print(registered,'regex')
            #print('$$$$$$$$')
            return True
    else:
        return True


def RightMove(x,y):
    #if(pattern[0]!= 0):
        #print('right')
    # print(tempRoad)
        #print(registered,'registerd')
        #print(pattern,'pattern FINAL')
        if(x==0 and y==0 and CheckNext(x,y,'R')): # (0,0) point
            tempRoad.append(RoadMapMatrix[x][y])
         #   print('001here')
        # print(pattern)
            #tempRoad.append(RoadMapMatrix[x][y+1])
            #pattern[x*n+y] = pattern[x*n+y]-1
            y+=1
            #pattern[x*n+y] = pattern[x*n+y]-1
            RightMove(x,y)
        if(x==0 and y==0 and not(CheckNext(x,y,'R')) ): # (0,0) point
            #pattern[x*n+y] = pattern[x*n+y]-1
            UpMove(x,y)

        if(x==n-1 and y==n-2): #Pivot point to register
           # print('now here 123')
            #this is also check repeat ??? 
            tempRoad.append(RoadMapMatrix[x][y])
            
            if(CheckRepeat(tempRoad)):
                if (CheckNext(x,y,'R')):
                    # pattern[x*n+y] = pattern[x*n+y]-1
                    memory.append(tuple(tempRoad))
                    tempRoad.append(RoadMapMatrix[x][y+1])
                    registered.append(tuple(tempRoad))
                    tempRoad.clear()
                    x=0
                    y=0
                #should call move again here !!!!!!!!!!!!!! otherwise its only one move
                    RightMove(x,y)
            else:
                while(tempRoad[len(tempRoad)-1]-1 != tempRoad[len(tempRoad)-2]):
                    pattern[x*n+y]+=1
                    x-=1
                    tempRoad.pop()
                

                pattern[x*n+y]+=1
                y-=1
                tempRoad.pop()
                UpMove(x,y)
                print ('final position')
                print('final temproad',tempRoad,'pattern',pattern)
                print('register:',registered)
                #TODO: write the repeat ig

        if(x==n-2 and y==n-1):  #Pivot point 2 to register
            print('002here','x=',x,'y=',y)
            tempRoad.append(RoadMapMatrix[x][y])
            
            if(CheckRepeat(tempRoad)):
                if(CheckNext(x,y,'U')):
                #pattern[x*n+y] = pattern[x*n+y]-1
                    memory.append(tuple(tempRoad))
                    print('fucking memory? ',memory)
                    tempRoad.append(RoadMapMatrix[x+1][y])
                    registered.append(tuple(tempRoad))
                    tempRoad.clear()
                    print('002here','temp',tempRoad,'registered',registered,'memory',memory)
                    x=0
                    y=0
                    RightMove(x,y)
            else:
               # print('@@@@@')
                tempRoad.pop()
                y-=1
                UpMove(x,y)


        if( x!=0 and x<n-2 and y==n-1):
            print('x=',x,'y=',y)
            print('004here')
            #print('here')
            
            tempRoad.append(RoadMapMatrix[x][y])
        #  print(tempRoad)
            if(CheckRepeat(tempRoad)):

                if(CheckNext(x,y,'U')):
                    #pattern[x*n+y] = pattern[x*n+y]-1
                # tempRoad.append(RoadMapMatrix[x][y])
                    memory.append(tuple(tempRoad))
                    UpMove(x,y)
                else:
                    pattern[x*n+y] = 0
                    tempRoad.clear()
                    x=0
                    y=0
                    RightMove(x,y)
            else:
                print('005here')
                tempRoad.pop()
                y-=1 # one step to left
                UpMove(x,y) # then goes up

        if(x==n-1 and y<n-2 and y!=0):
            print('006here')
            
                #pattern[x*n+y] = pattern[x*n+y]-1
            tempRoad.append(RoadMapMatrix[x][y])
            if(CheckRepeat(tempRoad)):

                if(CheckNext(x,y,'R')):
                    memory.append(tuple(tempRoad))
                    y+=1
                #print('problemo')
                    RightMove(x,y)

                else:
                    #TODO this is wrong and should be changed
                    #print('problemo')
                    pattern[x*n+y] = 0 
                    tempRoad.clear()
                    x=0
                    y=0
                    RightMove(x,y)
            
            else:
                while(tempRoad[len(tempRoad)-1]-1 != tempRoad[len(tempRoad)-2]):
                    pattern[x*n+y]+=1
                    x-=1
                    tempRoad.pop()
                

                pattern[x*n+y]+=1
                y-=1
                tempRoad.pop()
                UpMove(x,y)
            



        if(x==0 and y==n-1):                            #this is for corner right down
            if (CheckNext(x,y,'U')):
                tempRoad.append(RoadMapMatrix[x][y])
                print('Check corner',x , y)
                UpMove(x,y)
            else:
                pattern[n*x+y] = 0 
        if(y==0 and x==n-1):
            if(CheckNext(x,y,'R')):
                tempRoad.append(RoadMapMatrix[x][y])
                print('Check corner',x , y)
                y+=1
                RightMove(x,y)
            else:
                pattern[n*x+y]=0
                
        else:
            if(x<n and y<n):
                if(CheckNext(x,y,'R')):
                    tempRoad.append(RoadMapMatrix[x][y])
                    print(tempRoad,'ghgh')
                    y+=1
                    RightMove(x,y)
                elif(CheckNext(x,y,'U')):
                    tempRoad.append(RoadMapMatrix[x][y])
                    UpMove(x,y)
            else:
                printRegistered()
            
            

def UpMove(x,y):
    print('UP')
    if(x==0 and y==0 and CheckNext(x,y,'U')): # (0,0) point
        print('007here')
        tempRoad.append(RoadMapMatrix[x][y])
        #tempRoad.append(RoadMapMatrix[x+1][y])
       # pattern[x*n+y] = pattern[x*n+y]-1
        x+=1
       # pattern[x*n+y] = pattern[x*n+y]-1
        print('@M', x ,'=x',y,'=y')
        RightMove(x,y)
    if(x==0 and y==0 and  not(CheckNext(x,y,'U'))):
        pattern[0]=0
        print ("the end")
        
        
    else:
        print('008here')
        print('herehrerer',x,y)
        x+=1
        RightMove(x,y)



RightMove(0,0)



#print(registered)

