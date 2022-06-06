Question:
We use three bit-representations to represent three characters : 0, 10, 11 (the corresponding characters don't matter)
So bits representation 1, 01 are not valid. Given an array of bits ending with 0, find out if it's only valid to translate the last 0 into 
the 0 bit representation (means it's not valid when the last 0 is translated into the 10 bits representation)

Example 1:
Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:
Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

                          
                          
                          
                          
                          
                          
                          
                          
                          
                          

Solution:
                          
if we iterate through from left->right
      for each of the bit 'b' at index 'i'
             if 'b' is equal to 1
                  it must be 2 bits
                        then we can move to index 'i+2'
             else 'b' is equal to 0
                 it must be 1 bit
                      then we can move to index 'i+1'
      After performing the iteration
           if our last index is at the end of the array
                  Then it must be a 1 bit (0)
                          
                          
                          
# (Time, Space) Complexity : O(n), O(1)

    def isOneBitCharacter(self, bits: List[int]) -> bool:
           if not bits: return False
            n = len(bits)

            index = 0
            while index < n:
                if index == n-1 : return True
                if bits[index] == 1: 
                    index += 2              
                else: index += 1
            return False
