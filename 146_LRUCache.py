class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        if not self.head:
            return True

    def addNode(self, node):
        # add to front of the list
        if self.isEmpty():
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
        self.head = node

    def removeNode(self, node):
        # search for the item and remove it from the list
        if self.isEmpty():
            return None
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # store the node with each key
        self.cache = {}
        # head is most recently used item, tail is least recently used
        self.usage = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key].val
        self.usage.removeNode(self.cache[key])

        newNode = Node(key, val)
        self.usage.addNode(newNode)
        self.cache[key] = newNode
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.usage.removeNode(self.cache[key])
            updatedNode = Node(key, value)
            self.usage.addNode(updatedNode)
            self.cache[key] = updatedNode
        else:
            newNode = Node(key, value)
            if self.capacity == 0:
                toEvict = self.usage.tail
                self.usage.removeNode(toEvict)
                self.cache.pop(toEvict.key)
                self.capacity += 1

            self.usage.addNode(newNode)
            self.cache[key] = newNode
            self.capacity -= 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)