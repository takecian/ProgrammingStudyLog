import bisect


class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.students = []

    def seat(self) -> int:
        if len(self.students) == 0:
            self.students.append(0)
            return 0
        else:
            distance = self.students[0]
            position = 0
            for i in range(1, len(self.students)):
                d = self.students[i] - self.students[i - 1]
                d //= 2
                if d > distance:
                    distance = d
                    position = d + self.students[i - 1]

            if self.N - 1 - self.students[-1] > distance:
                position = self.N - 1
            bisect.insort(self.students, position)
            print(position)
            return position

    def leave(self, p: int) -> None:
        self.students.remove(p)
