from django.urls import path
from .views import activate,signup



urlpatterns = [
    path('signup/',signup,name='signup'),
    path('activate/<uidb64>/<token>/',activate, name='activate')
]
