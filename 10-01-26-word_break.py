from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        state = [False for i in range(len(s) + 1)]
        state[0] = True

        # "neetcode"
        #  0123 4567
        #  1234 5678
        #  i = 3
        # neet -> len = 4
        # 3 - 4 + 1 = 0
        # s[0:4] -> 0 to 3
        for i in range(len(s)):  # 0 indexed
            for word in wordDict:
                # match the word
                word_length = len(word)

                if i - word_length + 1 >= 0 and s[i - word_length + 1 : i + 1] == word:
                    if state[i - word_length + 1]:
                        state[i + 1] = True  # keep track of 1 indexed value

        return state[-1]
