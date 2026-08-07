class Solution:
    def isValid(self, s: str) -> bool:
        #For odd length of string s, return False
        n=len(s)
        if n%2==1 : return False
        st=[]       #Declare stack st
        for it in s :
            #If there is open parentheses then push it to stack
            #If empty st is to be starting with close parentheses then return False
            #Check combo pop outs : (), {}, []
            #Else push it in st
            if it=="(" or it=="{" or it=="[" : st.append(it)
            elif not st and (it==")" or it=="}" or it=="]") : return False
            elif it==")" and st[-1]=="(" : st.pop()
            elif it=="}" and st[-1]=="{" : st.pop()
            elif it=="]" and st[-1]=="[" : st.pop()
            else : st.append(it)
        #If we get empty stack at the end then return True
        #Else return False
        if not st : return True
        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna