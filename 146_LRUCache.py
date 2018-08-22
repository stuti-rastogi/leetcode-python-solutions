#define double linked list node (DLL) and used as cache
class Node(object):
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
        
class LRUCache(object):
    #define <key:node> hashtable, head node and tail node
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.hashTable={}
        self.hd=None
        self.tl=None
        
    #remove node from DLL
    def removeNode(self,node):
        #if the removed node is head, remove head
        if node==self.hd:
            self.hd=self.hd.next
            if self.hd:
                self.hd.prev=None
        #if the removed node is tail, removed tail
        elif node==self.tl:
            self.tl=self.tl.prev
            if self.tl:
                self.tl.next=None
        #if the removed node is in between some nodes
        else:
            node.prev.next=node.next
            node.next.prev=node.prev
        #delete key:node from hashtable
        del self.hashTable[node.key]   
        
    #add node to the head of the DLL
    def addFirst(self,node):
        #if the DLL is empty, the head and tail are both None, set head and tail (only used when initializing the DLL)
        if not self.hd:
            self.hd=node
            self.tl=node
        else:
        #otherwise, set the node as head
            node.next=self.hd
            node.prev=None
            self.hd.prev=node
            self.hd=node
        #add the <key:node> pair of the node to the hashtable
        self.hashTable[node.key]=node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashTable:
            return -1
        #save node data since we will delete the node in removeNode() function.
        tmp=Node(self.hashTable[key].key,self.hashTable[key].value)
        #delete node
        self.removeNode(self.hashTable[key])
        #add the node to head
        self.addFirst(tmp)
        #return the node value
        return self.hashTable[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        #if the key is in hashtable, update the node value and move the node to the head of the DLL
        if key in self.hashTable:
            #save node data since we will delete the node in removeNode() function.
            tmp=Node(self.hashTable[key].key,value)
            #delete node
            self.removeNode(self.hashTable[key])
            #add node to head of DLL
            self.addFirst(tmp)
        else:
            #if the key is not in the hashtable
            newNode=Node(key,value)
            #when the capacity is zero, no more space for new node
            if self.capacity==0:
                #remove tail node from DLL
                self.removeNode(self.tl)
                #since we remove a node, the capacity will restore space for one node
                self.capacity+=1
            #add new node to the DLL head
            self.addFirst(newNode)
            #since we add a node, the capacity will be less
            self.capacity-=1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)