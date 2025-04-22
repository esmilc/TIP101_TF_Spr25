'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

def gcd_of_stings(str1, str2):
	pass


Example #1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example #2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example #3:
Input: st1 = "LEET", str2 = "CODE"
Output: ""


'''

def gcdOfStrings( str1: str, str2: str) -> str:
    stringToReturn = ""
    shortestLen = min(len(str1), len(str2))

    str1Len = len(str1)
    str2Len = len(str2)

    def isDivisor(index : int) -> bool:
        mult1, mult2 = str1Len // (index) , str2Len // (index) #In reality you dont have to floor divide
        return (str1[:index] * mult1 == str1) and (str1[:index] * mult2 == str2)

    
    for pos in range(shortestLen, 0, -1):
        if ((str1Len % pos) == 0) and ((str2Len % pos) == 0): #The substr must be cleanly divisible
            if isDivisor(pos):
                return str1[:pos]

    
    return stringToReturn