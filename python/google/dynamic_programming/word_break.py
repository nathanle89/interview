"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, dict, memo):
        if s in dict:
            return True

        if s in memo:
            return memo[s]

        result = False
        for i in range(1, len(s)):
            current_word = s[0:i]
            if current_word in dict:
                tmp = self.helper(s[i:], dict, memo)
                memo[s[i:]] = tmp
                result = result or tmp

        return result

solution = Solution()

print solution.wordBreak("leetcode", ["leet", "code"])
print solution.wordBreak("applepenapple", ["apple", "pen"])
print solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])

