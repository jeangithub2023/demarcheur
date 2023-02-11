from django.urls import path
from menage.views import contact, detail, index, menage

app_name='menage'

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>/detail', detail, name='detail'),
    path('<int:id>/menage', menage, name='menage'),
    path('contact/', contact, name='contact'),
]