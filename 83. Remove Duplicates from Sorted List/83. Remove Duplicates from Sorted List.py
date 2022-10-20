# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            answer = []
            repeated = []
            current = head
            my_list = []
            while current:
                my_list.append(current.val)
                current = current.next
            for num in my_list:
                if num in answer:
                    answer.remove(num)
                    repeated.append(num)
                else:
                    if num not in repeated:
                        answer.append(num)
          
            if len(answer) == 0:
                current: Optional[ListNode]
                return current
            else:
                current =head

            count = 1
            for num in answer:
                current.val = num
                if count != len(answer):
                    current = current.next 
                    count += 1
                else:
                    current.next = None

            
            return head           
