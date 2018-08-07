class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                while asteroid < 0 and stack and stack[-1] > 0:
                    if stack[-1] > abs(asteroid):
                        asteroid = 0
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        asteroid = 0
                    else:stack.pop();
                if asteroid:stack.append(asteroid)
            else:
                stack.append(asteroid)
        return stack