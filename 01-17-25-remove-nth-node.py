# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = None
        cur = head

        length = 0
        while cur:
            length += 1
            cur = cur.next

        cur = dummy
        total_count = length - n + 1

        while total_count!=0:
            total_count -= 1
            prev = cur
            cur = cur.next
        
        # Remove the node properly
        print(prev.val)
        print(cur.val)
        prev.next = cur.next
        cur.next = None

        return dummy.next
