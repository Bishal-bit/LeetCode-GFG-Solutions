class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1 : return True
        if n%2==1 : return False
        for i in range(int(100)) :
            if 2**i==n : return True
            if i>n : return False
        return False 
       

