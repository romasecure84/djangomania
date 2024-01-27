from django.shortcuts import render
from django.http import HttpResponse, Http404
from random import randint
from .fake_db.pages import FAKE_DB_PAGES

#FAKE_DB_PROJECTS = [
#    f"https://picsum.photos/id/{id}/100/80"  for id in range(121, 129) 
#]

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


def page_view(request, slug):
    result = list(filter(lambda x:(x['url'] == slug), FAKE_DB_PAGES))

    if result:
        context = dict(
            page_title = result[0]['title'],
            #FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
            detail= result[0]['detail'],
        )
        return render(request, "page/page_detail.html", context)
    raise Http404
