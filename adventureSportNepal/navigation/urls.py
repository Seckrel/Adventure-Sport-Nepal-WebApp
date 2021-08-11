from django.urls import path
from .views import *

urlpatterns = [
    path('show-nav', NavigationList.as_view())
]