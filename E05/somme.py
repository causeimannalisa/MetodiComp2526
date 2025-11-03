import numpy as np
 
#   es0
def naturali(n):
    somma=0;
    i=0;
    while(i<=n):
        somma+=i
        i+=1
     
    return somma;
    
def radici(n):
    somma=0;
    arr=np.array(range(1,n+1))
    somma=np.sum(np.sqrt(arr))
    
    return somma;
    
#   es 1    

def sommaprod(n):
    num=range(1,n+1)
    somma=np.sum(num)
    prod=np.prod(num)
    
    return somma,prod
    
def potenza(n,alpha=1):
    lol=np.array(0);
    for i in range(1,n+1):
        tot=i**alpha
        lol=np.append(lol,tot)
        
    somm=np.sum(lol)
    return somm;
    