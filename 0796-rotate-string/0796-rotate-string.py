class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ns, ng=len(s), len(goal)
        #If length is different then return False
        if ns!=ng : return False
        s+=s
        #Check if goal is a part of s or not
        if s.find(goal)!=-1 : return True
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna