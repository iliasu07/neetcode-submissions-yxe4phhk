# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur is not None:
            nxt = cur.next  #None
            cur.next = prev  # 3 -> 2 -> 1 -> None
            prev = cur  # 3
            cur = nxt   # None
        head = prev

        return head