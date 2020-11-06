# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    ## 链表版的MergeSort
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        # MergeSort
        mid = self.getMiddle(head)
        nextPart = mid.next
        mid.next = None
        return self.merge(self.sortList(head), self.sortList(nextPart))
    
    # 找中点：快慢针      
    def getMiddle(self, head):
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    
    # merge two sorted lists
    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next= ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        if l1: cur.next=  l1
        if l2: cur.next = l2
        return dummy.next
