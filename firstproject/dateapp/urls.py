from django.urls import path
from .views import get_date, get_year, get_day, get_month

urlpatterns = [
    path('', get_date, name="get_date"),
    path('year/', get_year),
    path('day/', get_day),
    path('month/', get_month)

]
