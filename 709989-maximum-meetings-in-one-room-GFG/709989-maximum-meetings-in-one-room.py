class Solution:
    def maxMeetings(self, s, f):
        # code here
        n=len(s)
        v=[]
        #Pass start and ending time to a list v
        for i in range(n) :
            v.append([s[i], f[i], i])
        #Always choose the meeting that finishes earliest
        #If finish time same then keep lower index at early position
        v.sort(key=lambda x: (x[1], x[2]))
        #Initialize end as -1 as we dont want it to cause issue initially
        end=-1      
        ans=[]
        for it in v :
            #If end time of previous meeting and starting time of 
            #current meeting do not overlap then do append index+1, update end
            index=it[2]
            if end<it[0] : 
                ans.append(index+1)
                end=it[1]
        #Return sorted(ans)
        return sorted(ans)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna