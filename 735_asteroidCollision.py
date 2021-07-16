class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []

        stack = []
        for asteroid in asteroids:
            breakOut = None
            while stack and asteroid < 0 < stack[-1]:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    breakOut = True
                    break
                else:
                    breakOut = True
                    break
            if not breakOut:
                stack.append(asteroid)
        return stack
