Question:
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

  
  
  
  
  
  
  
  
  
Solution:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs==[""]:
            return ""

        if len(strs)==1:
            return strs[0]
        
        cnt_list=[]

        for i,_ in enumerate(strs):
            cnt=0
            if i<len(strs)-1:
                for z1, z2 in zip(strs[i],strs[i+1]):
                    if z1==z2:
                        cnt+=1
                cnt_list.append(strs[i][:cnt])

        return min(cnt_list)
