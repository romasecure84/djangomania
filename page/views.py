from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from random import randint
from page.models import Page

FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/400" for id in range(11, 16)
]

def home_view(request):
    # context = {'platform': f'Django Platformu Istifade Edildi: {randint(1, 100)} '}
    page_title = 'Ana Sehife'
    context = dict(page_title = page_title,
                    #FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
                    FAKE_DB_CAROUSEL = FAKE_DB_CAROUSEL,)
    return render(request, 'page/home_page.html', context)


def page_view(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    context = dict(
        page = page,
    )
    return render(request, "page/page_detail.html", context)
 
