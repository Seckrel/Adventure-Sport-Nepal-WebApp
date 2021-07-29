from django.urls import path
from .views import ShowAll

app_name = 'trek'

urlpatterns = [
    path('show-all/', ShowAll.as_view())
]
