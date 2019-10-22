from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm,MyUserChangeForm
from .models import College,School,Department,Level,Category,Student_category,Lecturer_category
from .models import College_council,School_council,Department_council,Academic_council,MyUser


class MyUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username','email']


admin.site.register(MyUser,MyUserAdmin)
admin.site.register(College)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Category)
admin.site.register(Student_category)  
admin.site.register(College_council)
admin.site.register(School_council)
admin.site.register(Department_council)  
admin.site.register(Academic_council)
admin.site.register(Lecturer_category)

