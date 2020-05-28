from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Student_Exam)
admin.site.register(Questions)
admin.site.register(Student_Response)
