from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q1 = deque(students)
        q2 = deque(sandwiches)

        consecutive_mismatches = 0

        while q1 and consecutive_mismatches < len(q1) :
            if q1[0] == q2[0]:
                q1.popleft()
                q2.popleft()
                consecutive_mismatches = 0
            else:
                a = q1.popleft()
                q1.append(a)
                consecutive_mismatches += 1

        return len(q1)
        