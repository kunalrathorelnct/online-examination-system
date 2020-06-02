from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources
class StudentResource(resources.ModelResource):
	class Meta:
		model = Student
		import_id_fields = ('email',)
admin.site.register(Exam)
admin.site.register(Student_Exam)
admin.site.register(Question)
admin.site.register(Student_Response)
admin.site.register(Section)
class StudentAdmin(ImportExportModelAdmin):
	resource_class = StudentResource
admin.site.register(Student,StudentAdmin)