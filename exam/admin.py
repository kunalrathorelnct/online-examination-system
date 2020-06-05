from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin,ExportActionModelAdmin
from import_export import resources
from django.utils.html import format_html

class ProcteredAdmin(admin.ModelAdmin):
    search_fields = ('student_exam__student__roll_no','student_exam__exam__subject_name',)
    def image_tag(self, obj):
        return format_html('<img src="{}" height="100px"/>'.format(obj.img.url))
    list_display = ('__str__','image_tag',)
    image_tag.short_description = 'Image'
    list_per_page = 20 
    
class StudentResource(resources.ModelResource):
	class Meta:
		model = Student
		import_id_fields = ('email',)

class StudentExamResource(resources.ModelResource):
	class Meta:
		model = Student_Exam
		fields = ('student','exam')
		import_id_fields = ('student',)
admin.site.register(ProcteredSS,ProcteredAdmin)
admin.site.register(Exam)

class StudentResponseAdmin(ExportActionModelAdmin):
	 list_filter = ('question__question_type',)
	 search_fields = ('student_exam__student__roll_no','student_exam__exam__subject_name',)
admin.site.register(Student_Response,StudentResponseAdmin)

class StudentAdmin(ImportExportModelAdmin):
	resource_class = StudentResource
admin.site.register(Student,StudentAdmin)

class StudentExamAdmin(ImportExportModelAdmin):
	resource_class = StudentExamResource
admin.site.register(Student_Exam,StudentExamAdmin)

class SectionAdmin(admin.ModelAdmin):
	exclude = ('total_marks','no_of_questions',)
admin.site.register(Section,SectionAdmin)

from django.forms import ModelForm
from django.core.validators import EMPTY_VALUES
class QuestionForm(ModelForm):
	class Meta:
		model = Question
		fields = '__all__'
	def clean(self):
		type_of_question = self.cleaned_data.get('question_type')
		if type_of_question=='single_choice' or type_of_question=='multiple_choice':
			choices = self.cleaned_data.get('choices')
			answer = self.cleaned_data.get('answer')
			if choices in EMPTY_VALUES:
				self._errors['choices'] = self.error_class([
    				'choices are required in MCQ'])
			if answer in EMPTY_VALUES:
				self._errors['answer'] = self.error_class([
    				'answer Field is required in MCQ'])
			
		return self.cleaned_data
class QuestionAdmin(admin.ModelAdmin):
	form = QuestionForm
	list_filter = ('exam__subject_name',)

admin.site.register(Question,QuestionAdmin)