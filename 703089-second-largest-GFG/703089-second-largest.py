class Solution:
    def getSecondLargest(self, arr):
        # code here
        #Declare large and slarge as -inf
        large=slarge=float('-inf')
        for it in arr :
            #If element is greater than large then,
            #Update slarge as large and large as element (it)
            if it>large :
                slarge=large
                large=it
            #If slarge< element (it) <large then update slarge as it
            elif slarge<it<large :
                slarge=it
        #If slarge never updates itself then return -1 else return slarge
        return slarge if slarge!=float('-inf') else -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna