class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans=[]
        if not intervals : return ans
        #Sort intervals based on 0th element of each intervals
        intervals.sort(key=lambda x: x[0])
        
        #Store intervals[0] as prev
        prev=intervals[0]
        #Traverse from 1st element
        for it in intervals[1: ] :
            #If prev overlapped with it, update prev
            if it[0]<=prev[1] :
                prev[0]=min(prev[0],it[0])
                prev[1]=max(prev[1], it[1])
            
            #Else append prev to ans, update prev as prev=it
            else :
                ans.append(prev)
                prev=it
        
        #Append prev to ans
        ans.append(prev)
        #Return ans
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna