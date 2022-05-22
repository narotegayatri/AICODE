N=int(input("Enter the value of n: "))
L=[['--' for i in range(N)]for i in range(N)]


def printBoard(B):
    print("Solution :")
    for i in range (N):
        for j in range (N):
            print(L[i][j],end=" ")
        print("")
        
def Check(L,row,col):
    #RoW
    if(row==r and col==c):
        return False
    
    for i in range(col):
        if(L[row][i]!='--'):
            return False
        
    #Column
    for j in range(row):
        if(L[j][col]!='--'):
            return False
    
    #UL-Diagonal
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if(L[i][j]!='--'):
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,N,1)):
        if(L[i][j]!='--'):
            return False
        
    
    #LL-Diagonal
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if(L[i][j]!='--'):
            return False
        
    for i,j in zip(range(row,N,1),range(col,N,1)):
        if(L[i][j]!='--'):
            return False
      
      
    
    
    #all conditions ok
    return True

def NQueen(L,col):
    
    #base condition
    if col >=N:
        return True

    for i in range(N):
        if(Check(L,i,col)):
            
            #place Queen
            L[i][col]='Q'+str(i)
            
            if(NQueen(L,col+1)):
                return True
            
            #backtrack
            L[i][col]='--'
        
    return False
    
def Solve():
    
    if(NQueen(L,0)==False):    
        print("Solution Not Exit")
        return False
    
    printBoard(L)
    return True

r,c=map(int,input("Queen cannot be placed at:").split(','))
Solve()
