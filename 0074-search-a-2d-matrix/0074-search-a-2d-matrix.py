class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary Search
        nr, nc = len(matrix), len(matrix[0])
        length = nr * nc

        def val(index: int):
            """
            Given an integer index which serves as the index of a value in the 
            matrx (assuming we took the entire matrix as on array), return the element
            at that index.

            Example:
            1   3   5   7
            19  11  16  60

            The above grid is equivalent to
            1 3 5 7 19 11 16 60

            And thus we can consider that as an array of non-decreasing integers

            val(0) -> 1
            val(3) -> 7
            val(6) -> 16
            """
            return matrix[math.floor(index / nc)][index % nc]

        def bin_search(n: int) -> bool:
            """
            Given an integer n, return true if it's in the matrix, else false
            """
            l, r = 0, length - 1
            while l <= r:
                mid = (l + r) // 2
                if val(mid) == n: return True
                if val(mid) > n:
                    r = mid - 1
                else:
                    l = mid + 1
                
            return False

        return bin_search(target)