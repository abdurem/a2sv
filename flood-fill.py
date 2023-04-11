class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.oCol = image[sr][sc]
        if self.oCol == color:
            return image
            
        def inbound(i, j):
            return 0 <= i < len(image) and 0 <= j < len(image[0])

        def flood(i, j, d):
            image[i][j] = color

            for dx, dy in d:
                x = dx + i
                y = dy + j

                if inbound(x, y) and image[x][y] == self.oCol:
                    flood(x, y, d)
                    # print(i, j, image, color, self.oCol)

        
        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        flood(sr, sc, direction)

        return image