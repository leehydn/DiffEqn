import math

m1, m2 = 4, 5
k1, k2, k3 = 4, 8, 6

####################s########  Modifier  ####################################
def f(mat,j): #mat[0] = t, mat[1] = y, mat[2] = z, mat[3] = w
#mat[0] = t, mat[1] = x1', mat[2] = x1, mat[3] = x2', mat[4] = x2
    if j==0: 
        return None #Differentiation form of time Do not modify
    elif j==1 :
        return (mat[1]-1)*(mat[1]-2)*(mat[1]-4)**2*(mat[1]-6)*(mat[1]-7)
    elif j==2 :
        return 9*mat[2]**2-16*mat[1]**2
    elif j==3:
        return -k3*mat[4]/m2-k2*(mat[4]-mat[2])/m2
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
    matrix=get_initial
    time=initial
    print [time]+matrix
    matrixs=matrix[:]
    for i in range(len(matrix)):
            matrix[i]=createmat(time,matrixs)[i]   
    for i in range(slicingnum):
        time+=length
        matrixs=matrix[:]
        for i in range(len(matrix)):
            matrix[i]=createmat(time,matrixs)[i]
        print ["%.4f" %time] + matrixs[:]
            
        
###########################################################################

n=input("Numbers of Variable : ")
initial=float(input("Initial Time : "))
terminal=float(input("Terminal Time :"))
numinitial = int(input("Numbers of initial : "))
numslicing = int(input("Numbers of h : "))
assert initial<terminal
for j in range(numinitial):
    get_initial=[0]*n
    copylist = [0]*n
    for i in range(n):
        get_initial[i]=float(input("("+str(j+1)+") Initial Value of "+str(i+1)+"th value : "))
        copylist[i] = get_initial[i]
    for i in range(numslicing):
        for k in range(n):
            get_initial[k] = copylist[k]
        slicingnum=int(input(" ("+str(i+1)+") Time Slicing Number : "))
        length= ((terminal-initial)/slicingnum)
                ###########################################################################
        start()
a = input('x')
