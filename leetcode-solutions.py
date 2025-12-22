#3110
word = "hello"
score = 0
for i in range(len(word) - 1):
	score += abs(ord(word[i]) - ord(word[i + 1]))
print(score)



#1119
def remove_vowels(s):
    res: ""
    vowels = "aeiou"
    for i in s:
        if i not in vowels:
            result += i

    return result

def remove.vowels(s): 
  return "".join(a for a in s if a not in"aeiou")


#1 two sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list [int]:
        d = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in d:
                return [d[y], i]
            d[x] = i



#9 Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s [::-1]

print(Solution().isPalindrome(1551))


#13 Roman to Integer
class Solution:
    def romanToInt(self, s: str)-> int:
        roman = {"I": 1, "V": 5, "X": 10, "L":
                 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res


#14 longest common prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = "" 

        for i in range(len(strs[0])): #iterate over the characters of the first string
            for s in strs: #compare with all other strings
                if i == len(s) or s[i] != strs[0][i]: #if out of range or mismatch 
                    return res
            res += strs[0][i] #if match, append
        return res
                


#20 Valid Parentheses
class Solution:
    def validParanthesis(self, s:str ) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                


#21 merge two sorted lists
#two lists that have integers will be merged where the final list should be in order
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy


#58 length of last word
def lastWord(s):
	return len(s.split()[-1])




#69 Sqrt(x)



#70 Climbing Stairs
class Solution:
    def climbStairs(self, n):
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
    

#83 Remove duplicate from Sorted List
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return heady
    



# 125 Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))


# 268 Missing Number
class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return i
        return len(nums)



# 434 Number of Segments in a String
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
    

class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        in_word = False

        for ch in s:
            if ch != ' ':
                if not in_word:
                    count += 1
                    in_word = True
            else:
                in_word = False

        return count

# 485 Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0 # the longest streak we have seen overall
        current = 0 # how many 1s we have counted consecutively right now

        for x in nums:
            if x == 1:
                current += 1
                if current > maximum:
                    maximum = current
            else:
                current = 0

        return maximum
    


# 504 Base 7

# 100 / 7 = 14 % 2
# 14 / 7 = 2  % 0
# 2 / 7 = 0 % 2
# base 7 - 202 (210)
# 2x7² + 0x7¹ + 2x7⁰  
# 98 + 0 + 2 

# base representation of base 7 goes upwards

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        original_num = num # add after
        num = abs(num) # add after
        remainders = []

        while num > 0:
            remainder = num % 7
            remainders.append(str(remainder))
            num //= 7
    
        if original_num < 0: # add after
            remainders.append('-') # add after
        remainders.reverse()
        return ''.join(remainders)
    


# 575 Distribute Candies
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)
    


# 657 Robot Return to Origin
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        
        return x == 0 and y == 0


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and \
               moves.count('L') == moves.count('R')
