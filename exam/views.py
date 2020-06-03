from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
from django.utils import timezone
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import base64
from django.core.files.base import ContentFile


def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))

def onlineexam(request,uid):
	if request.method=='GET':
		if uid:
			student_object = Student_Exam.objects.get(external_identifier = uid)
			exam = student_object.exam
			questions = Question.objects.filter(exam=exam)
		else:
			return HttpResponse("Invalid Request")
		student_object.start_time = timezone.now()
		sections = Section.objects.filter(exam=exam)
		student_object.start_time = timezone.localtime(timezone.now())
		student_object.save()

		return render(request,'quiz.html',{'uid':uid,'sections':sections,'questions':questions,'exam':exam,'range':range(1,len(questions)+1)})
def examSummary(request,uid):
	if request.method=='GET':
		if uid:
			student_object = Student_Exam.objects.get(external_identifier = uid)
			exam = student_object.exam
		else:
			return HttpResponse("Invalid Request")
		student_object.start_time = timezone.now()
		sections = Section.objects.filter(exam=exam)
		return render(request,'examsummary.html',{'sections':sections})

def iframeview(request,uid):
	try:

		section = request.GET.get('section')
	except:
		section = 1
	uid = uid
	exam = Student_Exam.objects.get(external_identifier=uid).exam
	questions = Question.objects.filter(exam=exam,section=Section.objects.get(id=section))
	return render(request,'iframesquestionpaper.html',{'questions':questions})

def iframeview1(request,uid):
	try:
		section = request.GET.get('section')
	except:
		section = 1
	uid = uid
	exam = Student_Exam.objects.get(external_identifier=uid).exam
	questions = Question.objects.filter(exam=exam,section=Section.objects.get(id=section))
	return render(request,'questionpaper.html',{'questions':questions})

def infoView(request,uid):
	if request.method=='GET':
		student_object = Student_Exam.objects.get(external_identifier = uid)
		if student_object.exam.start_time<=timezone.localtime(timezone.now()):
			exam = student_object.exam
			duration = str(exam.total_duration/1000/1000)[-3:]	
			sections = Section.objects.filter(exam=exam)
			return render(request,'iframesInstruction.html',{'student_object':student_object,'exam':exam,'sections':sections,'duration':duration})


def examView(request,uid):
	if request.method=='GET':
		student_object = Student_Exam.objects.get(external_identifier = uid)
		if student_object.exam.start_time<=timezone.localtime(timezone.now()):
			student =student_object.student
			subject_name = student_object.exam.subject_name
			return render(request,'index.html',{'student':student,'subject_name':subject_name,'uid':uid})
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
		student_exam = Student_Exam.objects.get(external_identifier=uid)
		student_response,created = Student_Response.objects.get_or_create(
				question = question,
				student_exam = student_exam
			)
		student_response.response = request.data.get('response')
		student_response.time_stamp = timezone.now()
		student_response.save()
		return Response({'status':'ok'})

class PhotoUploadView(APIView):
	def post(self, request,uid, *args, **kwargs):
		ss = request.data['file']
		student_object = Student_Exam.objects.get(external_identifier = uid)
		img_upload = ProcteredSS(student_exam=student_object,img=base64_file(ss))
		img_upload.save()
		return Response({'status':'ok'})

class WarningCountUpdate(APIView):
	def post(self,request,uid):
		student_object = Student_Exam.objects.get(external_identifier = uid)
		student_object.warning_count+=1
		if student_object.warning_count>=3:
			return Response({'status':'submit'})
		student_object.save()
		return Response({'status':'ok'})