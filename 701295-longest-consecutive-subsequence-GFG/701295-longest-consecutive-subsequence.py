class Solution:
    def longestConsecutive(self, arr):
        # code here
        #Pass whole list to a set
        st=set(arr)
        #Initialize maxi as 0
        maxi=0
        for it in arr :
            #If it-1 in set then continue
            if it-1 in st : continue
            target=it       #Store target=it 
            count=0         #Store count as 0
            while target in st : 
                #If target found then increment count,increment target
                count+=1
                target+=1
            #Update maxi
            maxi=max(maxi, count)
        #Return maxi
        return maxi
        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna