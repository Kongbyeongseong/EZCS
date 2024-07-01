from django.urls import path 
from . import views
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('searchPW/', views.searchPW, name='searchPW'),

]