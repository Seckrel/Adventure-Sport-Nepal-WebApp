from django.urls import path
from .views import index

app_name = 'frontend'

urlpatterns = [
    path('', index, name='home'),
    path('trek', index),
    path('ski', index),
    path('faq', index),

]