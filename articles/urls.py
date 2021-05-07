from django.urls import path, include
from . import views 


urlpatterns = [
    path('', views.view_articles, name='view_articles'),
    path('<slug:slug>', views.article_details, name='article_details'),
]
