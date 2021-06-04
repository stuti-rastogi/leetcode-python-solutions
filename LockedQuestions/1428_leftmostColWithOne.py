# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """

class BinaryMatrix(object):
   def get(self, row: int, col: int) -> int:
       pass
   def dimensions(self) -> list:
       pass

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        row = 0
        col = cols-1
        
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                col -= 1
            else:
                row += 1
                
        return col+1 if col != cols-1 else -1


    # def binarySearch(self, binaryMatrix, row, low, high):
    #     while low < high:
    #         mid = (low + high) // 2
    #         midElement = binaryMatrix.get(row, mid)
    #         if midElement == 0:
    #             low = mid + 1
    #         else:
    #             high = mid
    #     return low


    # def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    #     rows, cols = binaryMatrix.dimensions()

    #     minCol = cols
    #     for row in range(rows):
    #         candidateCol = self.binarySearch(binaryMatrix, row, 0, cols-1)
    #         if binaryMatrix.get(row, candidateCol) == 1:
    #             minCol = min(minCol, candidateCol)

    #     return -1 if minCol == cols else minCol