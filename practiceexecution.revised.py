# I have tried to seperate the code into  files but it doesn't work anymore. So I just put all the codes in one file. 
class Questions: 
    def __init__(self, question_num, question, question_type):
        self.question_num = question_num
        self.question = question 
        self.question_type = question_type 

    def question_type(self, algorithm, python):
        self.algorithm = algorithm
        self.python = python

    def __str__(self):
        res = "Question number: " + str(self.question_num) + "\nQuestion: " + self.question + "\nType: " + self.question_type + "\n"
        return res

class Answers:
    def __init__(self, student_name, question, q_marks):
        self.student_name = student_name
        self.question = question
        self.q_marks = q_marks


    def __str__(self):
        res = "\nName: " + self.student_name + "\n"+ str(self.question) + "Marks: " + str(self.q_marks) + "\n"
        return res


class Grade:
    def __init__(self, answer):
        self.answer = answer

    def calculation(self):
        total_marks = 0 
        algorithm_total_marks = 0
        python_total_marks = 0 
        count_type_algorithm = 0
        count_type_python = 0
        for answer in self.answer:
    
            if answer.question.question_type == "python":
                python_total_marks += answer.q_marks
                count_type_python += 1

            if answer.question.question_type == "algorithm":
                algorithm_total_marks += answer.q_marks
                count_type_algorithm += 1

        if python_total_marks < (count_type_python * 10) * 0.5 or algorithm_total_marks < (count_type_algorithm * 10) * 0.5:
            return total_marks
    
        else:
            total_marks = python_total_marks + algorithm_total_marks
            return total_marks



# 		if question_type is algorithm: 
# 			algorithm_marks += question_marks 
# 		if question_type is python:
# 			python_marks += question_marks 
# 		if  algorithm_marks < 10 or python_marks < 10: 
# 			total_marks = 0 
# 		else: 
# 			total_marks = algorithm_marks +  python_marks 
# 		return total_marks 
# #I think there are some problems here, therefore is not running now. 

    def __str__(self):
        res = self.answer
        res = res + "Student" + self.student_name + "\nTotal Marks: " + str(self.total_marks)
        return res


q1 = Questions(1, "How are you?", "algorithm")
q2 = Questions(2, "hello world?", "algorithm")
q3 = Questions(3, "boom?", "python")
q4 = Questions(4, "bello?", "python")

print(q1, q2, q3, q4)

ans1 = Answers("Michelle", q1, 10)
ans2 = Answers("Michelle", q2, 8)
ans3 = Answers("Michelle", q3, 9)
ans4 = Answers("Michelle", q4, 7)
ans5 = Answers("Ann", q1, 8)
ans6 = Answers("Ann", q2, 8)
ans7 = Answers("Ann", q3, 1)
ans8 = Answers("Ann", q4, 2)
ans9 = Answers("Peter", q1, 2)
ans10 = Answers("Peter", q2, 2)
ans11 = Answers("Peter", q3, 2)
ans12 = Answers("Peter", q4, 2)


answer_1 = [ans1, ans2, ans3, ans4]
answer_2 = [ans5, ans6, ans7, ans8]
answer_3 = [ans9, ans10, ans11, ans12]


grade1 = Grade(answer_1)
grade2 = Grade(answer_2)
grade3 = Grade(answer_3)
final_marks1 = grade1.calculation()
final_marks2 = grade2.calculation()
final_marks3 = grade3.calculation()

print("\nfinal marks 1: " + str(final_marks1))
print("\nfinal marks 2: " + str(final_marks2))
print("\nfinal marks 3: " + str(final_marks3))

# I want to print the student_name with final marks but I cannot find the way to print the first attributes in an objects. 
# I can only print the whole objects
print(ans1.__dict__.values())







#function is outside the class
#method is inside the class 
