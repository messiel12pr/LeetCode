'''

    1700. Number of Students Unable to Eat Lunch

'''

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n_ones = sum(students)
        n_zeroes = len(students) - n_ones

        while students and sandwiches:
            if n_ones == len(students) and sandwiches[0] == 0 or \
               n_zeroes == len(students) and sandwiches[0] == 1:
                break

            if students[0] == sandwiches[0]:
                if students[0] == 1:
                    n_ones -= 1

                else:
                    n_zeroes -= 1

                students.pop(0)
                sandwiches.pop(0)

            else:
                students.append(students.pop(0))

        return len(students)
