from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User



# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
    return render(request,"auth/login.html")

def register(request):
    username = request.POST.get("user")
    email = request.POST.get("email")
    password = request.POST.get("password")
    if User.objects.filter(username__iexact=username).exists():
        return render(request, "auth/register.html", {"error": "Username already exists"})
    if User.objects.filter(email__iexact=email).exists():
            print("Email already exists")
            return render(request, "auth/register.html", {"error": "Email already exists"})
    if username and email and password:
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect("/")
    return render(request,"auth/register.html")

VALID_CODE = "abc123"

def pwd_protected(request):
    is_allowed = request.session.get('protected_page_allowed') or 0
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            request.session['protected_page_allowed'] = 1
    if is_allowed:
        return render(request, "protected/view.html")
    return render(request, "protected/entry.html")