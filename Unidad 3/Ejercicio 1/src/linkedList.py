import json
from typing import TypeVar, List, Generic, Optional
import array

U = TypeVar('U')

class LinkedList(Generic[U]):

    def __init__(self, U):
        self._head: Optional = None
        self._NodeType = type(U)
        self.hash_set : set = set()

    def all_keys(self):
        return hash_set

    def all_values(self):
        values = []
        tmp = self.head

        while tmp is not None:
            values.append(tmp.value.to_dict())
            tmp = tmp.next
        return values

    def all(self):
        dic = {}
        tmp = self.head

        while tmp is not None:
            dic[tmp.hash_key]=tmp.value
            tmp = tmp.next
        return dic

    @property
    def head(self) -> U | None:
        return self._head

    def insert_at_beginning(self, item : U) -> U | None:
        
        #print("insert at beginning starts ok")
        key = item.hash_key
        if key in self.hash_set or self.getNode(item.id) is not None: return None

        #print(f"id: {item.id}, hash: {key}")

        oldHead = self.head
        newNode = LinkedNode(item, oldHead)
        self._head = newNode
        self.hash_set.add(key)
        return item   
        
    def insert(self, item : U) -> U | None:
        
        if not hasattr(item, 'hash_key'): return None
        
        key = item.hash_key
        if(key in self.hash_set): return None

        oldHead = self.head
        newNode = LinkedNode(item, None, oldHead)
        oldHead.prev = newNode
        self._head = newNode
        return newNode   

    def display(head):
        current = head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        
    def deleteNode(self, key : str | U): 
        newKey = hash(key)
        if newKey not in self.hash_set: return None

        # Store head node 
        tmp = self.head 

        # If head node itself holds the key to be deleted 
        if (tmp is not None): 
            if (tmp.data.hash_key == newKey): 
                self._head = tmp.next
                tmp = None
                return

        prev = None
        # Search for the key to be deleted, keep track of the 
        # previous node as we need to change 'prev.next' 
        while(tmp is not None): 
            if tmp.data.hash_key == newKey: 
                break
            prev = tmp 
            tmp = tmp.next

        # if key was not present in linked list 
        if(tmp == None): 
            return

        # Unlink the node from linked list 
        prev.next = tmp.next
        self.hash_set.remove(newKey)
        tmp = None

    def getNode(self, order_id : int) -> U | None:
        key = hash(order_id) 
        tmp = self.head 
        if (tmp is not None): 
            if tmp.hash_key == key: 
                print(tmp)
                return tmp

        while(tmp is not None): 
            if tmp.hash_key == key: 
                return tmp
            tmp = tmp.next

        return None

    def isInList(self, value : U) -> U | None:
        if value.hash_key not in self.hash_set: return None
        return value.hash_key

    def setNode(self, value) -> U | None:
        
        node = self.getNode(value.hash_key)
        if node is not None:
            node.set_value(value)
            return value
        return None

    # Utility function to print the linked LinkedList 
    def printList(self): 
        tmp = self.head 
        while(tmp): 
            print (" %d" %(tmp.data)), 
            tmp = tmp.next       

V = TypeVar('V')

class LinkedNode(Generic[V]):

    def __init__(self, value : V, 
        next: Optional = None,
        ):
        self._value = value
        self.next = next

    @property
    def value(self):
        return self._value

    def to_dict(self):
        return self.value.to_dict() 

    def set_value(self, value : V):
        self._value = value
    
    @property
    def hash_key(self) -> str:
        return self._value.hash_key
