class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        #list to store chars of merged strings
        merged = []

        #zip the two strings together. effectively making as many pairs as there are characters in the smallest string
        for charOne, charTwo in zip(word1, word2):
            merged.append(charOne + charTwo)

        #handle both cases when either string is larger than the other
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        #convert list to string and return
        return "".join(merged)
            