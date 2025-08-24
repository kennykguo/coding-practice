# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_two(l1, l2):
            dummy = ListNode(0, None)
            cur = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    l1 = l1.next
                cur = cur.next

            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            
            return dummy.next

        if not lists:
            return None
          
        while len(lists) > 1:
            print("here")
            new = []
            for i in range(0, len(lists), 2):
                print("here1")
                if i + 1 < len(lists): # two elements available to merge
                    new.append(merge_two(lists[i], lists[i + 1]))
                    print(new)
                else: # only one element available to merge
                    new.append(merge_two(lists[i], None))
                    print(new)
            lists = new
        
        return lists[0]
            

            

