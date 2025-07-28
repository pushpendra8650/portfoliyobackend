from django.urls import path
from .views import ContactCreateAPIView

urlpatterns = [
    path('api/contact/', ContactCreateAPIView.as_view(), name='contact-create'),
]
