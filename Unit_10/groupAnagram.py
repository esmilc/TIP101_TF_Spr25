'''
Problem 4: Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def group_anagrams(strs):
	pass

Example Usage:

Example #1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Expeced Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example #2:
Input: strs = [""]
Expected Output: [[""]]

Example #3:
Input: strs = ["a"]
Expected Output: [["a"]]
'''

def group_anagrams(strs):
    charsToWords = {}
    rtrnLst = []
    for word in strs:
        sortedChars = [char for char in word]
        sortedChars.sort() #This sorts inplace
        key = tuple(sortedChars) #lists cant be a dictionary key
        charsToWords[key] = charsToWords.get(key, []) + [word]
    
    for lst in charsToWords.values():
        rtrnLst.append(lst)
    return rtrnLst



strs1 = ["eat","tea","tan","ate","nat","bat"]
#Expeced Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs2 = [""]
#Expected Output: [[""]]


strs3 = ["a"]
#Expected Output: [["a"]]

print(group_anagrams(strs1))
print(group_anagrams(strs2))
print(group_anagrams(strs3))