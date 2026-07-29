class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Initialize buy as prices[0], maxprofit as float('-inf')
        buy=prices[0]
        maxprofit=float('-inf')
        for it in prices :
            #Count profit as it-buy
            profit=it-buy
            #Update maxprofit as max(maxprofit, profit)
            maxprofit=max(maxprofit, profit)
            #Update buy as min(buy,it)
            buy=min(buy,it)
        #Return maxprofit
        return maxprofit
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna