import math

#define n 
n=6

temp = [ 0 for x in range(n)]

Matrix = [temp for x in range(n)]

print(Matrix)

roadMap =[]
pattern = []

for x in range(n*n):
    pattern.append(0)



#first and last step 
step = (math.factorial((n-1)*2))/(math.factorial(n-1)*math.factorial(n-1))
print(step)
pattern[0] = pattern [(n*n)-1] = step

for x in range(n):
    for y in range(n):
        if ((x==0 or y==0) and (x!=y)):
            step = math.factorial(2*n-2-x-y)/(math.factorial(n-1-x)*math.factorial(n-1-y))
            Matrix[x][y] = step 
            pattern [x*n + y]= step
            print (x , 'x and y',y , 'step', step )
        if (((x==n-1) or (y==n-1) or (x>0 and y>0)) and not(x==y==n-1)):
            pass
            s = math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
            tep = math.factorial(2*n-2-x-y)/(math.factorial(n-1-x)*math.factorial(n-1-y))
         #  print(s,'s',tep,'tep')
            step = s*tep
            pattern[x*n +y] = step




print(pattern)
