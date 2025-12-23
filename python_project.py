# student mark analysis

import numpy as np
np.random.seed(40)
marks = np.random.randint(10, 101, size = (20, 5))

avgerage_by_subject = np.mean(marks,axis=0)
average_by_student = np.mean(marks,axis =1)

high = np.max(marks, axis =0)
low = np.min(marks, axis=0)

total_marks = np.sum(marks, axis = 1)
max_highest = np.argmax(total_marks)

pass_fail = marks >= 40

pass_count = np.sum(pass_fail, axis = 0)
difficult_subject = np.argmin(avgerage_by_subject)

ranks = np.argsort(-total_marks)


print("average by subject = ", avgerage_by_subject)
print("average_by_student", average_by_student)

print("highest mark =", high)
print("lowest marks = ", low)

print("total marks =", total_marks ) 
print("total_highest_student =", max_highest, "with marks of = ", total_marks[max_highest])

print(" pass count =", pass_count)

print("difiicult subject is =", difficult_subject, " withb the difiicult subject of", avgerage_by_subject[difficult_subject])

print("first rank of the class", ranks[0])
print("first rank of the class", ranks[:5])