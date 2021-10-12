from django.urls import path
from .views import ShowAll, ShowPackage

app_name = 'trek'

urlpatterns = [
    path('show-all/', ShowAll.as_view()),
    path('<int:id>/', ShowPackage.as_view())
]
