from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.utils.html import format_html

class ProcteredAdmin(admin.ModelAdmin):
    search_fields = ('student_exam__student__roll_no',)
    def image_tag(self, obj):
        return format_html('<img src="{}" height="100px"/>'.format(obj.img.url))
    list_display = ('__str__','image_tag',)
    image_tag.short_description = 'Image'
    
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
#admin.site.register(Student_Exam)
admin.site.register(Question)
admin.site.register(Student_Response)
admin.site.register(Section)
class StudentAdmin(ImportExportModelAdmin):
	resource_class = StudentResource
admin.site.register(Student,StudentAdmin)

class StudentExamAdmin(ImportExportModelAdmin):
	resource_class = StudentExamResource
admin.site.register(Student_Exam,StudentExamAdmin)