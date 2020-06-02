from django.shortcuts import render,HttpResponse
from .models import Student_Exam,Question,Section
# Create your views here.
from django.utils import timezone
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

def onlineexam(request,uid=None):
	if request.method=='GET':
		if uid:
			student_object = Student_Exam.objects.get(external_identifier = uid)
			exam = student_object.exam
			questions = Question.objects.filter(exam=exam)
		else:
			return HttpResponse("Invalid Request")
		student_object.start_time = timezone.now()
		sections = student_object.exam.no_of_sections
		return render(request,'quiz.html',{'uid':uid,'sections':sections,'questions':questions,'exam':exam,'range':range(1,len(questions)+1)})
	
def iframeview(request,uid):
	try:
		section = request.query_params['section']
	except:
		section = 1
	uid = uid
	exam = Student_Exam.objects.get(external_identifier=uid).exam
	questions = Question.objects.filter(exam=exam,section =section)
	return render(request,'iframesquestionpaper.html',{'questions':questions})

def examView(request,uid):
	if request.method=='GET':
		student_object = Student_Exam.objects.get(external_identifier = uid)
		if student_object.exam.start_time<=timezone.now():
			student =student_object.student
			exam = student_object.exam
			return render(request,'index.html',{'student':student,'exam':exam,'uid':uid})
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

class PhotoUploadView(APIView):
	def post(self, request,uid, *args, **kwargs):
		ss = request.data['file']
		student_object = Student_Exam.objects.get(external_identifier = uid)
		student_object.ss = ss
		student_object.save()
		return Response({'status':'ok'})