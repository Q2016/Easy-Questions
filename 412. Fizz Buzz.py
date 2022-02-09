Question:
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]

Solution:
This approach is an optimization over approach 2. When the number of mappings are limited, approach 2 looks good. But what if 
you face a tricky interviewer and he decides to add too many mappings?
Having a condition for every mapping is not feasible or may be we can say the code might get ugly and tough to maintain.
What if tomorrow we have to change a mapping or may be delete a mapping? Are we going to change the code every time we have a modification in the mappings?
We don't have to. We can put all these mappings in a Hash Table.
  
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
