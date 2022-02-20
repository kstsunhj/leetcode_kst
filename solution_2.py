class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = ListNode()
        current.next = l1
        
        while True:
            current.next.val += l2.val
            
            # Carry
            if current.next.val >= 10 and current.next.next != None:
                current.next.val -= 10
                current.next.next.val += 1
            elif current.next.val >= 10 and current.next.next == None:
                current.next.val -= 10
                current.next.next = ListNode(1)
            
            # Forward
            if current.next.next != None:
                current.next = current.next.next
            else:
                current.next.next = l2.next
                current.next = current.next.next
                l2.next = None
                
            if l2.next != None:
                l2 = l2.next
            else:
                l2.val = 0
            
            if current.next == None and l2.next == None:
                break
        
        return l1