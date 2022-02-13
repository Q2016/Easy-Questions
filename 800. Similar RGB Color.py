Question:
The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.
For example, "#15c" is shorthand for the color "#1155cc".
The similarity between the two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)2 - (CD - WX)2 - (EF - YZ)2.
Given a string color that follows the format "#ABCDEF", return a string represents the color that is most similar to the given color 
and has a shorthand (i.e., it can be represented as some "#XYZ").
Any answer which has the same highest similarity as the best answer will be accepted.

Example 1:
Input: color = "#09f166"
Output: "#11ee66"
Explanation: 
The similarity is -(0x09 - 0x11)2 -(0xf1 - 0xee)2 - (0x66 - 0x66)2 = -64 -9 -0 = -73.
This is the highest among any shorthand color.
Example 2:
Input: color = "#4e3fe1"
Output: "#5544dd"
Constraints:

color.length == 7
color[0] == '#'
color[i] is either digit or character in the range ['a', 'f'] for i > 0.
Explanation
Since we only need to find the closest colors with shorthand, we can list out all shorthand hex codes and find out the closest hex code combination to the given color.

Solution:

class Solution:
    def similarRGB(self, color: str) -> str:

        def get_closest(s):
            return min(['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff'], key=lambda x: abs(int(s, 16) - int(x, 16)))

        results = [get_closest(color[i:i + 2]) for i in range(1, len(color), 2)]

        return '#' + ''.join(results)
        
Time Complexity: O(N).
Space Complexity: O(N).
