class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        #Do Transpose operation
        for i in range(n) :
            for j in range(i+1,n) :
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        #Reverse each and every row
        for row in matrix : 
            row.reverse()
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna