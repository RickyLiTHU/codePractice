class Solution(object):
    def fill(self, image, x, y, newColor):
        l = x == 0 or image[y][x-1] != self.color
        r = x >= len(image[0])-1 or image[y][x+1] != self.color
        u = y == 0 or image[y-1][x] != self.color
        d = y >= len(image)-1 or image[y+1][x] != self.color
        #print(image, x , y, l, r, u, d)
        image[y][x] = newColor
        if l and r and u and d:
            #print("returned", x , y)
            return
        else:
            if not l:
                #print(x , y,"l")
                self.fill(image, x-1, y, newColor)
            if not r:
                #print(x , y,"r")
                self.fill(image, x+1, y, newColor)
            if not u:
                #print(x , y,"u")
                self.fill(image, x, y-1, newColor)
            if not d:
                #print(x , y,"d")
                self.fill(image, x, y+1, newColor)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.color = image[sr][sc]
        if self.color != newColor:
            self.fill(image, sc, sr, newColor)
        return image