from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, MyLoginView


app_name = 'accounts'


urlpatterns = [
    path('login/', MyLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
]
