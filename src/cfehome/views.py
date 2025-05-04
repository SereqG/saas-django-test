from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.filter(path=request.path)

    context = {"page_visit_count": len(queryset)}

    PageVisit.objects.create(path=request.path)

    return render(request, "home.html", context)
