from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dq_students = deque(students)
        dq_sandwiches = deque(sandwiches)
        cnt = 0

        while True:
            if len(dq_sandwiches) == 0 and len(dq_students) == 0:
                return 0

            if not dq_sandwiches[0] in dq_students:
                return len(dq_students)

            student = dq_students.popleft()

            if dq_sandwiches[0] == student:
                dq_sandwiches.popleft()
            else:
                dq_students.append(student)

