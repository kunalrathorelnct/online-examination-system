from django.shortcuts import render,HttpResponse
from .models import Student_Exam,Question
# Create your views here.
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone

def onlineexam(request):
	return render(request,'quiz.html')
	
def home(request):
	return render(request,'index.html')

def iframeview(request):
	return render(request,'iframesquestionpaper.html')

def examView(request,uid):
	if request.method=='GET':
		student_object = Student_Exam.objects.get(external_identifier = uid)
		if student_object.exam.start_time<=timezone.now():
			name = student_object.student.name
			email = student_object.student.email
			sections = student_object.exam.sections
			student_object.start_time = timezone.now()
			return render(request,'exam.html',{'name':name,'email':email,'sections':sections})
		else:
			return HttpResponse("Start time is "+str(student_object.start_time)+"Or paper was Over")
	return HttpResponse("Only Get Allowded")


class StudentQuizView(APIView):
	def get(self,request,uid):
		section = request.query_params['section']
		uid = uid
		exam = Student_Exam.objects.get(external_identifier=uid).exam
		questions = Question.objects.filter(exam=exam,section_no =section)
		questions = QuestionSerializer(questions,many=True)
		
		return Response({'questions':questions.data})

class StudentResponse(APIView):
	def post(self,request,uid):
		question = int(request.data.get('question'))
		question = Question.objects.get(pk=question)
		student_exam = Student_Exam.objects.get(external_identifier=uid).exam
		student_response,created = Student_Response.objects.get_or_create(
				question = question,
				student_exam = student_exam.id
			)
		student_response.response = request.data.get('response')
		student_response.time_stamp = timezone.now()
		student_response.save()
		return Response({'status':'ok'})

