from collections import namedtuple

N = int(input())
categories_list = ",".join(input().split())

Students = namedtuple('Student', categories_list)
total_marks = 0
for _ in range(N):
    student_info_list = input().split()
    temp_student = Students(*student_info_list)
    total_marks += int(temp_student.MARKS)

final_result = "%.2f" % (total_marks / N )
print(final_result)

