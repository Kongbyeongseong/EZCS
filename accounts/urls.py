# from django.urls import path 
# from . import views
# from django.contrib.auth import views as auth_views

# app_name = 'accounts'

# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(template_name='accounts/Login.html'), name='login'), 
#     #path('logout/', auth_views.LogoutView.as_view(template_name='accounts/Login.html'), name='logout'),
#     #path('signup/', auth_views.signupView.as_view(template_name='accounts/Login.html'), name='signup'),
# ]
from django.urls import path 
<<<<<<< HEAD
=======
from django.contrib.auth import views as auth_views
>>>>>>> 8e63f706690a8a255cbdf7dcb00b2165fa563487
from . import views

app_name = 'accounts'

urlpatterns = [
<<<<<<< HEAD
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
=======

    #path('signup/', views.signup, name='signup'),
    #path('login/', views.login_view, name='login'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
>>>>>>> 8e63f706690a8a255cbdf7dcb00b2165fa563487
]