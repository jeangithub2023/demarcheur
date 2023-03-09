from django.urls import path
from menage.views import apropos, contact, detail, index, menage

app_name='menage'

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>/detail', detail, name='detail'),
    path('<int:id>/menage', menage, name='menage'),
    path('contact/', contact, name='contact'),
    path('apropos/', apropos, name='apropos'),
]