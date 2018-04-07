import math

m, L, g, kl,kq = 1, 5, 9.8, 0.01, 0.0001

####################s########  Modifier  ####################################
def f(mat,j): #mat[0] = t, mat[1] = y, mat[2] = z, mat[3] = w
#mat[0] = t, mat[1] = x1', mat[2] = x1, mat[3] = x2', mat[4] = x2
    if j==0: 
        return None #Differentiation form of time Do not modify
    elif j==1 :
        return mat[2]
    elif j==2 :
        return (-m*g*math.sin(mat[1])-kl*L*mat[2]-kq*L*mat[2]*abs(L*mat[2]))/(m*L)
    elif j==3:
        return -mat[3]+2*math.cos(mat[1])*mat[2]+mat[1]+1+math.sin(mat[0])
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
    L = []
    K = 1.0
    matrix=get_initial
    time=initial
    print [time]+matrix
    matrixs=matrix[:]
    for i in range(len(matrix)):
            matrix[i]=createmat(time,matrixs)[i]   
    for i in range(slicingnum):
        time+=length
        T = [0]*len(matrixs)
        for i in range(len(matrixs)):
            T[i] = matrixs[i]
        matrixs=matrix[:]
        for i in range(len(matrix)):
            matrix[i]=createmat(time,matrixs)[i]
        print ["%.4f" %time] + matrixs[:]
        if max(abs(T[1]),abs(matrixs[1]),abs(matrix[1]))==abs(matrixs[1]) and abs(matrixs[1])<K:
            L.append(["%.4f" %time] + T[:]+matrixs[:]+matrix[:])
            K = K/10
    for i in range(len(L)):
        print L[i]
        
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
