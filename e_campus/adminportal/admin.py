from django.contrib import admin
from .models import Role
from .models import User
from .models import Course
from .models import StudentCourse,Batch,BatchDetails,BatchTime,Attendance
# # Register your models here.

# Register your models here.
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(Batch)
admin.site.register(BatchDetails)
admin.site.register(BatchTime)
admin.site.register(Attendance)