from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls import url

from . import views 

app_name = 'exam'

urlpatterns = [
		url('instruction', TemplateView.as_view(template_name="iframesInstruction.html"),name='instructions'),
		path('',views.home),
		path('onlineexam/', views.onlineexam, name='onlineexam'),
		
    	path('info/<uuid:uid>/',views.examView),
    	path('getquestion/<uuid:uid>/',views.StudentQuizView.as_view()),
    	path('response/<uuid:uid>/',views.StudentResponse.as_view()),
    ] 
