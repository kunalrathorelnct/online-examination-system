from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		exclude = ('exam',)

# class StudentExamSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Student_Exam
# 		fields = ('ss','external_identifier','exam','student',)