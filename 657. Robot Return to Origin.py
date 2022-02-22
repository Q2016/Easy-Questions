Question:
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot 
ends up at (0, 0) after it completes its moves. You are given a string moves that represents the move sequence of the robot 
where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).


Example 1:
Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin 
where it started. Therefore, we return true.


Solution: Simulation
We can simulate the position of the robot after each command. Initially, the robot is at (x, y) = (0, 0). If the move is 'U', 
the robot goes to (x, y-1); if the move is 'R', the robot goes to (x, y) = (x+1, y), and so on.

class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0
