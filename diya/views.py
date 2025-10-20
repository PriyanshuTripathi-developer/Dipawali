from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wish
from .forms import WishForm, RegisterForm
from django.http import JsonResponse
from .models import UserProfile, GlobalStats


def home(request):
    return render(request, 'home.html')

def leaderboard(request):
    return render(request, 'leaderboard.html')


def profile(request):
    if request.user.is_authenticated:
        wishes = Wish.objects.filter(user=request.user).order_by('-created_at')
        wish_count = Wish.objects.filter(user=request.user).count()
    else:
        wishes = []
        wish_count = 0;
        # wish_count = Wish.objects.filter(user=request.user).count()
    return render(request, 'profile.html', {'wishes': wishes  , 'wish_count': wish_count})

def wishes(request):
     wishes = Wish.objects.all().order_by('-created_at')
     return render(request, 'wishes.html', {'wishes': wishes})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_wish(request):
    if request.method == 'POST':
        form = WishForm(request.POST, request.FILES)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.user = request.user
            wish.save()
            return redirect('wishes')
    else:
        form = WishForm()
    return render(request, 'wish_form.html', {'form': form})

@login_required
def light_diyas(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    stats, _ = GlobalStats.objects.get_or_create(id=1) 
    if not profile.has_lit_diyas:
        profile.has_lit_diyas = True
        profile.save()

        stats.total_diyas += 1
        stats.save()

        return JsonResponse({
            'status': 'success',
            'already_lit': False,
            'total': stats.total_diyas
        })
    else:
        return JsonResponse({
            'status': 'success',
            'already_lit': True,
            'total': stats.total_diyas
        })

def get_total_diyas(request):
    stats, _ = GlobalStats.objects.get_or_create(id=1)
    return JsonResponse({'total': stats.total_diyas})