from django.shortcuts import render,redirect,get_object_or_404
from .models import Announce
from account.models import Category,MyUser
from .forms import AnnounceForm
from django.utils import timezone


def index(request):
    return render(request, 'index.html')

def homeP(request,name):
    return render(request, 'homeP.html')

def announce(request,name):
    user=get_object_or_404(MyUser,username=name)
    announces=Announce.objects.all()
    context={'announces':announces,'name':name}
    return render(request,'announce.html',context)

def nu_announce(request,name):
    categories= Category.objects.all()
    if request.method == 'POST':
        form =AnnounceForm(request.POST)
        user= get_object_or_404(MyUser,username=name)
        data=request.POST.copy()
        cat=data.get('Catgy')
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
                        receivers=MyUser.objects.filter(category=cat,Lecturer=lect)
                else:
                    receivers=MyUser.objects.all()        
            else:
                    receivers=MyUser.objects.all()
                
                # for receiver in receivers:
                    # announce.receiver.add(receiver)    
            # users=MyUser.objects.all()
            # context={'receivers':receivers,'users':users,
            #         'category':cat,'student':std,'lecturer':lect,'college_council':col_cnl,'academic_council':acad_cnl,
            #         'school_council':skl_cnl,'department_council':dep_cnl,'school':skl,'department':dep,'level':lev} 
            # return render(request,'zero.html',context)   
            for receive in receivers:
                announce.receiver.add(receive)  
            return redirect('board',name=user.username)  
        
    else:
        form=AnnounceForm()      
    context={'form':form,'categories':categories}    
    return render(request,'nu_announce.html',context)

def board(request,name):
    user= get_object_or_404(MyUser,username=name)
    announces =Announce.objects.filter(sender=user.pk)
    receivers=MyUser.objects.filter(category='Student')
    context={'announces':announces,'name':name,'receivers':receivers}
    return render(request,'board.html',context)

def view_announce(request,name,pky):
    user= get_object_or_404(MyUser,username=name)
    announce=get_object_or_404(Announce,pk=pky)
    context={'announce':announce,'user':user}
    return render(request,'view_announce.html',context)

def receiver(request):
    users=MyUser.objects.all()
    return render(request,'zero.html',{'users':users})    