class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=[]
        count=0
        for it in s :
            #If it==Outermost opening, count==0 then increment count, dont add it to ans string
            if it=='(' and count==0 : count+=1
            #If it==opening, count>=1 then increment count, add it to ans string
            elif it=='(' and count>=1 :
                count+=1
                ans.append(it)
            #If it==closing, count>1 then decrement count, add it to ans string
            elif it==')' and count>1 :
                count-=1
                ans.append(it)
            #If it==Outermost closing, count==1 then decrement count, dont add it to ans string
            elif it==')' and count==1 : count-=1
        #Function expects return type as string. So convert list to string
        return "".join(ans)
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna