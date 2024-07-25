from django.shortcuts import render, redirect  
from django.http import HttpResponse  
from django.template import loader  
from .models import Member
from .forms import MemberForm
from .forms import ContactForm

# Create your views here.
# def members(request):
#     return HttpResponse("Hello world")

def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def new_member(request):
    template = loader.get_template('new_member.html')
    return HttpResponse(template.render())

# == is equal to the value, === is equal to the value and data type
def all_members(request):
    if request.method == 'POST':
        # check if a member delete request is made
        member_id = request.POST.get('member_id')
        if member_id:
            try:
                member = Member.objects.get(pk=member_id)
                member.delete()
            except Member.DoesNotExist:
                pass #Hnalde if member does not exist or other errors

            # Riderect after delete to prevent duplicate POST on refresh
            return redirect('all_members') #Replace with your URL name of named urls.py
    
    # fetch all members
    members = Member.objects.all()
    
    context = {
        'members': members,
    }

    return render(request, 'all_members.html', context)

def member_create_view(request):
    if request.method == 'POST':
        form = MemberForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('member_success')
    else:
        form = MemberForm()
    return render(request, 'member_form.html', {'form': form})

#Member_AdminForm
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

def success(request):
    return render(request, 'Success_.html')