from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import FormDataForm,BranchForm,AccountTypeForm,MaterialForm,DistrictForm
from .models import Branch,AccountType,Material,FormData,District



def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bankapp:newpage')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('bankapp:login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']


        if not username or not password or not password1:
            messages.error(request, "Your registration is not completed")
            return redirect('bankapp:register')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('bankapp:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('bankapp:login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('bankapp:register')
    return render(request, "register.html")



def newpage(request):
    return render(request, "newpage.html")

def form(request):
    form = FormDataForm()
    if request.method == 'POST':
        form=FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Application Success")
            return redirect('bankapp:home')
    return render(request,"form.html",{'form':form})


def logout_view(request):
    logout(request)
    return redirect('bankapp:home')


def load_branch(request):
    district_id = request.GET.get('district_id')
    branch = Branch.objects.filter(branch_id=district_id).all()
    return render(request, 'coursedropdown.html', {'branch': branch})