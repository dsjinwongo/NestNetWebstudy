from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from django.utils import timezone
from .forms import ScheForm

# Create your views here.

def home(request):
    Schedules=Schedule.objects
    return render(request, 'blog/home.html', {'Schedules':Schedules})

def detail(request, sche_id):
    Sche_detail=get_object_or_404(Schedule, pk=sche_id)
    return render(request, 'blog/detail.html', {'Sche':Sche_detail})

def sche_new(request):
    if request.method =="POST":
        form =ScheForm(request.POST)
        if form.is_valid():
            Sche=form.save(commit=False)
            Sche.published_date=timezone.datetime.now()
            Sche.save()
            return redirect('detail', sche_id=Sche.pk)
    else:
        form =ScheForm()
    return render(request, 'blog/sche_new.html',{'form':form})

def sche_edit(request, sche_id):
    Sche=get_object_or_404(Schedule, pk=sche_id)
    if request.method == "POST":
        form=ScheForm(request.POST, instance=Sche)
        if form.is_valid():
            sche=form.save(commit=False)
            sche.published_date=timezone.datetime.now()
            sche.save()
            return redirect('detail', sche_id=sche.pk)
    else:
        form=ScheForm(instance=Sche)
    return render(request, 'blog/sche_edit.html',{'form':form})

def sche_delete(request, sche_id):
    sche=get_object_or_404(Schedule, pk=sche_id)
    sche.delete()
    return redirect('home')