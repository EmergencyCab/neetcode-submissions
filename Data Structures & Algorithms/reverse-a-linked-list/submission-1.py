# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 

        while curr != None:
            next_node = curr.next 
            curr.next = prev 
            prev = curr
            curr = next_node 
        return prev


# 1->2->3->None
# prev = None 
# curr = 1 (1 != None ) 
# next = 2
# curr.next -> 1.next = prev ( None <-1 2->3->None)

#prev = 1 
#curr = 2 

#Now curr(2) != None 
#next = 2.next (3)
#2.next = prev = (None <- 1 <- 2 3 -> None)

#prev = curr =2 
#curr = 3 

#Now curr(3) != None 
#next = curr.next 3.next = NONE
#3.next = prev (None <- 1 <-2 <-3  NONE)

#prev = curr =3 
#curr = NONE (DONE)
     
