import math
from itertools import islice 


#define n 
n=4

#Create 2D  intitak List
temp = [ 0 for x in range(n)]
Matrix = [temp for x in range(n)]
#print(Matrix)

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
    registered.append(0)
    memory.append(0)
    c+=1


#first and last step 
step = (math.factorial((n-1)*2))/(math.factorial(n-1)*math.factorial(n-1))
#print(step)
pattern[0] = pattern [(n*n)-1] = step


#OTHER steps
for x in range(n):
    for y in range(n):
        if ((x==0 or y==0) and (x!=y)):
            step = math.factorial(2*n-2-x-y)/(math.factorial(n-1-x)*math.factorial(n-1-y))
            Matrix[x][y] = step 
            pattern [x*n + y]= step
            #print (x , 'x and y',y , 'step', step )
        if (((x==n-1) or (y==n-1) or (x>0 and y>0)) and not(x==y==n-1)):
            s = math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
            tep = math.factorial(2*n-2-x-y)/(math.factorial(n-1-x)*math.factorial(n-1-y))
         #  print(s,'s',tep,'tep')
            step = s*tep
            pattern[x*n +y] = step



Matrix = convert(pattern , var_lst)
RoadMapMatrix = convert(roadMap , var_lst)


print(pattern)
print(roadMap)
print(RoadMapMatrix[3][3])


def CheckNext(x,y,direction):
    if(direction == 'R'):
        if(pattern[n*x+y+1]!=0 and pattern[n*x+y+1] != -1):
            pattern[x*n+y] = pattern[x*n+y]-1
            return True
    elif(direction == 'U'):
        if (pattern[n*x+y+n]!=0 and pattern[n*x+y+n] != -1 ):
            pattern[x*n+y] = pattern[x*n+y]-1
            return True
        elif(pattern[n*x+y+n] == -1):
            pattern[x*n+y] = 0
            return False
    else:
        return False

def CheckRepeat(tempRoad):
    if(len(memory) == 0  or memory[len(memory)-1] != tempRoad ):
        return True
    else:
        return False


def RightMove(x,y,tempRoad):
    if(x==0 and y==0 and CheckNext(x,y,'R')): # (0,0) point
        tempRoad.append(RoadMapMatrix[x][y])
        #tempRoad.append(RoadMapMatrix[x][y+1])
        #pattern[x*n+y] = pattern[x*n+y]-1
        y+=1
        #pattern[x*n+y] = pattern[x*n+y]-1
        RightMove(x,y,tempRoad)
    if(x==0 and y==0 and not(CheckNext(x,y,'R')) ): # (0,0) point
        #pattern[x*n+y] = pattern[x*n+y]-1
        UpMove(x,y,tempRoad)

    if(x==n-1 and y==n-2): #Pivot point to register
        #this is also check repeat ??? 
        tempRoad.append(roadMap[n*x+y])
        memory.append(tempRoad)
        if(CheckRepeat(tempRoad) and CheckNext(x,y,'R')):
           # pattern[x*n+y] = pattern[x*n+y]-1

            tempRoad.append(roadMap[n*x+y+1])
            registered.append(tempRoad)
            tempRoad.clear()
            x=0
            y=0
            #should call move again here !!!!!!!!!!!!!! otherwise its only one move
            RightMove(x,y,tempRoad)
        else:
            pass
            #TODO: write the repeat 

    if(x==n-2 and y==n-1):  #Pivot point 2 to register
        tempRoad.append(Matrix[x][y])
        memory.append(tempRoad)
        if(CheckRepeat(tempRoad)):
            if(CheckNext(x,y,'U')):
            #pattern[x*n+y] = pattern[x*n+y]-1
                tempRoad.append(Matrix[x][y+1])
                registered.append(tempRoad)
                tempRoad.clear()
                x=0
                y=0
                RightMove(x,y,tempRoad)
        else:
            pass
            #TODO: write the repeat 


    if(x<n-2 and y==n-1):
        tempRoad.append(RoadMapMatrix[x][y])
        memory.append(tempRoad)
        if(CheckRepeat(tempRoad)):

            if(CheckNext(x,y,'U')):
                #pattern[x*n+y] = pattern[x*n+y]-1
               # tempRoad.append(RoadMapMatrix[x][y])
                UpMove(x,y,tempRoad)
            else:
                pattern[x*n+y] = 0
                tempRoad.clear()
                x=0
                y=0
                RightMove(x,y,tempRoad)
        else:
            tempRoad.pop()
            y-=1 # one step to left
            UpMove(x,y,tempRoad) # then goes up

    if(x==n-1 and y<n-2):
        if(CheckNext(x,y,'R')):
            pattern[x*n+y] = pattern[x*n+y]-1
            tempRoad.append(RoadMapMatrix[x][y])
            y+=1
            RightMove(x,y,tempRoad)

        else:
            pattern[x*n+y] = 0 
            tempRoad.clear()
            x=0
            y=0
            RightMove(x,y,tempRoad)
    else:
        if(CheckNext(x,y,'R')):
            tempRoad.append(RoadMapMatrix[x][y])
            y+=1
            RightMove(x,y,tempRoad)
        elif(CheckNext(x,y,'U')):
            tempRoad.append(RoadMapMatrix[x][y])
            UpMove(x,y,tempRoad)
            
            

def UpMove(x,y,tempRoad):
    if(x==0 and y==0 and CheckNext(x,y,'U')): # (0,0) point
        tempRoad.append(RoadMapMatrix[x][y])
        #tempRoad.append(RoadMapMatrix[x+1][y])
       # pattern[x*n+y] = pattern[x*n+y]-1
        x+=1
       # pattern[x*n+y] = pattern[x*n+y]-1
        RightMove(x,y,tempRoad)
    if(x==0 and y==0 and  not(CheckNext(x,y,'U'))):
        print ("the end")
    else:
        x+=1
        RightMove(x,y,tempRoad)

