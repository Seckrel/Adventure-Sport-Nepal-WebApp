from django.urls import path
from .views import index, index_with_id

app_name = 'frontend'

urlpatterns = [
    path('', index, name='home'),
    path('trek/<int:id>/', index_with_id),
    path('ski/<int:id>/', index_with_id),
    path('faq', index),

]