Question:
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). 
Each LED represents a zero or one, with the least significant bit on the right. For example, the below binary watch reads "4:51".
Given an integer turnedOn which represents the number of LEDs that are currently on, return all possible times the watch could represent. 
You may return the answer in any order. The hour must not contain a leading zero. For example, "01:00" is not valid. It should be "1:00".
The minute must be consist of two digits and may contain a leading zero. For example, "10:2" is not valid. It should be "10:02".
 
Example 1:
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Solution:
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        binary=["8h","4h","2h","1h","32m","16m","8m","4m","2m","1m"]
        
        # function to generate all the sub lists
        def sub_lists (l):
            lists = [[]]
            for i in range(len(l) + 1):
                for j in range(i):
                    lists.append(l[j: i])
            return lists
        
        tmp=sub_lists(binary)
        #print(tmp)
        res=[]
        for l in tmp:
            res_m=[]
            res_h=[]
            if len(l)==turnedOn:
                for i in l:
                    if i[:-1]=="m":
                        res_m.append(int(i[:len(i)-1]))
                    else:
                        res_h.append(int(i[:len(i)-1]))
            
            H=str(sum(res_h))
            M=str(sum(res_m))
            print(H,M)
            
            if H=="0":
                H="00" 
                
            if M=="0":
                M="00"
            
            res.append(H+":"+M)
                
            for i in res:
                if(i == "00:00"):
                    res.remove(i)
    
    
        return res
