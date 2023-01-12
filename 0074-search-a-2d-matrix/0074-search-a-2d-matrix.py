class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low = 0
        high = len(matrix) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            if matrix[mid][-1] < target:
                low = mid + 1
            elif matrix[mid][-1] > target:
                high = mid - 1
            else:
                break
                
        if matrix[mid][-1] < target:
            mid+=1
        if mid == len(matrix):
            return False
        row=matrix[mid]
        print(row)  
        low = 0
        high = len(row) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2
            if row[mid] < target:
                low = mid + 1
            elif row[mid] > target:
                high = mid - 1
            else:
                return True
        return False