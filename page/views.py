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

def about_us_view(request):
    page_title = 'Haqqimizda'
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi dictum, metus a euismod bibendum, libero urna hendrerit diam, sit amet ornare nibh ligula non arcu. Vivamus rutrum urna quis ex fermentum cursus. Aliquam varius erat sem, sit amet pellentesque ipsum venenatis non. Phasellus dapibus, ante posuere fermentum tristique, turpis libero iaculis arcu, eget gravida erat sem sit amet nulla. Nullam porttitor, nulla ut ultricies scelerisque, enim nulla laoreet metus, blandit lacinia turpis eros eget mauris. Nullam at egestas dolor. Quisque sagittis mattis commodo."
    context = {"page_title": page_title, 
            "hero_content": hero_content,
             #"FAKE_DB_PROJECTS" : FAKE_DB_PROJECTS,
    }
    return render(request, 'page/about_us_view.html', context)

def contact_us_view(request):
    page_title = 'Elaqe'
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi dictum, metus a euismod bibendum, libero urna hendrerit diam, sit amet ornare nibh ligula non arcu. Vivamus rutrum urna quis ex fermentum cursus. Aliquam varius erat sem, sit amet pellentesque ipsum venenatis non. Phasellus dapibus, ante posuere fermentum tristique, turpis libero iaculis arcu, eget gravida erat sem sit amet nulla. Nullam porttitor, nulla ut ultricies scelerisque, enim nulla laoreet metus, blandit lacinia turpis eros eget mauris. Nullam at egestas dolor. Quisque sagittis mattis commodo."
    context = dict(page_title = page_title, 
                   hero_content = hero_content,
                   #FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
    )
    return render(request, 'page/contact_us_view.html', context)

def vision_view(request):
    page_title = 'Vizyonumuz'
    context = dict(page_title = page_title,
                    #FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
                    )
    return render(request, 'page/vision.html', context)

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
