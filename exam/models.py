from django.db import models
import uuid
# Create your models here.


class Student(models.Model):
	email = models.EmailField(primary_key=True)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Exam(models.Model):
	exam_code = models.CharField(unique=True,max_length=20)
	start_time = models.DateTimeField(blank=False,null=False)
	duration = models.DurationField()

	def __str__(self):
		return self.exam_code

class Student_Exam(models.Model):
	def file_path(self,filename):
		return "{0}/{1}/{2}".format(self.exam.exam_code,self.student.name,filename)

	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
	external_identifier = models.UUIDField(unique=True, default=uuid.uuid4)
	warning_count = models.IntegerField(default=0)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	ss = models.FileField(null=True,blank=True,upload_to = file_path)

	def __str__(self):
		return str(self.student.name)+'_'+self.exam.exam_code

class Question(models.Model):
	def file_path(self,filename):
		return "{0}/{1}/{2}".format(self.exam.exam_code,self.question_text[:5],filename)

	exam = models.ForeignKey(Exam,on_delete = models.CASCADE)
	question_text = models.TextField()
	ex_img = models.FileField(null=True,blank=True,upload_to = file_path)


	def __str__(self):
		return self.question_text[:5]

class Student_Response(models.Model):
	student_exam = models.ForeignKey(Student_Exam,on_delete = models.CASCADE)
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	time_stamp = models.DateTimeField(auto_now=True)
	response = models.TextField()

	class Meta:
		unique_together = ['student_exam','question']

	def __str__(self):
		return self.student_exam.student.name+"_"+str(self.question)