from myproject.myapp.views import home,login,logout,register,save_register
from django.urls import path

urlpatterns = [
    path('home', home),
    path('login', login),
    path('logout',logout),
    path('register',register),
    path('save_register',save_register)
]
