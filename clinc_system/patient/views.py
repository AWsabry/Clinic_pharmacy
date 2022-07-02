from django.shortcuts import redirect, render
from patient.forms import AppointmentForm, LoginForm, RegisterForm
from django.views.decorators.csrf import csrf_exempt
from patient.models import Appointment, Profile
from django.contrib.auth import authenticate, logout
from django.contrib.auth import authenticate, login as user_login
from django.contrib import messages

# Create your views here.


@csrf_exempt
def login(request):
    form = LoginForm(request.POST, request.FILES)
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            if form.is_valid():
                print("Post")
                email = request.POST.get('email')
                password = request.POST.get('password')
                user = authenticate(request, email=email, password=password)
                print(user)
                user_login(request, user)
                return redirect('/')
    return render(request, 'login.html',)


def index(request):
    # x = Roshetta.objects.filter(user= request.user).all()
    # print(x)
    return render(request, 'index.html',)


def logOut(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        email = form.data.get('email')
        first_name, last_name = form.data.get(
            'first_name'), form.data.get('last_name')
        password = form.data.get('password1')

        user = Profile.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        return redirect('/login')
    else:
        form = RegisterForm()
        return render(request, "register.html",  {
        })

def appointment(request):
    form = AppointmentForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            email = request.POST.get('email')
            name = request.POST.get('name')
            what_for = request.POST.get('what_for')
            PhoneNumber = request.POST.get('PhoneNumber')
            date = request.POST.get('date')
        Appointment.objects.create(
            name = name,
            email = email,
            what_for = what_for,
            PhoneNumber = PhoneNumber,
            date = date,
        )
        return redirect('/')
    return render(request, 'appointment.html',)