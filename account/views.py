from django.shortcuts import render, redirect, get_object_or_404 
from .models import College,School,Department,Level,Category,Student_category,Lecturer_category
from .models import Department_council,School_council,College_council,Academic_council,MyUser
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from account.forms import SignUpForm

def home(request):
    return render(request, 'home.html')

def load_departments(request):
    skl= request.GET.get('school')
    school = School.objects.get(name=skl)
    departments = Department.objects.filter(school=school)
    context={'departments':departments}
    return render(request, 'dep_options.html', context)

def load_levels(request):
    depart=request.GET.get('department')
    department =Department.objects.get(name=depart)
    levels=Level.objects.filter(department=department)
    context={'levels':levels}
    return render(request, 'lv_options.html', context)

def load_category(request):
    cat=request.GET.get('category')
    student_cats=Student_category.objects.all()
    lecturer_cats=Lecturer_category.objects.all()
    col_council_cats=College_council.objects.all()
    skl_council_cats=School_council.objects.all()
    dep_council_cats=Department_council.objects.all()
    acad_council_cats=Academic_council.objects.all()
    schools=School.objects.all()
    levels=Level.objects.all()
    context={'cat':cat,'student_cats':student_cats,'lecturer_cats':lecturer_cats,
            'col_council_cats':col_council_cats,'dep_council_cats':dep_council_cats,
            'schools':schools,'levels':levels,'skl_council_cats':skl_council_cats,
            'acad_council_cats':acad_council_cats }
    return render(request, 'cat_selected.html', context)

def register(request):
    form=SignUpForm(request.POST)
    categories=Category.objects.all()  
    if request.method == 'POST':
        data=request.POST.copy()  
        cat=str(data.get('Catgy'))      
        std=str(data.get('Std_cat'))
        if std == 'None':
            std ='.x.'
        regN=str(data.get('Reg'))
        if regN == 'None':
            regN ='.x.'
        lect=str(data.get('Lect'))
        if lect == 'None':
            lect ='.x.'
        stfId=str(data.get('Staff'))
        if stfId == 'None':
            stfId ='.x.'
        col_cnl=str(data.get('Col_council_cat'))
        if col_cnl == 'None':
            col_cnl ='.x.'
        acad_cnl=str(data.get('Acad_council_cat'))
        if acad_cnl == 'None':
            acad_cnl ='.x.'
        skl_cnl=str(data.get('Skl_council_cat'))
        if skl_cnl == 'None':
            skl_cnl ='.x.'
        dep_cnl=str(data.get('Dep_council_cat'))
        if dep_cnl == 'None':
            dep_cnl ='.x.'
        skl=str(data.get('Skl'))
        if skl == 'None':
            skl ='.x.'
        dep=str(data.get('Depart'))
        if dep == 'None':
            dep ='.x.'
        lev=str(data.get('Lv'))
        if lev == 'None':
            lev ='.x.'
        if form.is_valid():
            user=form.save(commit=False)
            user.category=cat
            user.student=std
            user.regNo=regN
            user.lecturer=lect
            user.staffId=stfId
            user.college_council=col_cnl
            user.academic_council=acad_cnl
            user.school_council=skl_cnl
            user.department_council=dep_cnl
            user.school=skl
            user.department=dep
            user.level=lev
            user.save()
            login(request, user) 
            return redirect('announce',name=user.username)
                        
        else:
            return redirect('register')
    context={'categories':categories,'form':form}
    return render(request, 'register.html', context)

def loginfx(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                context={'form':form,'user':user}
                return redirect('announce' , name=username)
            else:
                messages.error(request,"Invalid username or password")    
        else:
            messages.error(request,"Form not valid")
    form=AuthenticationForm()
    context={'form':form}
    return render(request,'login.html',context)

def logoutfx(request):
    logout(request)
    return redirect('/')

def trie(request):
    user=request.user
    context={'user':user}
    subject='this is my subject'
    message=render_to_string('mail.html',context)
    from_email=settings.EMAIL_HOST_USER
    to=[settings.EMAIL_HOST_USER]
    fail_silently=False

    send_mail(subject,message,from_email,to,fail_silently)
    return HttpResponse('okay')    

# def trie(request):
#     user=request.user
#     context={'user':user}
#     subject='this is my subject'
#     message=render_to_string('mail.html',context)
#     from_email=settings.EMAIL_HOST_USER
#     to=[settings.EMAIL_HOST_USER]
#     fail_silently=False

#     send_mail(subject,message,from_email,to,fail_silently)
#     return HttpResponse('okay') 