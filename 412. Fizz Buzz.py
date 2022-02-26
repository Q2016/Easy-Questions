Question:
Given an integer n, return a string array answer for 0=< i =<n where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

 
Solution: Hashing: using key
We can put all these mappings in a Hash Table.
  
  class Solution:
    def fizzBuzz(self, n):
        # ans list
        ans = []
        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}
        for num in range(1,n+1):
            num_ans_str = ""
            for key in fizz_buzz_dict.keys():
                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]
            if not num_ans_str:
                num_ans_str = str(num)
