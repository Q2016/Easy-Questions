Question:
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 











Solution: Character Processing in One-Pass

We replace all the punctuations with spaces and at the same time convert each letter to its lowercase. 
One could also accomplish this in two stages. Here we merge them together in one stage.

We split the output in the above step into words, with the separator of spaces.

We then iterate through the words to count the appearance of each unique word, excluding the words from the banned list.

With the hashmap of {word->count}, we then walk through all the items to find the word with the highest frequency.    

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1). replace the punctuations with spaces,
        #      and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        #2). split the string into words
        words = normalized_str.split()

        word_count = defaultdict(int)
        banned_words = set(banned)

        #3). count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        #4). return the word with the highest frequency
        return max(word_count.items(), key=operator.itemgetter(1))[0]
    
    
Complexity Analysis

Let N be the number of characters in the input string and M be the number of characters in the banned list.

Time Complexity: O(N+M).

It would take O(N) time to process each stage of the pipeline as we built.

In addition, we built a set out of the list of banned words, which would take O(M) time.

Hence, the overall time complexity of the algorithm is O(N+M).

Space Complexity: O(N+M).

We built a hashmap to count the frequency of each unique word, whose space would be of O(N).

Similarly, we built a set out of the banned word list, which would consume additional O(M) space.

Therefore, the overall space complexity of the algorithm is O(N+M).    
