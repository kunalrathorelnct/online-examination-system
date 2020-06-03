from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls import url

from . import views 

app_name = 'exam'

urlpatterns = [
		path('instruction/<uuid:uid>/', views.infoView,name='instructions'),
		path('iframeview/<uuid:uid>',views.iframeview,name='iframe'),
		path('ques/<uuid:uid>',views.iframeview1,name='iframe1'),
		path('onlineexam/<uuid:uid>', views.onlineexam, name='onlineexam'),
		path('examsummary/<uuid:uid>', views.examSummary, name='examsummary'),
		path('uploadimage/<uuid:uid>/',views.PhotoUploadView.as_view()),
    	path('info/<uuid:uid>/',views.examView),
    	path('getquestion/<uuid:uid>/',views.StudentQuizView.as_view()),
    	path('response/<uuid:uid>/',views.StudentResponse.as_view()),
    ] 
