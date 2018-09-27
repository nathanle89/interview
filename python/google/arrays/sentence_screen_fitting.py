"""
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 <= rows, cols <= 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
"""

class Solution(object):
    # Timeout solution
    # def wordsTyping(self, sentence, rows, cols):
    #     """
    #     :type sentence: List[str]
    #     :type rows: int
    #     :type cols: int
    #     :rtype: int
    #     """
    #     row_index = 0
    #     col_index = 0
    #     total_sentence_counter = 0
    #     sentence_index = 0
    #     while row_index < rows:
    #         current_word_len = len(sentence[sentence_index])
    #         if cols - col_index >= current_word_len:
    #             col_index += current_word_len
    #
    #             # Add a space
    #             if cols - col_index > 0:
    #                 col_index += 1
    #
    #             sentence_index += 1
    #
    #             if sentence_index == len(sentence):
    #                 sentence_index = 0
    #                 total_sentence_counter += 1
    #         else:
    #             # Current word does not fit so we start on the next line
    #             row_index += 1
    #             col_index = 0
    #
    #     return total_sentence_counter

    def wordsTyping(self, sentence, rows, cols):
        length_of_sentence = 0

        for word in sentence:
            length_of_sentence += len(word) + 1 # Length of word and space

        row_index = 0
        total_sentence_count = 0
        current_word_index = 0
        while row_index < rows:
            remaining_spot = cols % length_of_sentence
            total_sentence_count += cols / length_of_sentence

            while remaining_spot >= len(sentence[current_word_index]):
                remaining_spot -= len(sentence[current_word_index]) + 1
                current_word_index += 1

                if current_word_index == len(sentence):
                    current_word_index = 0
                    total_sentence_count += 1

            # At this point I'm done with one line
            row_index += 1

            # if the sentence fits perfectly into one row then we can skip forward
            # Imagine the sentence fits into one line with some remaining spaces
            # We continue fitting words into it. At one point we create a block that perfectly fit N number of sentences
            # At that point all we need to do is multiply X number of time to get the total count
            if current_word_index == 0:
                total_sentence_count = (rows / row_index) * total_sentence_count
                row_index = (rows / row_index) * row_index

        return total_sentence_count



rows = 3
cols = 6
sentence = ["a", "bcd", "e"]

solution = Solution()

print solution.wordsTyping(sentence, rows, cols)

rows = 2
cols = 8
sentence = ["hello", "world"]
print solution.wordsTyping(sentence, rows, cols)

rows = 4
cols = 5
sentence = ["I", "had", "apple", "pie"]
print solution.wordsTyping(sentence, rows, cols)