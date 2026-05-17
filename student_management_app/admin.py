from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from student_management_app.models import *

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)

admin.site.register(ClassTeacher)