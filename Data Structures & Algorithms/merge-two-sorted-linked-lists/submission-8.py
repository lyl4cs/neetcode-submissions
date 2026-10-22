# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # make dummy list
        # compare each number 1 node from list 1 and list 2
        # which ever one is smaller goes first then the bigger goes after
        # continue until list is sorted
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 # "appending" to dummy node
                tail = tail.next
                list1 = list1.next #move forward now
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        tail.next = list1 or list2

        return dummy.next