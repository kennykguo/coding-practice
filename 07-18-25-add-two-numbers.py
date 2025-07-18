# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


        

        # list1 = []
        # list2 = []

        # while l1:
        #     list1.append(l1.val)
        #     l1 = l1.next
        
        
        # while l2:
        #     list2.append(l2.val)
        #     l2 = l2.next

        # num1 = 0
        # num2 = 0
        # length1 = len(list1) - 1
        # length2 = len(list2) - 1
        # print(list1)
        # print(list2)
        
        # for val in list1:
        #     num1 += val * pow(10, length1)
        #     length1 = length1 - 1
        
        # for val in list2:
        #     num2 += val * pow(10, length2)
        #     length2 = length2 - 1
        
        # return num1 + num2


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_on = 0
        prev1 = None
        prev2 = None
        res = l1
        
        while l1 and l2:
            val = l1.val + l2.val + carry_on
            carry_on = 0 # used carry out reset it now
            if val > 9: # carry out?
                val = val - 10
                carry_on = 1
            
            l1.val = val # save the value
            prev1 = l1
            prev2 = l2
            l1 = l1.next
            l2 = l2.next
        

        # here, edge cases - l1 longer, l2 longer, or carry on
        # l1 longer still
        if l1:
            while l1:
                val = l1.val + carry_on
                carry_on = 0 # used carry out reset it now
                if val > 9: # carry out?
                    val = val - 10
                    carry_on = 1
                l1.val = val # save the value
                prev1 = l1
                l1 = l1.next
            
            if carry_on:
                prev1.next = ListNode(1, None)
            return res


        
        # l2 longer
        if l2:
            prev1.next = l2
            print(l2.val)
            while l2:
                val = l2.val + carry_on
                carry_on = 0 # used carry out reset it now
                if val > 9: # carry out?
                    val = val - 10
                    carry_on = 1
                l2.val = val
                prev2 = l2
                l2 = l2.next

            if carry_on:
                prev2.next = ListNode(1, None)
            return res
        
        # both same length
        if carry_on:
            prev1.next = ListNode(1, None)
        return res
        
        
