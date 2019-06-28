# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         initializing a listNode with initial value zero
        result = ListNode(0)
        current = result
        carry = 0     
        # run the loop till any of the Linked list  l1 or l2 or carry is not empty
        while l1 or l2 or carry:
        # assign the value of l1 to val1
            val1 = (l1.val if l1 else 0)
        # assign the value of l2 to val2
            val2 = (l2.val if l2 else 0)
        #  divmod is an inbuilt python function that stores the value as (quotient, reminder)
            carry,out = divmod(val1+val2+carry,10)
        # add the carry to be used in the next iteration     
            current.next = ListNode(out)
            current = current.next
        # simultaneously iterate over both l1 and l2 
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return result.next
