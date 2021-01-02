# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp1= l1
        temp2 = l2
        dummy = ListNode(0)
        cur = dummy
        rem = 0
        while(temp1 is not None or temp2 is not None):
            val1 = temp1.val if temp1 is not None else 0
            val2 = temp2.val if temp2 is not None  else 0
            total = val1 + val2 + rem
            cur.next = ListNode(total%10)
            cur = cur.next
            rem = total//10
            temp1 = temp1.next if temp1 is not None else None
            temp2 = temp2.next if temp2 is not None else None
        if(rem > 0):
            cur.next = ListNode(rem)
        return dummy.next
        