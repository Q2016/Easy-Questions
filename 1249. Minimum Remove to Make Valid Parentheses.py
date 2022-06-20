Question:
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.







Solution:
  
class Solution:
    def minRemoveToMakeValid(self, s) :
        stack=[]
        split_str=list(s)
        for i in range(len(s)):
            if s[i]=='(':
                # if current char is '(' then push it to stack
                stack.append(i)
            elif s[i]==')':
                # if current char is ')' then pop top of the stack
                if len(stack) !=0:
                    stack.pop()
                else:
                    # if our stack is empty then we can't pop so make  current char as ''
                    split_str[i]=""
        for i in stack:
            split_str[i]=""
        return '' .join(split_str)  
      
Big o:
    n-->size of the s
    Time: O(n)
    Space: O(n)      

      
      
APPROACH 2 ( Better Approach ) ---> O(1) space Interview question


In this approach, we don't need a stack so no extra space will be used. Thanks @Ajna2 for the suggestion of keeping a count variable instead of using a stack.

First, create a count variable for storing the number of opening or closing brackets as per our need.
STEP 1:
Initialize count=0. For this step, we will use count for storing the number of open brackets.
Then, iterate the string s from start and at each iteration:
if open bracket found, then increase count.
if close bracket found, then check if no. of close brackets > no. of open brackets, then mark that character in s by replacing it by #, else decrease the count ( as matching parentheses found ).
int count=0; 
for(int i=0;i<n;++i){
	if(s[i]=='('){ // for open bracket
		++count;
	}
	else if(s[i]==')'){ // for close bracket
		if(count==0){  // if no. of close brackets > no. of open brackets
			s[i]='#';
		}
		else{
			// if matching parentheses found decrease count
			--count;
		}
	}
}
STEP 2 ( Reverse of STEP 1 )
Again, make count=0. For this step, we will use count for storing the number of close brackets.
Then, iterate the string s from the end and at each iteration:
if close bracket found, then increase count.
if open bracket found, then check if no. of open brackets > no. of close brackets, then mark that character in s by replacing it by #, 
else decrease the count ( as matching parentheses found ).
count=0;
for(int i=n-1;i>=0;--i){
	if(s[i]==')'){ // for close bracket
		++count;
	}
	else if(s[i]=='('){ // for open bracket
		if(count==0){ // if no. of open brackets > no. of close brackets
			s[i]='#';
		}
		else{
			// if matching parentheses found decrease count
			--count;
		}
	}
}
STEP 3:
Iterate the string s and append each non - marked character (#) to ans string.

string ans="";
for(int i=0;i<n;++i){
	if(s[i]!='#'){ 
		ans.push_back(s[i]);
	}
return ans;
  
  
  
COMPLETE CODE

class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int n=s.length();
        // Step 1 : Iterate from start
        int count=0; 
        for(int i=0;i<n;++i){
            if(s[i]=='('){ // for open bracket
                ++count;
            }
            else if(s[i]==')'){ // for close bracket
                if(count==0){  // if no. of close brackets > no. of open brackets
                    s[i]='#';
                }
                else{
                    // if matching parentheses found decrease count
                    --count;
                }
            }
        }
        
        // Step 2 : Iterate from end
        count=0;
        for(int i=n-1;i>=0;--i){
            if(s[i]==')'){ // for close bracket
                ++count;
            }
            else if(s[i]=='('){ // for open bracket
                if(count==0){ // if no. of open brackets > no. of close brackets
                    s[i]='#';
                }
                else{
                    // if matching parentheses found decrease count
                    --count;
                }
            }
        }
        
        // Step 3 : Create "ans" by ignoring the special characters '#'
        string ans="";
        for(int i=0;i<n;++i){
            if(s[i]!='#'){ 
                ans.push_back(s[i]);
            }
        }
        return ans;
    }
};
TIME COMPLEXITY
O(n+n+n) = O(n) [ Each step takes O(n) time ]

SPACE COMPLEXITY
O(1) [ No extra space used, ignoring "ans" ]      
