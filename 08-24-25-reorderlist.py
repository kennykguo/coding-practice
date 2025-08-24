# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        
        # get the length of the list and split it in half, reverse the second half, then reorient
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        cur = head
        print(length)


        half_length = length // 2 # 5 // 2 = 2
        if length % 2 == 0:
            length -= 1

        while half_length:
            cur = cur.next
            half_length -= 1
        print(cur.val)
        
        # break the list up
        temp = cur.next
        cur.next = None

        # reverse second part of list
        cur = temp
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        print(prev.val)
        
        # prev now points to head of new list
        cur = head
        
        while cur and prev:
            temp1 = cur.next
            temp2 = prev.next
            cur.next = prev
            prev.next = temp1
            
            cur = temp1
            prev = temp2
        
        # return head
