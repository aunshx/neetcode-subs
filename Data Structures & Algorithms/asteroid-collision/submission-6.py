class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue 

            while stack and stack[-1] > 0 and stack[-1] < -a:
                stack.pop()

            if stack and stack[-1] == -a:
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(a)

        return stack