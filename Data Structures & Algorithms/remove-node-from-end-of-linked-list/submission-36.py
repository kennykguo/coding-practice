# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        dummy = ListNode(0)
        dummy.next = head # dummy -> head
        cur = dummy
        temp = dummy

        # find the length of the list
        length = 0
        while temp:
            temp = temp.next
            length +=1

        # if n == 1:
        #     dummy.next = None
        #     return dummy.next

        count = 0
        # iterate until length - n -> n from the end
        while count != length - n:
            prev = cur
            cur = cur.next
            count +=1
        print(cur.val)
        
        prev.next = cur.next
        cur.next = None
        return dummy.next

        
        