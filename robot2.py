import math
from itertools import islice 


#define n 
n=4

#Create 2D  intitak List
temp = [ 0 for x in range(n)]
Matrix = [temp for x in range(n)]
#print(Matrix)

# 1D to 2D list convertor
def convert(lst, var_lst): 
    it = iter(lst) 
    return [list(islice(it, i)) for i in var_lst]


# list convertor pattern init
var_lst = [ n for x in range (n)]







roadMap =[]

#init pattern
pattern = []
for x in range(n*n):
    pattern.append(0)



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
            pass
            s = math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
            tep = math.factorial(2*n-2-x-y)/(math.factorial(n-1-x)*math.factorial(n-1-y))
         #  print(s,'s',tep,'tep')
            step = s*tep
            pattern[x*n +y] = step



Matrix = convert(pattern , var_lst)

#print(Matrix[1][1])
