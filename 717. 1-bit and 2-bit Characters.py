Question:
We have two special characters:
The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

Example 1:
Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

Solution:

    if not bits: return False
    n = len(bits)
    
    index = 0
    while index < n:
        if index == n-1 : return True
        if bits[index] == 1: 
            index += 2              
        else: index += 1
    return False
