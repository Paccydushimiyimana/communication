from django.shortcuts import render,redirect,get_object_or_404
from .models import Announce,MyUser
from .forms import AnnounceForm
from django.utils import timezone


def index(request):
    return render(request, 'index.html')

def homeP(request,name):
    return render(request, 'homeP.html')

def announce(request,name):
    announces=Announce.objects.all()
    context={'announces':announces}
    return render(request,'announce.html',context)

def nu_announce(request,name):
    if request.method == 'POST':
        form =AnnounceForm(request.POST)
        user= get_object_or_404(MyUser,username=name)
        if form.is_valid():
            announce=form.save(commit=False)
            announce.creator=user
            announce.date=timezone.now()
            announce.save()
        return redirect('board',name=announce.creator)  
    else:
        form=AnnounceForm()      
    context={'form':form}    
    return render(request,'nu_announce.html',context)

def board(request,name):
    user= get_object_or_404(MyUser,username=name)
    announces =Announce.objects.filter(creator=user.pk)
    context={'announces':announces,'name':name}
    return render(request,'board.html',context)

def view_announce(request,name,pky):
    user= get_object_or_404(MyUser,username=name)
    announce=get_object_or_404(Announce,pk=pky,creator=user.pk)
    context={'announce':announce}
    return render(request,'view_announce.html',context)