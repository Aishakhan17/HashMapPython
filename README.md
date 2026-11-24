## Dumping what I learnt and some implementation info

### Hash Maps

**Load Factor**
As a general rule, the default load factor (.75) offers a good tradeoff between time and space costs. Higher values decrease the space overhead but increase the lookup cost (reflected in most of the operations of the HashMap class, including get and put). The expected number of entries in the map and its load factor should be taken into account when setting its initial capacity, so as to minimize the number of rehash operations. If the initial capacity is greater than the maximum number of entries divided by the load factor, no rehash operations will ever occur.

**Collision Handling**
Collisions happen when two keys map to the same hashmap index. Several methods to resolve a collision: Separate chaining where each bucket in the hashmap is a linked list. In case of a collision, the new key value pair is added to the linkedlist. When fetching a key, you hash to get the bucket and then traverse the linked list until you find the key. There's also open addressing using linear probing, quadratic probing, double hashing.

**Double Hashing**
Two functions to hash a key.
Both serve the same purpose. They visit every bucket before they repeat themselves,
**Coprime Table Size and Step Size**
**Power of Two Table size**
