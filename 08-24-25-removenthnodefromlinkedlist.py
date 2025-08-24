# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        
        # get the length
        cur = dummy.next
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        # get right before the node
        count = length - n # n = 1, length = 1, count = 0
        cur = dummy
        while count > 0:
            cur = cur.next
            count -= 1
        print(cur.val)

        # traversing from dummy covers edge case - at the very start

        # remove the current node
        if not cur.next: # edge case - at the very end
            return None
        else:
            cur.next = cur.next.next

        return dummy.next
