class Solution:
    def isPalindrome(self, s):
        filtered_str=''.join(char.lower() for char in s if char.isalnum())
        rev_str=filtered_str[::-1]
        return filtered_str==rev_str
        
words="A man, a plan, a canal: Panama"
# This is 0P(zero and P)
words1='0P'
words3="race a car"
solution=Solution()
if solution.isPalindrome(words):
    print(True)
else:
    print(False)