import math
from cs1graphics import *

########################## Grpahic Setting #################################
world = Canvas(700, 200)
frame = Polygon(Point(40, 80), Point(40, 120), Point(660, 120), Point(660, 80), Point(650, 80), Point(650, 110), Point(50, 110), Point(50, 80))
world.add(frame)
frame.setFillColor('black')

OB1 = Square(30)
OB2 = Square(30)
world.add(OB1)
world.add(OB2)
OB1.moveTo(250, 95)
OB1.setFillColor('red')
OB2.moveTo(450, 95)
OB2.setFillColor('blue')
############################################################################

n=2
length = 0.1
get_initial = [0,1]                    #[initial pos(m1), initial velocity(m1), initial pos(m2), initial velocity(m2)]

m1, m2 = 4, 6                              # Mass
k1, k2, k3 = 4, 8, 6                       # Spring Constant
b = 0.0                                    # Air resistance 

####################s########  Modifier  ####################################
def f(mat,j): #mat[0] = t, mat[1] = y, mat[2] = z, mat[3] = w
#mat[0] = t, mat[1] = x1', mat[2] = x1, mat[3] = x2', mat[4] = x2
    if j==0: 
        return None #Differentiation form of time Do not modify
    elif j==1 :
        return mat[2]
    elif j==2 :
        return -mat[0]**2*mat[1]/(1+mat[0]**2)
    elif j==3:
        return -k3*mat[4]/m2-k2*(mat[4]-mat[2])/m2 -(b*mat[3])/m2
    elif j==4:
        return mat[3]
    else:
        return 0

################  Function Defining and Main Part  ########################

def createmat(time,mat):
    table=[[.0]*n for i in range(4)]
    summationlist=[]
    mat2=[time]+mat
    for j in range(4):
        if j==0:	
            for i in range(n):
                table[0][i]=f(mat2,i+1)*length
        elif j==3:
            matcopy=mat2[:]
            for i in range(n+1):
                if i==0:
                    matcopy[i]+=length
                else:
                    matcopy[i]+=table[j-1][i-1]
            for i in range(n):
                table[j][i]=f(matcopy,i+1)*length            
        else:
            matcopy=mat2[:]
            for i in range(n+1):
                if i==0:
                    matcopy[i]+=0.5*length
                else:
                    matcopy[i]+=0.5*table[j-1][i-1]
            for i in range(n):
                table[j][i]=f(matcopy,i+1)*length
            
    for i in range(n):
        sum=float(table[0][i]+2*table[1][i]+2*table[2][i]+table[3][i])
        summationlist.append(sum/6+get_initial[i])
    return summationlist

##########################   Print Part   #################################
def start():
    A = []
    matrix=get_initial
    time=0
    t = [time]+matrix
    A.append(t)
    matrixs=matrix[:]
    for i in range(len(matrix)):
            matrix[i]=createmat(time,matrixs)[i]   
    for i in range(1000):
        time+=0.1
        matrixs=matrix[:]
        for i in range(len(matrix)):
            matrix[i]=createmat(time,matrixs)[i]
        u = [time]+matrixs[:]
        A.append(u)
    return A

###########################################################################
A = start()

print A

for i in range(1000):
    OB1.move(20*A[i][2], 0)
    OB2.move(20*A[i][4], 0)

a = input('x')
