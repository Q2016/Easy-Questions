Question:
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Solution:Two pass
If we know the number of elements which would be discarded from the end of the array, we can copy the rest. How do we find out how many 
elements would be discarded in the end? The number would be equal to the number of extra zeros which would be added to the array. The extra 
zero would create space for itself by pushing out an element from the end of the array.
Once we know how many elements from the original array would be part of the final array, we can just start copying from the end. Copying from 
the end ensures we don't lose any element since, the last few extraneous elements can be overwritten.

Find the number of zeros which would be duplicated. Let's call it possible_dups. We do need to make sure we are not counting the zeros which would 
be trimmed off. Since, the discarded zeros won't be part of the final array. The count of possible_dups would give us the number of elements to be 
trimmed off the original array. Hence at any point, length_ - possible_dups is the number of elements which would be included in the final array.
Note: In the diagram above we just show source and destination array for understanding purpose. We will be doing these operations only on one array.
Handle the edge case for a zero present on the boundary of the leftover elements.
Let's talk about the edge case of this problem. We need to be extra careful when we are duplicating the zeros in the leftover array. This care should 
be taken for the zero which is lying on the boundary. Since, this zero might be counted as with possible duplicates, or may be just got included in the 
left over when there was no space left to accommodate its duplicate. If it is part of the possible_dups we would want to duplicate it otherwise we don't.
An example of the edge case is - [8,4,5,0,0,0,0,7]. In this array there is space to accommodate the duplicates of first and second occurrences of zero. 
But we don't have enough space for the duplicate of the third occurrence of zero. Hence when we are copying we need to make sure for the third occurrence 
we don't copy twice. Result = [8,4,5,0,0,0,0,0]
Iterate the array from the end and copy a non-zero element once and zero element twice. When we say we discard the extraneous elements, it simply means we 
start from the left of the extraneous elements and start overwriting them with new values, eventually right shifting the left over elements and creating 
space for all the duplicated elements in the array.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included  
                if left == length_ - possible_dups:
                    arr[length_] = 0 # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
