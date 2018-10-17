# I have tried to seperate the code into  files but it doesn't work anymore. So I just put all the codes in one file. 
class Questions: 
	def __init__(self, questions_num, questions, questions_type):
		self.questions_num = questions_num
		self.questions = questions 
		self.questions_type = questions_type 

	def questions_type(self, algorithm, python):
		self.algorithm = algorithm
		self.python = python

	def __str__(self):
		res = "Question number: " + str(self.questions_num) + "\nQuestion: " + self.questions + "\nType: " + self.questions_type + "\n"
		return res

class Answers:
	def __init__(self, student_name, question, question_marks):
		self.student_name = student_name
		self.question = question
		self.question_marks = question_marks

		
	def __str__(self):
		res = "\nName: " + self.student_name + "\n"+ str(self.question) + "Marks: " + str(self.question_marks) + "\n"
		return res



class Grade:
	def __init__(self, answer):
		self.answer = answer


	total_marks = 0 
	def total_marks(algorithm_marks, python_marks):
		if questions_type is algorithm: 
			algorithm_marks += question_marks 
		if question_type is python:
			python_marks += question_marks 
		return
		if  algorithm_marks < 10 or python_marks < 10: 
			total_marks = 0 
		else: 
			total_marks = algorithm_marks +  python_marks 
			return total_marks 
#I think there are some problems here, therefore is not running now. 

	def __str__(self):
		res = self.answer
		res = res + "\nTotal Marks: " + str(self.total_marks)
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
ans5 = Answers("Ann", q1, 1)
ans6 = Answers("Ann", q2, 2)
ans7 = Answers("Ann", q3, 1)
ans8 = Answers("Ann", q4, 2)

print(ans1, ans2, ans3, ans4)

answer_1 = [ans1, ans2, ans3, ans4]
answer_2 = [ans5, ans6, ans7, ans8]

grade1 = Grade(answer_1)
final_score = grade1.total_marks

print(final_score)






#function is outside the class
#method is inside the class 
