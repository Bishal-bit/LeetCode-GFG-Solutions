class Solution:
    def checkValidString(self, s: str) -> bool:
        low=high=0
        for ch in s :
            if ch=='(' :
                low+=1
                high+=1
            elif ch==')' :
                low-=1
                high-=1
            else :
                low-=1              # assume ')' for minimum
                high+=1             # assume '(' for maximum
            if high<0 : return False        #high < 0 : impossible
            low=max(0, low)
        return low==0                       #low == 0 : possible to make valid

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna