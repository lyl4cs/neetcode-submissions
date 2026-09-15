# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummyList = ListNode(0) # creating dummy node

        current = dummyList # creating current node

        while list1 and list2: # while list 1 and list 2 are not None
            if list1.val < list2.val: # if the value of list 1 is bigger then list 2 value
                current.next = list1 # list 1 value goes to dummy
                list1 = list1.next # moving the list 1 now to the next
            else:
                current.next = list2 # list 2 value goes to dummy
                list2 = list2.next # moving the list 2 now to next
            current = current.next
        current.next = list1 or list2

          



        return dummyList.next 
