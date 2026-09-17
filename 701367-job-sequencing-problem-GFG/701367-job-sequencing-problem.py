class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        n=len(deadline)
        v=[]
        for i in range(n) :
            #Append profit, followed by deadline
            v.append([profit[i], deadline[i]])
        #Sort v in reverse order
        v.sort(reverse=True)
        maxd=max(deadline)          #Store maxd as highest deadline
        slots=[False] * (maxd+1)    #Create Slots=[False] * (maxd+1) 
        #Initialize count and maxprofit as 0
        count=maxprofit=0
        for it in v :
            dis=it[1]       #Store it's deadline
            for it1 in range(dis, 0, -1) : #dis----1
                #If not slots[it] then make it True, increment count,
                #Add profit to maxprofit and break
                if not slots[it1] :
                    slots[it1]=True
                    count+=1
                    maxprofit+=it[0]
                    break
        #Return [count, maxprofit]
        return [count, maxprofit]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna