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
        
        #    1 -> 2 -> 2 -> 3
        #   pre  pre.next
        #             pre.next.next
        #  pre走到重复节点的前一个
        #  while去除：只要val = 重复值，去除当前点 -> 连到后一个
        
        # 有可能改变头节点
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        while pre.next and pre.next.next:
            # 找到重复节点
            if pre.next.val == pre.next.next.val:
                d_value = pre.next.val # 提取重复值
                while pre.next and pre.next.val == d_value: # 用while循环去除重复节点
                    pre.next=pre.next.next
            else:
                pre = pre.next
        return dummy.next
