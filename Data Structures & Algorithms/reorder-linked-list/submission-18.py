# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        slow = head
        fast = head

        if head.next == None:
            return
        
        cutoff = None
        while fast and fast.next:
            cutoff = slow
            slow = slow.next
            fast = fast.next.next
        
        print("half", slow.val)
        print("cutoff", cutoff.val)
        cutoff.next = None

        # reverse starting from slow
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        print("end", prev.val) # prev now points to beginning of the new list
        # now just combine them

        slow = head
        
        while slow and prev:
            print(slow.val)
            # move slow
            temp1 = slow.next
            slow.next = prev
            slow = temp1

            # move temp
            if not temp1:
                continue
            temp2 = prev.next
            prev.next = temp1
            prev = temp2
        
        # if not:

        
        # return head

