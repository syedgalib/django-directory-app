from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:listing_id>', views.single, name='single'),
]
