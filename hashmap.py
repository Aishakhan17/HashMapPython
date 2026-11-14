class hashMap:

    def __init__(self, initialCapacity, loadFactor, size):
        self.initialCapacity = initialCapacity
        self.loadFactor = loadFactor
        self.initSize = size
        self.currentSize = 0
        self.hashtable = [[] for _ in range(self.initSize)]
        self.backup = []
        self.resize = False

    def addKeyValuePair(self, key, value):
        hashedValue = self.getHashCodeOne(key)
        bucket = self.hashtable[hashedValue]

        print("Checking if key exists in hashtable")
        keyExists = self.containsKey(key, bucket)
        if not keyExists:
            print("Key doesn't exist. Adding it to hash map ")
            bucket.append((key, value))
            self.currentSize += 1
        else:
            recordedValue, recordedIndex = keyExists
            print(
                f"Key exists in the hash table with corresponding value {recordedValue}. Updating value to {value}"
            )
            bucket[recordedIndex] = (key, value)
            print("Values updated. Print to verify")
        self.checkForResizing()
        if self.resize:
            print("Load capacity exceeded, resizing hashmap, current hashmap is: ")
            self.printHashMap()
            self.resizeHashMap()
        self.printHashMap()

    def getKey(self, key):
        hashValue = self.getHashCodeOne(key)
        try:
            targetBucket = self.hashtable[hashValue]
            if targetBucket[0] == key:
                print(f"found key {key}, targetBucket is", {hashValue})
                return targetBucket
        except:
            print("Key does not exist. Would you like to add it? Y/N")
            text = input()
            if text.lower() == "yes" or text.lower() == "y":
                try:
                    print("Enter corresponding value for the key: ")
                    inputValue = input()
                    self.addKeyValuePair(key, str(inputValue))
                    print("Added to hashmap")
                except:
                    print("There was an issue adding the key value pair")
                    return False
            elif text == "no" or text == "n":
                print("Key not added as requested")
            else:
                print("There was an issue, try again!")

    def containsKey(self, key, bucket):
        for idx, (recordedKey, recordedValue) in enumerate(bucket):
            if recordedKey == key:
                return recordedValue, idx
        return False

    def containsValue(self, value):
        for bucket in range(self.currentSize):
            for recordedKey, recordedValue in self.hashtable[bucket]:
                if recordedValue == value:
                    print(
                        f"Found the value {recordedValue} and the corresponding key is {recordedKey} in bucket {bucket}"
                    )
                    return recordedValue
                else:
                    print("Value does not exist in the hashmap")

    def checkForResizing(self):
        if self.currentSize / self.initSize >= self.loadFactor:
            self.resize = True

    def resizeHashMap(self):
        self.initSize *= 2
        self.backupExistingPairs()
        print("self.initSize", self.initSize)
        self.hashtable = [[] for _ in range(self.initSize)]
        print("resized hashtable is: ", self.hashtable)
        # self.reinsertExistingPairs()
        # self.backup = []
        # print("back up reset", self.backup)

    def backupExistingPairs(self):
        print("Backing up existing pairs")
        for bucket in self.hashtable:
            print("bucket", bucket, "len(bucket)", len(bucket))
            if len(bucket) > 0:
                self.backup.append(bucket)
        print("Successfully backed up current hashmap data", self.backup)

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

    def getHashCodeOne(self, key):
        print("hash(key)", hash(key))
        hashedValue = hash(key) % self.initSize
        print("hashedValue", hashedValue)

        return hashedValue

    # def getHashCodeTwo(self, key):
    #     hashedValue
    #     print("second hash value")
    #     return hashedValue

    def printHashMap(self):
        print("self.hashtable", self.hashtable)

    def removeKey(self, key):
        print("remove key called")
        for idx in range(self.initSize):
            if len(self.hashtable[idx]) != 0:
                curr = self.hashtable[idx][0][0]
                if curr == key:
                    print("found", curr)
                    self.hashtable.pop(idx)
                    print("Removed key")
                    break
        print("Error: Key does not exist in the hashmap")

    def clear(self):
        self.hashtable = [[] for _ in range(self.initSize)]
        self.currentSize = 0
        print("Deleted hashmap")


def main():
    newHashMap = hashMap(initialCapacity=50, loadFactor=0.75, size=10)
    newHashMap.getSize()
    keyValuePairs = [
        ("Ayesha", "Khan"),
        ("Caolan", "Durrel-Loughlin"),
        ("Dobby", "Khan"),
        ("Marlow", "Schmarlow-Khan"),
        ("John", "Smith"),
        ("Abby", "Smith"),
        ("Emma", "Airey"),
    ]
    for entry in keyValuePairs:
        print("entry", entry)
        key = entry[0]
        value = entry[-1]
        newHashMap.addKeyValuePair(key, value)
    newHashMap.printHashMap()
    # newHashMap.getKey("Ayesha")
    # newHashMap.containsValue("Khan")
    # newHashMap.getKey("Dobby")
    # newHashMap.getSize()
    # newHashMap.printHashMap()
    # newHashMap.removeKey("Dobby")
    # newHashMap.printHashMap()
    # newHashMap.clear()
    # newHashMap.printHashMap()


main()
