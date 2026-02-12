# Create your views here.
from django.shortcuts import render, redirect
from .models import EntryPass
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def menu(request):
    return render(request, 'menu.html')



def visitor_entry(request):


    if request.method == "POST":
        name = request.POST['name']
        place = request.POST['place']
        cat = request.POST['category']

        if EntryPass.objects.filter(name=name).exists():
            messages.error(request, "Visitor already exists")
            return redirect('entry')
        else:
            entry = EntryPass.objects.create(name=name, place=place, category=cat)
            messages.success(request, "Visitor added successfully")
            return render(request, 'pass.html', {'p': entry})

    return render(request, 'entry.html')



def visitor_list(request):
    visitors = EntryPass.objects.all()
    return render(request, 'list.html', {'visitors': visitors})



def summary(request):
    total = EntryPass.objects.count()
    students = EntryPass.objects.filter(category="Student").count() 
    employees = EntryPass.objects.filter(category="Employee").count()
    unemp = EntryPass.objects.filter(category="Un-Employee").count()
    return render(request, 'summary.html', {'total': total,'students': students,'employees': employees,'unemp': unemp})
