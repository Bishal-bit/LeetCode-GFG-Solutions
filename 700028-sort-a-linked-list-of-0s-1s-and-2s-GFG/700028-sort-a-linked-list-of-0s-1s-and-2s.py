'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        temp=head
        zero=zerohead=Node(-1)
        one=onehead=Node(-1)
        two=twohead=Node(-1)
        while temp :
            nex=temp.next
            temp.next=None
            if temp.data==0 :
                zero.next=temp
                zero=zero.next
            elif temp.data==1 :
                one.next=temp
                one=one.next
            else :
                two.next=temp
                two=two.next
            temp=nex
        #Point last LL's node to None 
        two.next=None
        
        #Connect as 0--1--2 based on avaibility
        if zerohead.next :
            if onehead.next : 
                zero.next=onehead.next
                if twohead.next : one.next=twohead.next
            else : zero.next=twohead.next
        elif onehead.next :
            if twohead.next : one.next=twohead.next
        
        #Return LL        
        if  zerohead.next : return zerohead.next
        elif onehead.next : return onehead.next
        return twohead.next
        
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna