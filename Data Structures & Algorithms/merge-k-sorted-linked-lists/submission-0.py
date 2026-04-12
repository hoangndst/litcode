# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next

        nodes.sort()

        res = ListNode(0)
        curr = res
        for val in nodes:
            curr.next = ListNode(val)
            curr = curr.next

        return res.next
