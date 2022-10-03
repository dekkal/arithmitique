
def Srec(x,N):
    s=0
    if(len(x))==1:
        return x

    # else :
    #     if (len(x))==2:
    #         s=x[0]+x[1]
    #         return s

    #     else:
    #         N2=N//2
    #         for i in range (1,N2+1):
    #             x[i]=x[2*i-1]+x[2*i]
    #         N=N2

    #     return Srec(x,N2)
    
x=[10,2]
N=len(x)
res=Srec(x,N)
print("res",res)