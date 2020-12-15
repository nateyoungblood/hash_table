
# Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
# If an integer appears in the list multiple times, each copy is considered to be different;
# that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, 
# even if they include the same values.

arr_1 = [1, 5, 3, 3, 3]

k=6

def numberOfWays(arr, k):
    ways=0
    for x in range(len(arr)): #O(N^2)
        for y in range(len(arr)):
            if arr[x]+arr[y]==k and x!=y:
                ways=ways+1
    print(ways/2)
    
# numberOfWays(arr_1,k)    

def second(arr,k):
    hash={}
    for x in range(len(arr)):
        hash[arr[x]]=0
    for x in range(len(arr)):
        if hash[arr[x]] is not None:
            hash[arr[x]]=hash[arr[x]]+1
        else:
            hash[arr[x]]=1
    print(hash)
        
second(arr_1,k)
        