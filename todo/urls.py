from django.urls import path
from todo.views import (
    all_todos_view, 
    category_view, 
    todo_detail_view, 
    tag_view
    )

urlpatterns = [
    # All Todos:
    path('', all_todos_view, name='all_todos_view'),
    path('category/<slug:category_slug>/', category_view, name='category_view'),
    path('tag/<slug:tag_slug>/', tag_view, name='tag_view'),

    # Toodo Detail:
    path('category/<slug:category_slug>/todo/<int:id>/', todo_detail_view, name='todo_detail_view'),
]
