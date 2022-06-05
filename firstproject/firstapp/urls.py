
from django.urls import path
from .views import hellodjango, get_name
urlpatterns = [
    path('', hellodjango),
    path('<str:name>/', get_name)
]
