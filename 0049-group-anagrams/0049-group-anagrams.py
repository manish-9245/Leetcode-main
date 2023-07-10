class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        anagrams = {}
        for word in strs:
            key = 1
            for char in word:
                key *= primes[ord(char) - ord('a')]
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())