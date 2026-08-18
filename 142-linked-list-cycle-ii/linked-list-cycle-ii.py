# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        while True:
            fast = fast.next if fast else None
            fast = fast.next if fast else None
            slow = slow.next if slow else None
            
            if slow == fast:
                break

        while slow != head:
            head = head.next if head else None
            slow = slow.next if slow else None            

        return head