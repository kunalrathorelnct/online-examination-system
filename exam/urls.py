from django.urls import path,include

from . import views 

app_name = 'exam'

urlpatterns = [
    	path('<str:exam_code>/<uuid:uid>',views.examView)
    ]