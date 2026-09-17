class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        # code here
        n=len(arr)
        arr.sort()
        dep.sort()
        platform=maxplatform=0
        i=j=0
        while i<n and j<n :
            if arr[i]<=dep[j] :
                #If train arrives before depurture of train from station
                #Then we need one more platform
                #So update platform, maxplatform, i
                platform+=1
                maxplatform=max(maxplatform, platform)
                i+=1
            else :
                #If train arrives after depurture of train from station 
                #Then one less platform also ok
                #So update platform, j
                platform-=1
                j+=1
        #Return maxplatform
        return maxplatform

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna