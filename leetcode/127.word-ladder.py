#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
from collections import deque
import string
from typing import List

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # brute force bfs: for every letter in beginWord, replace it with a-z and check if it exists in wordList
        # if it does, then add it to the queue with it's level number. explore the word in the queue; 
        # if & when you encounter endWord return level else return 0
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        q = deque([(beginWord, 1)])

        while q:
            curr_word, level = q.popleft()
            if curr_word == endWord: return level

            for i in range(len(curr_word)):
                # for letter in string.ascii_lowercase:
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    next_word = curr_word[:i] + letter + curr_word[i+1:]
                    if next_word in wordSet and next_word != curr_word:
                        wordSet.remove(next_word) # mark it as visisted by removing from word set
                        q.append((next_word, level + 1))
        return 0 # no transformation sequence found
# @lc code=end

# TC: N * len(curr_word) * 26 ... N->len(wordList)
# SC: stored in a set so O(N)

# Affirm, Airbnb, Amazon, Apple, Audible, Bloomberg, Cohesity, Expedia, 
# Facebook, Google, LinkedIn, Lyft, Microsoft, Oracle, Qualtrics, Salesforce, 
# Samsung, Snapchat, Square, Tesla, Uber, Walmart Labs, Yelp, Zillow
