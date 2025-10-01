# #3110
# word = "hello"
# score = 0
# for i in range(len(word) - 1):
# 	score += abs(ord(word[i]) - ord(word[i + 1]))
# print(score)



# 1119
# def remove_vowels(s):
#     res: ""
#     vowels = "aeiou"
#     for i in s:
#         if i not in vowels:
#             result += i

#     return result

#def remove.vowels(s): 
#   return "".join(a for a in s if a not in"aeiou")


#1 two sum
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list [int]:
#         d = {}
#         for i, x in enumerate(nums):
#             y = target - x
#             if y in d:
#                 return [d[y], i]
#             d[x] = i



#9 Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)
#         return s == s [::-1]

# print(Solution().isPalindrome(1551))


#13 Roman to Integer
# class Solution:
#     def romanToInt(self, s: str)-> int:
#         roman = {"I": 1, "V": 5, "X": 10, "L":
#                  50, "C": 100, "D": 500, "M": 1000}
#         res = 0
#         for i in range(len(s)):
#             if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
#                 res -= roman[s[i]]
#             else:
#                 res += roman[s[i]]
#         return res


#14 longest common prefix



