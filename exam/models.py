from django.db import models
# Create your models here.


class Student(models.Model):
	email = models.EmailField(primary_key=True)
	name = models.CharField(max_length=50)

class Exam(models.Model):
	exam_code = models.CharField(unique=True,max_length=20)
	start_time = models.DateTimeField(blank=False,null=False)
	duration = models.DurationField()

class Student_Exam(models.Model):
	def file_path(self,filename):
		return "{0}/{1}/{2}".format(self.exam.exam_code,self.student.name,filename)

	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
	warning_count = models.IntegerField(default=0)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	ss = models.FileField(null=True,blank=True,upload_to = file_path)

class Questions(models.Model):
	def file_path(self,filename):
		return "{0}/{1}".format(self.exam.exam_code,filename)

	exam = models.ForeignKey(Exam,on_delete = models.CASCADE)
	question_text = models.TextField()
	ex_img = models.FileField(null=True,blank=True,upload_to = file_path)

class Student_Response(models.Model):
	student_exam = models.ForeignKey(Student_Exam,on_delete = models.CASCADE)
	question = models.ForeignKey(Questions,on_delete = models.CASCADE)
	time_stamp = models.DateTimeField(auto_now=True)
	response = models.TextField()
