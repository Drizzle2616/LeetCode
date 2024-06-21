class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        # Initialize the first row
        row = [1] * (rowIndex + 1)
        
        # Compute the values for each row
        for i in range(1, rowIndex + 1):
            # Update the row in reverse order to ensure we use only O(rowIndex) space
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        
        return row

# Example usage:
solution = Solution()
print(solution.getRow(3))  # Output: [1, 3, 3, 1]
print(solution.getRow(0))  # Output: [1]
print(solution.getRow(1))  # Output: [1, 1]
