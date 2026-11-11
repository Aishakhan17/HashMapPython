class hashMap:

    def __init__(self, initialCapacity, loadFactor, size):
        self.initialCapacity = initialCapacity
        self.loadFactor = loadFactor
        self.size = size
        self.hashtable = [[] for _ in range(self.size)]

    def addKeyValuePair(self, key, value):
        hashedValue = self.getHashCode(key)
        print("hashedValue", hashedValue)
        bucket = self.hashtable[hashedValue]

        print("Checking if key exists in hashtable")
        keyExists = self.containsKey(key, bucket)
        if not keyExists:
            print("Key doesn't exist. Adding it to hash map ")
            bucket.append((key, value))
        else:
            recordedValue, recordedIndex = keyExists
            print(
                f"Key exists in the hash table with corresponding value {recordedValue}. Updating value to {value}"
            )
            bucket[recordedIndex] = (key, value)
            print("Values updated. Print to verify")
        self.printHashMap()

    def getKey(self, key):
        pass

    def containsKey(self, key, bucket):
        for idx, (recordedKey, recordedValue) in enumerate(bucket):
            if recordedKey == key:
                return recordedValue, idx
        return False

    def containsValue(self, value):
        pass

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def getHashCode(self, key):
        hashedValue = hash(key) % 10
        return hashedValue

    def printHashMap(self):
        print("self.hashtable", self.hashtable)

    def removeKey(self, key):
        pass

    def clear():
        pass


def main():
    newHashMap = hashMap(initialCapacity=50, loadFactor=0.75, size=10)
    newHashMap.addKeyValuePair("Ayesha", "Khan")
    newHashMap.printHashMap()


main()
