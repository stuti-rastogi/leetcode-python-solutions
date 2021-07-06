class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]

    

# class Node:
#     def __init__(self, page):
#         self.val = page
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self, headNode):
#         self.head = headNode
        
#     def append(self, currNode, newNode):
#         currNode.next = newNode
#         newNode.prev = currNode
        
#     def printList(self):
#         curr = self.head
#         while curr:
#             print (curr.val, end=" ")
#             curr = curr.next
#         print ()
    
# class BrowserHistory:
#     def __init__(self, homepage: str):
#         self.curr = Node(homepage)
#         self.pages = DoublyLinkedList(self.curr)

#     def visit(self, url: str) -> None:
#         newNode = Node(url)
#         self.pages.append(self.curr, newNode)
#         self.curr = newNode

#     def back(self, steps: int) -> str:
#         count = 0
#         while count < steps and self.curr.prev:
#             self.curr = self.curr.prev
#             count += 1
#         return self.curr.val

#     def forward(self, steps: int) -> str:
#         count = 0
#         while count < steps and self.curr.next:
#             self.curr = self.curr.next
#             count += 1
#         return self.curr.val
        


# # Your BrowserHistory object will be instantiated and called as such:
# # obj = BrowserHistory(homepage)
# # obj.visit(url)
# # param_2 = obj.back(steps)
# # param_3 = obj.forward(steps)