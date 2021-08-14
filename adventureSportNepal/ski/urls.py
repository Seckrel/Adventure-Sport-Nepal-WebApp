from django.urls import path
from .views import ShowAll, ShowPackage


app_name = 'ski'

urlpatterns = [
    path('show-all/', ShowAll.as_view()),
    path('<int:id>/', ShowPackage.as_view())
]
