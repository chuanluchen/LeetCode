# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #  dummy   1   2   3   4   5     长度：l+1  走n+1
        #                  fast---->
        #  slow-------->
        # 快慢针：fast先走n+1步，fast/slow同时走
        # fast走到底时slow.next是要删除的值
        dummy = ListNode(0)
        dummy.next= head
        
        fast, slow = dummy, dummy
        
        for i in range(n + 1):
            fast = fast.next
            
        while fast: 
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next
