from django.shortcuts import render
from visits.models import PageVisit
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

LOGIN_URL = settings.LOGIN_URL

def home_view(request):
    if request.user.is_authenticated:
     print(request.user)
    return about_view(request)

def about_view(request):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0
    my_title = "My Page"
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count(),
    }
    PageVisit.objects.create(path=request.path)
    return render(request, 'home.html', my_context)
@login_required
def user_only_view(request):
    return render(request,"protected/user_only.html")

@staff_member_required(login_url="/warning/staff/member")
def staff_only_view(request):
    return render(request,"protected/staff_only.html")

def staff_only_warning(request):
    return render(request,"protected/staff_only_warning.html")