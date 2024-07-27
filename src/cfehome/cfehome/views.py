from django.shortcuts import render
from visits.models import PageVisit


def home_page_view(request):
    page_visit = PageVisit.objects.filter(path=request.path)
    page_visit_total = PageVisit.objects.all()
    page_visit_create = PageVisit.objects.create()
    
    return render(request, 'home.html', my_context = {'page_visit': page_visit})
