class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_Students(Student_list):
  #sort the list of Student in descending order of CGPA
  sorted_Student = sorted(Student_list,
                          key=lambda Student: Student.cgpa,
                          reverse=True)
  #syntex - Lambda arg:exp
  return sorted_Student


#Example usage:
Students = [
    Student("Layoga", "A123", 7.8),
    Student("Yajeev",  "A124", 8.9),
    Student("kani", "A125", 9.1),
    Student("Visithkumar", "A126", 9.9),
]

sorted_Student = sort_Students(Students)

#print the sorted list of students
for Student in sorted_Student:
  print("Name: {},Roll Number: {}, CGPA: {}".format(Student.name, Student.roll_number, Student.cgpa))