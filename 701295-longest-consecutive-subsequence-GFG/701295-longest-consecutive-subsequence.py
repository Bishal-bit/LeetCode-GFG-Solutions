class Solution:
    def longestConsecutive(self, arr):
        # code here
        #Pass whole list to a set
        s=set(arr)
        #Initialize maxi as 0
        maxi=0
        #Traverse for each and every element
        for it in arr :
            target=it   #Store target=it 
            #If target-1 not in set then it might be the start of a consequtive sequence
            if target-1 not in s:
                count=0     #Store count as 0
                while target in s:
                    #If target found then increment count,update maxi, increment target
                    count+=1 
                    maxi=max(maxi,count)
                    target+=1
        #Return maxi
        return maxi            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna