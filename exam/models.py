from django.db import models
import uuid
import datetime
# Create your models here.


class Student(models.Model):
	email = models.EmailField(primary_key=True)
	name = models.CharField(max_length=50)
	roll_no = models.CharField(max_length=20)

	def __str__(self):
		return self.roll_no


class Exam(models.Model):
	subject_name = models.CharField(max_length=50)
	start_time = models.DateTimeField(blank=False,null=False)
	total_duration = models.DurationField()
	total_marks = models.IntegerField(default=100)
	negative_marks = models.IntegerField(default=0)
	no_of_sections = models.IntegerField(default=1)
	def __str__(self):
		return self.subject_name

class Section(models.Model):
	exam = models.ForeignKey(Exam,on_delete = models.CASCADE)
	section_name = models.CharField(max_length=20)
	section_duration = models.DurationField()
	total_marks = models.IntegerField(default=100)

	def __str__(self):
		return self.section_name

class Student_Exam(models.Model):
	def file_path_ss(self,filename):
		return "students/{0}/{1}/{2}".format(self.exam.subject_name,self.student.roll_no,str(datetime.datetime.now())+'.png')

	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
	external_identifier = models.UUIDField(unique=True, default=uuid.uuid4)
	warning_count = models.IntegerField(default=0)
	start_time = models.DateTimeField(null=True,blank=True)
	end_time = models.DateTimeField(null=True,blank=True)
	ss = models.FileField(null=True,blank=True,upload_to = file_path_ss)

	def __str__(self):
		return self.exam.subject_name+'_'+str(self.student.roll_no)

class Question(models.Model):
	def file_path(self,filename):
		return "/{0}/{1}/{2}".format(self.exam.subject_name,self.question_text[:5],filename)

	question_choice = (
		('single_choice','single_choice'),
		('multiple_choice','multiple_choice'),
		('subjective','subjective'),
		)

	exam = models.ForeignKey(Exam,on_delete = models.CASCADE)
	question_text = models.TextField()
	ex_img = models.FileField(null=True,blank=True,upload_to = file_path)
	question_type = models.CharField(max_length=20,choices=question_choice,default="single_choice")
	section = models.ForeignKey(Section,on_delete = models.CASCADE,null=True)
	marks = models.IntegerField(default=4)
	choices = models.CharField(max_length = 100,blank=True,null=True)
		

	def __str__(self):
		return self.question_text[:5]

class Student_Response(models.Model):
	student_exam = models.ForeignKey(Student_Exam,on_delete = models.CASCADE)
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	time_stamp = models.DateTimeField()
	response = models.TextField()

	class Meta:
		unique_together = ['student_exam','question']

	def __str__(self):
		return self.student_exam.exam.subject_name+'_'+str(self.student_exam.student.roll_no)+"_"+str(self.question)