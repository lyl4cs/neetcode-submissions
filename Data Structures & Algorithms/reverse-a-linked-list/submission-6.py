# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Since we start at the head, I should make curr go to the head
        # which means behind me I have nothing.
        behind = None
        curr = head
        #while current is still in the list

        while curr != None:
            # i want to walk forward, pointing there
            nxt = curr.next
            # now im saying, I want to flip this list around point behind me
            curr.next = behind
            # im about to move forwards, I want to bring behind to where im at now before i move
            behind = curr
            # walk forward to where i pointed earlier
            curr = nxt
        # behind becomes the new head of the list when curr is none.
        return behind 