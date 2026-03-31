# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        prev, curr = head, head.next

        while prev != None and curr != None and curr.next != None:
            if prev == curr:
                return True
            
            prev = prev.next
            curr = curr.next.next
        
        return False

