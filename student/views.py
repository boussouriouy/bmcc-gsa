from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import Member
from .form import StudentForm
# Create your views here.
def member(request):
    obj = Member.objects.all()
    
    # This is for the paginator
    obj1 = Member.objects.all()
    paginator = Paginator(obj1, 8)
    page = request.GET.get('page')
    paged_obj = paginator.get_page(page)
    context = {
        'member': obj,
        'member': paged_obj
    }
    return render(request, 'member.html', context)

def detail(request, detail_id):
    obj = get_object_or_404(Member, pk=detail_id)
    context = {
        'details': obj
    }
    return render(request, 'detail.html', context)

def form(request):
    my_form = StudentForm(request.POST, request.FILES)
    if my_form.is_valid():
       my_form.save();
       my_form = StudentForm()
       return redirect('member')
       
    context ={
      'profile':my_form  
    }
    return render(request, 'form.html', context)


