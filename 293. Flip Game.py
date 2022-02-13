Question:
You are playing a Flip Game with your friend.
You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". 
The game ends when a person can no longer make a move, and therefore the other person will be the winner.
Return all possible states of the string currentState after one valid move. You may return the answer in any order. If there is no valid move, 
return an empty list [].

Example 1:

Input: currentState = "++++"
Output: ["--++","+--+","++--"]
Example 2:

Input: currentState = "+"
Output: []
Constraints:

1 <= currentState.length <= 500
currentState[i] is either '+' or '-'.
Explanation
Iterate the string and whenever we see “++”, we can replace it with “–” and record the flipped strings.

Solution:

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        results = []

        for i in range(0, len(currentState) - 1):
            sub = currentState[i:i+2]            

            if sub == "++":
                flip = currentState[:i] + "--" + currentState[i+2:]
                results.append(flip)


        return results
        
        
Time Complexity: O(N).
Space Complexity: O(N).
