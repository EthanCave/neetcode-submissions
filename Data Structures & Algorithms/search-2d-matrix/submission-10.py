class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Find Row
        l, r = 0, len(matrix) - 1
        comp_mid = lambda l,r: (l+r + 1) // 2
        mid = comp_mid(l,r)
        print(l,r,mid)
        while l < r:
            if target < matrix[mid][0]:
                r = mid - 1
                mid = comp_mid(l,r)
            if target >= matrix[mid][0]:
                l = mid
                mid = comp_mid(l,r)
        
        #Search Row
        row = l
        print(f"row: {row}")
        l, r = 0, len(matrix[row]) - 1
    
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

        
            
                