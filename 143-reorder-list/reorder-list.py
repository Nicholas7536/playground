class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        first = []
        second = []
        slow = head
        fast = slow

        while fast is not None and fast.next is not None:
            first.append(ListNode(slow.val))
            slow = slow.next
            fast = fast.next.next
      
        while slow is not None:
            second.append(ListNode(slow.val))
            slow = slow.next

        curr = head
        i = 1  
        j = len(second) - 1 
        while i < len(first) or j >= 0:
            if j >= 0:
                curr.next = second[j]
                curr = curr.next
                j -= 1
            if i < len(first):
                curr.next = first[i]
                curr = curr.next
                i += 1
                
        curr.next = None 