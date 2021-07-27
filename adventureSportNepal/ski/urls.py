from django.urls import path
from .views import ShowAll


app_name = 'ski'

urlpatterns = [
    path('show-all/', ShowAll.as_view())
]
