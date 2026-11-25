from linkedlist import *


class hashMap:

    def __init__(self, loadFactor, size, collisionHandlingMethod):
        self.loadFactor = loadFactor
        self.initSize = size
        self.currentSize = 0
        self.backup = []
        self.resize = False
        self.collisionHandlingMethod = collisionHandlingMethod
        if self.collisionHandlingMethod == "SC":
            self.initializeLinkedListTable()
        else:
            self.hashtable = [[] for _ in range(self.initSize)]

    def initializeLinkedListTable(self):
        self.hashtable = []
        for _ in range(self.initSize):
            llist = LinkedList()
            self.hashtable.append(llist)
        self.printHashMap()

    def addKeyValuePair(self, key, value):
        hashedValue = self.getFirstHashCode(key)
        bucket = self.hashtable[hashedValue]
        if self.collisionHandlingMethod == "SC":
            print("Checking if key exists in hashtable")
            if bucket.head == None:
                print("Key does not exist. Adding it to Hashmap")
                node = Node(key=key, value=value)
                bucket.head = node
            else:
                print("There's a collision. Adding to linked list")
                curr = bucket.head
                while curr is not None:
                    if curr.next == None:
                        node = Node(key=key, value=value)
                        curr.next = node
                        break
                    curr = curr.next
            self.currentSize += 1

        self.checkForResizing()
        if self.resize:
            print("Load capacity exceeded, resizing hashmap, current hashmap is: ")
            self.resizeHashMap()

    def getKey(self, key):
        hashedValue = self.getFirstHashCode(key)
        result = []
        bucket = self.hashtable[hashedValue]
        if bucket.head is not None:
            curr = bucket.head
            while curr is not None:
                if curr.key == key:
                    result.append((curr.key, curr.value))
                curr = curr.next
        return result

    def getValue(self, value):
        result = []
        for bucket in self.hashtable:
            if bucket.head is not None:
                curr = bucket.head
                while curr is not None:
                    if curr.value == value:
                        result.append((curr.key, curr.value))
                    curr = curr.next
        return result

    def checkForResizing(self):
        if self.currentSize / self.initSize >= self.loadFactor:
            print("needs resizing")
            self.resize = True

    def resizeHashMap(self):
        self.resize = False
        self.initSize *= 2
        self.backupExistingPairs()
        self.initializeLinkedListTable()
        self.currentSize = 0
        self.reinsertExistingPairs()
        self.backup = []

    def backupExistingPairs(self):
        print("Backing up existing pairs")
        for bucket in self.hashtable:
            if bucket.head is not None:
                curr = bucket.head
                while curr is not None:
                    self.backup.append((curr.key, curr.value))
                    curr = curr.next
        print("Backed up successfully")

    def reinsertExistingPairs(self):
        print("Rehashing and reinserting current data from back up")
        for pairs in self.backup:
            self.addKeyValuePair(pairs[0], pairs[-1])
        print("Successfully rehashed and reinserted data")

    def isEmpty(self):
        return self.currentSize == 0

    def getSize(self):
        print("Current hashmap size is: ", self.currentSize)
        return self.currentSize

    def getFirstHashCode(self, key):
        hashedValue = hash(key) % self.initSize
        return hashedValue

    def printHashMap(self):
        if self.collisionHandlingMethod == "SC":
            for bucket in self.hashtable:
                if bucket.head is not None:
                    curr = bucket.head
                    while curr is not None:
                        print("curr.key", curr.key, "curr.value", curr.value)
                        curr = curr.next

        else:
            print("self.hashtable", self.hashtable)

    def removeKeyValuePair(self, key, value):
        for bucket in self.hashtable:
            if bucket.head is not None:
                curr = bucket.head
                prev = None
                while curr is not None:
                    if curr.key == key and curr.value == value:
                        print("found", curr.key, prev)
                        if prev is not None:
                            prev.next = curr.next
                        elif prev is None and curr.next:
                            prev = curr.next
                            bucket.head = prev
                        else:
                            bucket.head = None
                        self.currentSize -= 1
                        print("Deleted Key successfully")
                        return
                    prev = curr
                    curr = curr.next

    def clear(self):
        self.hashtable = [[] for _ in range(self.initSize)]
        self.currentSize = 0
        print("Deleted hashmap")


def main():
    newHashMap = hashMap(loadFactor=0.75, size=10, collisionHandlingMethod="SC")
    newHashMap.getSize()
    keyValuePairs = [
        ("Ayesha", "Khan"),
        ("Caolan", "Durrel-Loughlin"),
        ("Dobby", "Khan"),
        ("Marlow", "Schmarlow-Khan"),
        ("John", "Smith"),
        ("Abby", "Smith"),
        ("Emma", "Airey"),
        ("Mona", "Lisa"),
    ]
    for entry in keyValuePairs:
        print("entry", entry)
        key = entry[0]
        value = entry[-1]
        newHashMap.addKeyValuePair(key, value)
    newHashMap.printHashMap()
    result = newHashMap.getKey("Ayesha")
    if result:
        print(f"Found the following keys that match the search")
        for pair in result:
            print(f"key {pair[0]} with the following corresponding value {pair[-1]}")
    result = newHashMap.getValue("Smith")
    if result:
        print(f"Found the following values that match the search")
        for pair in result:
            print(f"value {pair[-1]} with the following corresponding key {pair[0]}")
    size = newHashMap.getSize()
    print("Current hashmap size is: ", size)

    newHashMap.printHashMap()
    newHashMap.removeKeyValuePair("Dobby", "Khan")
    newHashMap.printHashMap()
    size = newHashMap.getSize()
    print("Current hashmap size is: ", size)
    # newHashMap.clear()
    # newHashMap.printHashMap()


main()
