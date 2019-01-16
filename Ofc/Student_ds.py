

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_no_of_marks(self):
        return len(self.marks)
    def get_total_sum(self):
        return sum(self.marks)
    def max_mark(self):
        return max(self.marks)
    def min_mark(self):
        return min(self.marks)
    def avg(self):
        return sum(self.marks)/len(self.marks)
    def add_new_mark(self,new_mark):
        self.marks.append(new_mark)
        return self.marks
    def remove_marks_at(self,index):
        del self.marks[index]



student=Student('Suv',[59,78,96,98])
no=student.get_no_of_marks()
print(no)
total=student.get_total_sum()
print(total)
highest_marks=student.max_mark()
print(highest_marks)
lowest_marks=student.min_mark()
print(lowest_marks)
avg_marks=student.avg()
print(avg_marks)
latest_marks=student.add_new_mark(79)
print(latest_marks)
student.remove_marks_at(4)
print(student.marks)

