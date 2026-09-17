class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five=ten=0
        for it in bills :
            #If it==5 then increment five
            if it==5 : five+=1
            #If it==10
                #If five is there, increment ten,decrement five.
                #else return false;
            elif it==10 : 
                if five :
                    ten+=1
                    five-=1
                else : return False
            #If it==20
                #If(five && ten) go for (five--,ten--) or if(five>=3) do (five-=3) 
                #else return false
            else :
                if five and ten :
                    five-=1
                    ten-=1
                elif five>=3 : five-=3
                else : return False
        return True



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna