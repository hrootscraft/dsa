#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
from typing import List
from collections import deque, defaultdict
# @lc code=start
class Solution:
    ## approach 2: Memory Limit Exceeded
    def is_difference_one(self, word1, word2):
        different_chars = 0
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                different_chars +=1 
        return different_chars == 1

    def build_graph(self, wordList): # build the graph with edges between words that differ by one character
        l = len(wordList)
        graph = defaultdict(lambda: set()) # creates a new empty set for each key individually

        # defaultdict(set()) would create a single set object as the default value for all keys. 
        # That means, every key in the graph dictionary would point to the same set object. 
        # As a consequence, when you modify one key's set, you would also be modifying the sets 
        # of all other keys because they all reference the same object.

        for i in range(l):
            for j in range(i+1, l):
                word1 = wordList[i]
                word2 = wordList[j]
                if self.is_difference_one(word1, word2):
                    graph[word1].add(word2)
                    graph[word2].add(word1)
        return graph

    # perform a bfs on the constructed graph to find shortest transformation sequences from beginWord to endWord
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)        
        graph = self.build_graph(wordList)
                    
        q = deque([(beginWord, [])]) # initialize the queue with beginWord and an empty current_sequence
        visited = set()
        ans = defaultdict(lambda: [])

        while q:
            curr_word, curr_sequence = q.popleft()
            curr_sequence.append(curr_word)
            visited.add(curr_word)

            if curr_word == endWord:
                ans[len(curr_sequence)].append(curr_sequence[::])
                continue

            for neighbor in graph[curr_word]:
                if neighbor not in visited:
                    q.append((neighbor, curr_sequence[::]))
        
        if not ans: return []
        return ans[min(ans)]

        # approach 1: Time Limit Exceeded
        # # bfs: here we store the subsequence at each level that potentially leads to target
        # # and we do not mark the word from the wordList until that level is completed unlike in prob # 127
        # # where once we get that word in the path we remove it from wordList because we only have to return the level #
        # # but here we're supposed to return all the subsequences in that level that get to the target
        # if endWord not in wordList: return []

        # word_set = set(wordList)
        # q = deque([[beginWord]]) # on level 0 we only have one element in the list that starts with beginWord
        # words_used_on_level = defaultdict(list) # initialize a defaultdict to store words at each level
        # words_used_on_level[0] = [beginWord] # at level 0 we only have a single element list that starts with beginWord
        # level = 0 
        # ans = []

        # while q:
        #     curr_sequence = q.popleft()

        #     # entire level from the queue has to be explored and only then you delete the words used on that level from word_set
        #     # update level and remove words used in previous levels
        #     if len(curr_sequence) > level:
        #         level += 1
        #         for word in words_used_on_level[level]:
        #             word_set.discard(word)
        #         del words_used_on_level[level]

        #     last_word_in_curr_seq = curr_sequence[-1]

        #     if last_word_in_curr_seq == endWord:
        #         # ensure that only sequences that match the length of the shortest sequence 
        #         # to reach the target word are added to the ans list
        #         if not ans or len(ans[0]) == len(curr_sequence): 
        #             ans.append(curr_sequence)

        #     # generate new words by replacing each character
        #     for i in range(len(last_word_in_curr_seq)):
        #         for letter in "abcdefghijklmnopqrstuvwxyz":
        #             next_word = last_word_in_curr_seq[:i]+letter+last_word_in_curr_seq[i+1:]
        #             if next_word in word_set:
        #                 q.append(curr_sequence+[next_word])
        #                 words_used_on_level[level+1].append(next_word) 
        
        # return ans



# Amazon, Box, Facebook, Google, LinkedIn, Lyft, Microsoft, Oracle, Pinterest, Uber, Yahoo, Yelp 
# @lc code=end
