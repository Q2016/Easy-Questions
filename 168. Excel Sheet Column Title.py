Question:
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...




Solution:
    def convertToTitle(self, columnNumber: int) -> str:       
        values=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        dic={}
        for i in range(len(values)):
            dic[i]=values[i]
        myint=columnNumber
        if myint<=26:
            return dic[myint-1]
        m=[]
        r=[]
        while myint>26:
            tmp=myint//26
            m.append(tmp) # mod
            tmp=myint%26
            r.append(tmp) # remain
            myint=myint//26
        s = zip(reversed(m), reversed(r))
        mystring=""
        for m_,r_ in list(s):
            mystring=mystring+dic[m_-1]+dic[r_-1]

        return mystring
