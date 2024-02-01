from django.urls import path
from .views import *

urlpatterns = [
    path('suv/', sign_up_view, name='signup_url'),
    path('siv/', sign_in_view, name='signin_url'),
    path('sov/', sign_out_view, name='signout_url')
]