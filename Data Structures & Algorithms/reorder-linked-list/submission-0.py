# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return None
        
        slow, fast = head, head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        
        def reverse(head: Optional[ListNode]):
            prev, curr = None, head

            while curr != None:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            return prev

        head2 = slow.next
        slow.next = None
        head2 = reverse(head2)

        node = head
        node2 = head2

        while node != None and node2 != None:
            tmp = node.next
            node.next = node2
            tmp2 = node2.next
            node2.next = tmp
            node2 = tmp2
            node = tmp


        
        
        
