Question:
Given a callable function f(x, y) with a hidden formula and a value z, reverse engineer the formula and return all positive 
integer pairs x and y where f(x,y) == z. You may return the pairs in any order.
While the exact formula is hidden, the function is monotonically increasing, i.e.:
f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
The function interface is defined like this:
interface CustomFunction {
public:
  // Returns some positive integer f(x, y) for two positive integers x and y based on a formula.
  int f(int x, int y);
};
We will judge your solution as follows:
The judge has a list of 9 hidden implementations of CustomFunction, along with a way to generate an answer key of all valid pairs for a specific z.
The judge will receive two inputs: a function_id (to determine which implementation to test your code with), and the target z.
The judge will call your findSolution and compare your results with the answer key.
If your results match the answer key, your solution will be Accepted.


Example 1:
Input: function_id = 1, z = 5
Output: [[1,4],[2,3],[3,2],[4,1]]
Explanation: The hidden formula for function_id = 1 is f(x, y) = x + y.
The following positive integer values of x and y make f(x, y) equal to 5:
x=1, y=4 -> f(1, 4) = 1 + 4 = 5.
x=2, y=3 -> f(2, 3) = 2 + 3 = 5.
x=3, y=2 -> f(3, 2) = 3 + 2 = 5.
x=4, y=1 -> f(4, 1) = 4 + 1 = 5.


Solution:
Time: O(x + y), space: O(1) excluding return list.

    public List<List<Integer>> findSolution(CustomFunction customFunction, int z) {
        List<List<Integer>> ans = new ArrayList<>();
        int x = 1, y = 1000;
        while (x < 1001 && y > 0) {
            int val = customFunction.f(x, y);
            if (val < z) { 
                ++x; 
            }else if (val > z) { 
                --y; 
            }else {
                ans.add(Arrays.asList(x++, y--));
            }
        }
        return ans;
    }
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x, y, ans = 1, 1000, []
        while x < 1001 and y > 0:
            val = customfunction.f(x, y)
            if val > z:
                y -= 1
            elif val < z:
                x += 1
            else:
                ans += [[x, y]]
                x += 1
                y -= 1
        return ans
Method 2: Binary Search
Time: O((xlogy), space: O(1) excluding return list.

    public List<List<Integer>> findSolution(CustomFunction customFunction, int z) {
        List<List<Integer>> ans = new ArrayList<>();
        for (int x = 1; x < 1001; ++x) {
            int l = 1, r = 1001;
            while (l < r) {
                int y = (l + r) / 2;
                if (customFunction.f(x, y) < z) {
                    l = y + 1;
                }else {
                    r = y;
                }
            }
            if (customFunction.f(x, l) == z) {
                ans.add(Arrays.asList(x, l));
            }
        }
        return ans;
    }
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1, 1001):
            l, r = 1, 1001
            while l < r:
                y = (l + r) // 2
                if customfunction.f(x, y) < z:
                    l = y + 1;
                else:
                    r = y
            if  customfunction.f(x, l) == z:
                ans += [[x, l]]
        return ans
