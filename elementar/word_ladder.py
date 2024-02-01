import time
from typing import List


# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
# beginWord -> s1 -> s2 -> ... -> sk such that: Every adjacent pair of words differs by a single letter. Every si for
# 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList. sk == endWord Given two words,
# beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation
# sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

# https://leetcode.com/problems/word-ladder/description/?envType=study-plan-v2&envId=top-interview-150

def solution(begin_word: str, end_word: str, words: List[str]) -> List[str]:
    if len(begin_word) != len(end_word) or end_word not in words:
        return list()
    current_word = begin_word
    if get_letter_match(current_word, end_word) is True:
        return [current_word, end_word]

    index = 0
    count = 0
    result_list = []
    while current_word != end_word and index < len(words):
        if get_letter_match(current_word, end_word) is True:
            result_list.append(current_word)
            result_list.append(end_word)
            count += 2
            return result_list
        elif get_letter_match(current_word, words[index]) is True:
            result_list.append(current_word)
            current_word = words[index]
            count += 1
        index += 1
    return result_list


def get_letter_match(current_word, next_word) -> bool:
    lst = [value for value in current_word if value in next_word]
    return len(lst) >= len(current_word) - 1


if __name__ == '__main__':
    start_time = time.time()

    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    data = {"start": "hit", "end": "cog"}
    sol = solution(data['start'], data['end'], word_list)
    print("{} : {} solution is: {}, found: {} words".format(word_list, data, sol, len(sol)))

    word_list = ["hot", "dot", "dog", "lot", "log"]
    data = {"start": "hit", "end": "cog"}
    sol = solution(data['start'], data['end'], word_list)
    print("{} : {} solution is: {}, found: {} words".format(word_list, data, sol, len(sol)))

    word_list = ["hot", "cot", "dot", "dog", "lot", "log"]
    data = {"start": "cat", "end": "dog"}
    sol = solution(data['start'], data['end'], word_list)
    print("{} : {} solution is: {}, found: {} words".format(word_list, data, sol, len(sol)))

    word_list = ["a", "b", "c"]
    data = {"start": "a", "end": "c"}
    sol = solution(data['start'], data['end'], word_list)
    print("{} : {} solution is: {}, found: {} words".format(word_list, data, sol, len(sol)))

    word_list = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
    data = {"start": "leet", "end": "code"}
    sol = solution(data['start'], data['end'], word_list)
    print("{} : {} solution is: {}, found: {} words".format(word_list, data, sol, len(sol)))

    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
