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
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Solution: Character Processing in One-Pass
With the approach of String manipulation pipeline, it is clear and easy to debug, since we could locate and inspect each stage 
if anything goes wrong. However, one might argue that it is probably not the most efficient way to solve the problem, since we 
scan the input string multiple times.
Indeed, it is possible to process the input string once and only once to accomplish the tasks.
We could iterate through the string character by character, and do the processing on-the-fly, rather than delaying the processing 
to the latter stages of the pipeline. The idea is that we consume the input string on the character base. At the moment we reach 
the end of one word, we can then start to perform the word-based logics such as checking if the word is in the banned list, 
updating the frequency of the word and also updating the most frequent word we've seen so far etc.
We could implement the algorithm in one single loop, over the characters of the input string.
At each iteration, the character is either of letter (maybe digit), or punctuation or space in other cases.
character pointers
Further more, we could divide it into the following two cases:
Case (1): we are in the middle of a word.
Case (2): we in in-between the words, e.g. punctuations between the words or at the end of the paragraph.
We then can organize the logics into the above two cases.
In case (1), we simply append the character into the word buffer.
In case (2), we do the rest of the logics, as follows:
check if the word is enlisted in the banned list.
if not, update the frequency of the word.
update the most common word that we've seen so far.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        banned_words = set(banned)
        ans = ""
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []

        for p, char in enumerate(paragraph):
            #1). consume the characters in a word
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph)-1:
                    continue

            #2). at the end of one word or at the end of paragraph
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned_words:
                    word_count[word] +=1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
                # reset the buffer for the next word
                word_buffer = []

        return ans
