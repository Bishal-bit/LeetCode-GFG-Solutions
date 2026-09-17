class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        n=len(val)
        v=[]
        for i in range(n) :
            v.append([val[i], wt[i]])
        #Sort in Descending order keeping val/wt as deciding factor
        v.sort(key=lambda x : x[0]/x[1], reverse=True)
        amount=0
        for it in v :
            #If pair's wt is in capacity add val to amount & decrease capacity be wt
            if it[1]<=capacity : 
                amount+=it[0]
                capacity-=it[1]
            #If capacity is less than pair's wt then 
            #add to amount by (val/wt)*capacity
            elif it[1]>capacity and capacity>0 :
                amount+= it[0]/it[1]*capacity
                break
        return amount
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna