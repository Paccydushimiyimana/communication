from django.shortcuts import render,redirect,get_object_or_404
from .models import Announce
from account.models import Category,MyUser
from .forms import AnnounceForm
from django.utils import timezone
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def announce(request,name):
    user=request.user
    announcesall=Announce.objects.all().order_by('-id')
    announces=[]
    for announcet in announcesall:
        if user in announcet.receiver.all():
            announces.append(announcet)                
    context={'announces':announces}
    return render(request,'announce.html',context)

def nu_announce(request,name):
    categories= Category.objects.all()
    if request.method == 'POST':
        form =AnnounceForm(request.POST)
        user= get_object_or_404(MyUser,username=name)
        data=request.POST.copy()
        cate=data.get('Catgy')
        cat=str(cate)
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
            announce=form.save(commit=False)
            announce.sender=user
            announce.date=timezone.now()
            announce.save()
            
            if cat == 'Office of the Principal':
                receivers=MyUser.objects.filter(category=cat)
            elif cat == 'College council':
                if (col_cnl != ''):
                    receivers=MyUser.objects.filter(category=cat,college_council=col_cnl)
                else:    
                    receivers=MyUser.objects.filter(category=cat)
            elif cat == 'Academic Council':
                if acad_cnl != '':
                    receivers=MyUser.objects.filter(category=cat,academic_council=acad_cnl)
                else:  
                    receivers=MyUser.objects.filter(category=cat)
            elif cat == 'School_council':
                if skl_cnl != '':
                    if skl != '':
                        receivers=MyUser.objects.filter(category=cat,school_council=skl_cnl,school=skl)
                    else:
                        receivers=MyUser.objects.filter(category=cat,school_council=skl_cnl)    
                else:
                    receivers=MyUser.objects.filter(category=cat)
            elif cat == 'Department_council':
                if dep_cnl != '':
                    if skl != '':
                        if dep != '':
                            receivers=MyUser.objects.filter(category=cat,department_council=dep_cnl,school=skl,department=dep)
                        else:
                            receivers=MyUser.objects.filter(category=cat,department_council=dep_cnl,school=skl)
                    else:
                        receivers=MyUser.objects.filter(category=cat,department_council=dep_cnl)
                else:
                    receivers=MyUser.objects.filter(category=cat)
            elif cat == 'Student':
                if std != '':
                    if skl != '':
                        if dep != '':
                            if lev != 0:
                                receivers=MyUser.objects.filter(category=cat,student=std,school=skl,department=dep,level=lev)
                            else:
                                receivers=MyUser.objects.filter(category=cat,student=std,school=skl,department=dep,)
                        else:
                            receivers=MyUser.objects.filter(category=cat,student=std,school=skl)
                    else:
                        receivers=MyUser.objects.filter(category=cat,student=std)  
                else:
                    receivers=MyUser.objects.filter(category=cat)                
            elif cat == 'Lecturer':
                if lect != '':
                    if skl != '':
                        if dep != '':
                            if lev != 0:
                                receivers=MyUser.objects.filter(category=cat,lecturer=lect,school=skl,department=dep,level=lev)
                            else:
                                receivers=MyUser.objects.filter(category=cat,lecturer=lect,school=skl,department=dep,)
                        else:
                            receivers=MyUser.objects.filter(category=cat,lecturer=lect,school=skl)
                    else:
                        receivers=MyUser.objects.filter(category=cat,lecturer=lect)
                else:
                    receivers=MyUser.objects.all(category=cat)        
            else:
                    receivers=MyUser.objects.all() 
            for receive in receivers:
                announce.receiver.add(receive)  
            announce.view_by.add(user) 
            # return render(request,'ze.html',{'cat':cat})   
            return redirect('board',name=user.username)  
        
    else:
        form=AnnounceForm()      
    context={'form':form,'categories':categories}    
    return render(request,'nu_announce.html',context)

def board(request,name):
    user= request.user
    announces =Announce.objects.filter(sender=user.pk)
    context={'announces':announces,'name':name}
    return render(request,'board.html',context)

def view_announce_anct(request,name,pky):
    user= get_object_or_404(MyUser,username=name)
    announce=get_object_or_404(Announce,pk=pky)
    if user not in announce.view_by.all():
        announce.view_by.add(user)
    context={'announce':announce,'user':user}
    return render(request,'view_anct.html',context)

def view_announce_brd(request,name,pky):
    user= get_object_or_404(MyUser,username=name)
    announce=get_object_or_404(Announce,pk=pky)
    if user not in announce.view_by.all():
        announce.view_by.add(user)
    context={'announce':announce,'user':user}
    return render(request,'view_brd.html',context)    
 
def receiver(request):
    users=MyUser.objects.all()
    return render(request,'zero.html',{'users':users})    
 
def edit_announce(request,name,pky):
    user=request.user
    announce = get_object_or_404(Announce,pk=pky)
    form=AnnounceForm(request.POST or None, instance=announce)
    if form.is_valid():
        form.save()
        return redirect('view_announce_brd',name=user.username,pky=announce.pk)    
    context={'form':form}    
    return render(request,'edit_announce.html',context)    

def del_announce(request,name,pky):
    user=request.user
    announce = get_object_or_404(Announce,pk=pky)
    if request.method=='POST':
        announce.delete()
        return redirect('board',name=user)
    context={'announce':announce}    
    return render(request,'del_confirm.html',context)  
    
          