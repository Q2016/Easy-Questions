Question:
Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:
void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 
Example 1:
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]
Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Solution:
https://leetcode.com/problems/design-hashset/discuss/768659/Python-Easy-Multiplicative-Hash-explained  The goal of this problem is to 
create simple hash function, not using build-in methods. One of the simplest, but classical hashes are so-called Multiplicative 
hashing: https://en.wikipedia.org/wiki/Hash_function#Multiplicative_hashing.
The idea is to have hash function in the following form.
image

Here we use the following notations:

K is our number (key), we want to hash.
a is some big odd number (sometimes good idea to use prime number) I choose a = 1031237 without any special reason, it is just random odd number.
m is length in bits of output we wan to have. We are given, that we have no more than 10000 operations overall, so we can choose such m, so 
that 2^m > 10000. I chose m = 15, so in this case we have less collistions.
if you go to wikipedia, you can read that w is size of machine word. Here we do not really matter, what is this size, we can choose any w > m. I chose m = 20.
So, everything is ready for function eval_hash(key): ((key*1031237) & (1<<20) - 1)>>5. Here I also used trick for fast bit operation modulo 2^t: 
for any s: s % (2^t) = s & (1<<t) - 1.

How our HashSet will look and work like:

We create list of empty lists self.arr = [[] for _ in range(1<<15)].
If we want to add(key), then we evaluate hash of this key and then add this key to the place self.arr[t]. However first we need to check if this 
element not it the list. Ideally, if we do not have collisions, length of all self.arr[i] will be 1.
If we want to remove(key) element, we first evaluate it hash, check corresponding list, and if we found element in this list, we remove it from this list.
Similar with contains(key), just check if it is in list.
Complexity: easy question is about space complexity: it is O(2^15), because this is the size of our list. We have a lot of empty places in this list, 
but we still need memory to allocate this list of lists. Time complexity is a bit tricky. If we assume, that probability of collision is small, 
than it will be in average O(1). However it really depends on the size of our self.arr. If it is very big, probability is very small. If it is 
quite tight, it will increase. For example if we choose size 1000000, there will be no collisions at all, but you need a lot of memory. So, there 
will always be trade-off between memory and time complexity.

class MyHashSet: 
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]  
