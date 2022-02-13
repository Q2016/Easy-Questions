Question:
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.
The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter 
existing in the original uncompressed string.
next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.
Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. 
Please see here for more details.
Example:
StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '



Solution:
# saperate letters from numbers
class StringIterator(object):

    def __init__(self, compressedString):

        self.letters = []
        self.nums = []
        idx = 0
        while idx < len(compressedString):
            if compressedString[idx].isalpha():
                self.letters.append(compressedString[idx])
                idx += 1
            else:
                tmp = ''
                while idx < len(compressedString) and compressedString[idx].isdigit():
                    tmp += compressedString[idx]
                    idx += 1
                self.nums.append(int(tmp))
        self.idx = -1
        self.count = 0
        

    def next(self):
        """
        :rtype: str
        """
        if self.count == 0:
            self.idx += 1
            if self.idx >= len(self.letters):
                return ' '
            self.count = self.nums[self.idx]
        self.count -= 1
        return self.letters[self.idx]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.count == 0:
            self.idx += 1
            if self.idx >= len(self.letters):
                return False
            self.count = self.nums[self.idx]
        return True
