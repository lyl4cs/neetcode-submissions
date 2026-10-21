# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        behind = None # since we are starting at the head 
        # behind the head should be nothing
        curr = head # setting the head to where we are at currently
        # now we loop until end
        while curr != None:
            nxt = curr.next
            curr.next = behind
            behind = curr 
            curr = nxt

        return behind
            