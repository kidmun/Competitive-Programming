# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 1
        while(current.next):
            count += 1
            current = current.next
         
        
        
        middle = int(count/2)
        new_current = head
        new_count = 0

        while (new_current.next):
            if new_count == middle:
                return new_current
            new_count += 1
            new_current = new_current.next
        return new_current


    
        # for i in range(middle, len(head)):
        #     answer.append(head[i])
        # return answer