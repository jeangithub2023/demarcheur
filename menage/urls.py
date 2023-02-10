from django.urls import path
from menage.views import contact, detail, index

app_name='menage'

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>/detail', detail, name='detail'),
    path('contact/', contact, name='contact'),
]