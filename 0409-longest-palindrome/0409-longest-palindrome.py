class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        length_of_palindrome = 0
        odd_count_found = False
        
        for count in char_count.values():
            if count % 2 == 0:
                length_of_palindrome += count
            else:
                length_of_palindrome += count - 1
                odd_count_found = True
        
        if odd_count_found:
            length_of_palindrome += 1
        
        return length_of_palindrome