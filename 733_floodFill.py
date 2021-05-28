class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        numRows = len(image)
        numCols = len(image[0])

        if image[sr][sc] == newColor:
            return image
        currColor = image[sr][sc]
        image[sr][sc] = newColor

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for neighbor in neighbors:
            newRow = sr + neighbor[0]
            newCol = sc + neighbor[1]

            if 0 <= newRow < numRows and 0 <= newCol < numCols and image[newRow][newCol] == currColor:
                self.floodFill(image, newRow, newCol, newColor)

        return image
