from django.shortcuts import render

# Create your views here.

def examView(request,exam_code,uid):
	print(exam_code,uid)
	return render(request,'exam.html')