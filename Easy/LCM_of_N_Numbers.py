import math

def GCD(a,b,origa,origb):
    if a%b == 0:
        return int(int(origa*origb)/int(b)) 
    else:
        return GCD(b,a%b,origa,origb)

N = list(map(int,input().split()))

def LCM(N):
    a = N[0]
    b = N[1]
    li = GCD(a,b,a,b)

    for i in range(2, len(N)):
        li = GCD(li,N[i],li,N[i])
    
    return li

print('LCM:',LCM(N))
