class Solution:
    import heapq
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #Kth Largest Element--> go for min heap
        heap=[]
        for it in nums :
            #heappush elements to heap
            heapq.heappush(heap, it)
            #If len(heap) exceeds k then do heappop operation
            if len(heap)> k : heapq.heappop(heap)
        
        #Return heap[0]
        return heap[0]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna