class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize pointers for a and b
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        # Traverse both strings from end to start
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # Append the current bit result to the result list
            result.append(str(total % 2))
            # Calculate the new carry
            carry = total // 2
        
        # The result is built in reverse order, reverse it to get the final result
        return ''.join(reversed(result))

# Example usage:
solution = Solution()

# Test case 1
a = "11"
b = "1"
print(solution.addBinary(a, b))  # Output: "100"

# Test case 2
a = "1010"
b = "1011"
print(solution.addBinary(a, b))  # Output: "10101"
