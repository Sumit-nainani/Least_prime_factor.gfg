# Given a number N, find the least prime factors for all numbers from 1 to N.  
# The least prime factor of an integer X is the smallest prime number that divides it.
# Note :
# 1 needs to be printed for 1.
# You need to return an array/vector/list of size N+1 and need to use 1-based indexing to store the answer for each number.


# approach:
#     we will do this by applying seive algorithm of finding lowest prime
#     we can modify this by finding highest prime also by removing the condition in line  if(a[j]==0 ):
#     time - o(nlogn)


def leastPrimeFactor (self, n):
        # code here 
        a=[0]*(n+1)
        p=[1]*(n+1)
        a[1]=1
        for i in range(2,n+1):
            if p[i]==1:
               a[i]=i
               for j in range(2*i,n+1,i):
                   if(a[j]==0 ):
                       a[j]=i
                   p[j]=0
        return a