from django.urls import path
from .views import (
    home, about, contact, 
    dashboard, signup, user_login, 
    user_logout, addpost, updatepost, 
    deletepost,postdetail
)
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add/', addpost, name='addpost'),
    path('update/<int:id>/', updatepost, name='updatepost'),
    path('delete/<int:id>/', deletepost, name='deletepost'),
    path('post/<int:id>/', postdetail, name='postdetail'),



]
