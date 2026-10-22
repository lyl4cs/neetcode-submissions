# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #initalizing slow and fast
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
#reversing
        second = slow.next
        behind = None
        slow.next = None
        while second:
            nxt = second.next
            second.next = behind
            behind = second
            second = nxt

        first,second = head,behind
        while second:
            nxt1,nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first,second = nxt1,nxt2
