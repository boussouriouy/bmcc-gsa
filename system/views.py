from django.shortcuts import render, redirect
from django.contrib import messages    
from django.contrib.auth.models import User
from .models import Event, Document
from student.form import StudentForm
from .choices import event_choices
# Create your views here.
def index(request):
    obj1 = Event.objects.order_by('-date').filter(is_present=True)
    obj2 = Document.objects.all()
    context = {
        'events': obj1,
        'documents': obj2
        
    }
    return render(request, 'index.html', context)


def postEvent(request):
    obj = Event.objects.order_by('-date')
    context = {
        'event': obj
        
    }
    return render(request, 'event.html', context)


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

            
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already taken')
            return redirect(".")
        
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect(".")
        
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username, email=email)
            user.save();
            messages.info(request, 'successfully registred ' + str(user)+ ' set your profile')
            return redirect('/student/form')  
              
    else:
       return render(request, 'register.html')


def postEvent(request):
    querySet = Event.objects.order_by('-date')
    # Description
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # this for description only icontains with keywords or any paragraph
            querySet = querySet.filter(description__icontains=keywords)

    # # Title
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            querySet = querySet.filter(title__iexact=title)


    context = {
        'event': querySet,
        'event_choices':event_choices,
        # This line here is to say that if we search for something that word stays on the search field
        'values': request.GET
    }
    return render(request, 'event.html', context)