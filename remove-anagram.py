'''
You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.
Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".
'''
import collections

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
      ''' Find Resultant Array After Removing Anagram.
        @param {string[]} words 
      '''
        res=  [words[0]]
        for index, _ in enumerate(words[1:],1):
            if not collections.Counter(words[index]) == collections.Counter(words[index-1]):
                res.append(words[index])
        return res

  #     without 'collections' module. 
  #
  #     w= sorted(list(words[index]))
  #     x= sorted(list(words[index-1]))
  #     b = all([(w.count(item)==x.count(item) and len(w)==len(x)) for item in w])
  #     if not b:
  #         res.append(words[index])
  #     return res
