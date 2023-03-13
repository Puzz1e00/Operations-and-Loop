class Department:

    def __init__(self, name, num_of_student):
        self.name = name
        self.num_of_student = num_of_student

    def totalstudents(self, *args):
        list_of_no = [i.num_of_student for i in args]
        other_total = sum(list_of_no)
        return self.num_of_student + other_total


d1= Department('Science', 24)
d2= Department('Mathematics', 25)
d3= Department('Account',20)
result = d1.totalstudents(d2, d3)
print(result)