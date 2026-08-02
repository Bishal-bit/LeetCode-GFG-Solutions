class Solution:
    def reverseWords(self, s: str) -> str:
        #s = "the sky is blue"
        #words=s.split()=["the", "sky", "is", "blue"]
        words=s.split()
        #words.reverse()=["blue", "is", "sky", "the"]
        words.reverse()
        #" ".join(words)="blue is sky the"
        return " ".join(words)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna