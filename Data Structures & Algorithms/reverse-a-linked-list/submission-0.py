# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        temp = None
        while head != None:
            nxt = head.next
            head.next = temp
            temp = head
            head = nxt
        
        return temp
