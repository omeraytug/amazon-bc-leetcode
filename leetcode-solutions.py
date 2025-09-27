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
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list [int]:
        d = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in d:
                return [d[y], i]
            d[x] = i