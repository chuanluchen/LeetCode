# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        cur = dummy
        digit_sum = 0
        
        #将当前digit分别加入digit_sum
        p1, p2 = l1, l2
        while p1 or p2:
            if p1:
                digit_sum += p1.val
                p1 = p1.next
            if p2:
                digit_sum += p2.val
                p2 = p2.next

            
            # 处理digit_sum: 形成链表
            cur.next = ListNode(digit_sum % 10)
            digit_sum = digit_sum // 10 # 记录需要进位的值
            cur = cur.next

            
        # 处理1|00000问题
        if digit_sum: cur.next = ListNode(1)
                
        return dummy.next
            
