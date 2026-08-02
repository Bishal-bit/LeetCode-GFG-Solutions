class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        sign, ans=1, 0
        i=0
        #Ignore any leading whitespace
        while i<n and s[i]==" " : i+=1
        #For empty string " "
        if i==n : return 0
        #Determine the sign as (+)ve or (-)ve
        if s[i]=="-" : 
            sign=-1
            i+=1
        elif s[i]=="+" : 
            sign=1
            i+=1
        #Skip leading zeros
        while i<n and s[i]=="0" : i+=1
        #Count integer and check if it is digit or not
        #Dont forget to check overflow part
        while i<n and s[i].isdigit():
            ans=ans*10 + ord(s[i])-ord("0")
            if sign*ans > 2**31-1 : return 2**31-1 
            elif sign*ans < -(2**31) : return -(2**31) 
            i+=1
        return sign*ans


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna