from django.urls import path,include

from . import views 

app_name = 'exam'

urlpatterns = [
    	path('info/<uuid:uid>/',views.examView),
    	path('getquestion/<uuid:uid>/',views.StudentQuizView.as_view()),
    	path('response/<uuid:uid>/',views.StudentResponse.as_view()),
    ] 