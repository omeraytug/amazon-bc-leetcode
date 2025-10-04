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
        return head