class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m=len(matrix), len(matrix[0])
        top=0
        bottom=n-1
        left=0
        right=m-1
        ans=[]
        while top<=bottom and left<=right :
            #Print Top Row
            for i in range(left,right+1) :
                ans.append(matrix[top][i])
            top+=1
            #Print Right Column
            for i in range(top,bottom+1) :
                ans.append(matrix[i][right])
            right-=1
            #Print Bottom Row
            if top<=bottom :
                for i in range(right,left-1,-1) :
                    ans.append(matrix[bottom][i])
                bottom-=1
            #Print Left Column
            if left<=right :
                for i in range(bottom,top-1,-1) :
                    ans.append(matrix[i][left])
                left+=1
        #Return ans
        return ans


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna