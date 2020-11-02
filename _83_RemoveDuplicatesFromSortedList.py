# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        # 1  ->  1  ->   2
        # cur   cur.next cur.next.next
        
        cur = head
        while cur and cur.next:
            # 如果重复：指针连到下下个节点
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else: #不重复，往后走
                cur = cur.next
        return head
