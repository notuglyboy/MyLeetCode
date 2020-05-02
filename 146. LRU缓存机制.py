class ListNode(object):
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.map = {}
        self.head = None
        self.capacity = capacity
        self.list_len = 0
        self.tail = None

    def move_to_head(self, node):
        if node == self.head:
            return
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

    def insert_node(self,node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node
        
    #@myprint
    def get(self, key):
        node = self.map.get(key)
        if not node:
            return -1
        if node != self.head:
            self.move_to_head(node)
        return node.value

    def put(self, key, value):
        if not self.map.get(key):
            node = ListNode(key, value)
            self.insert_node(node)
            if self.list_len >= self.capacity:
                tail_tmp = self.tail
                self.tail = tail_tmp.prev
                self.tail.next = None
                del self.map[tail_tmp.key]
            else:
                self.list_len += 1
            self.map[key] = node
        elif self.map[key].value != value:
            tmp_node = self.map[key]
            tmp_node.value = value
            if tmp_node != self.head:
                self.move_to_head(tmp_node)