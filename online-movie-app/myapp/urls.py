from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name="home"),
    path('<id>/home',views.h,name='home'),
    path('acconts/',include('django.contrib.auth.urls')),
    path('acconts/logout',include('django.contrib.auth.urls')),
    path('profile',views.profile,name="profile"),
    path('<id>/profile',views.pro,name="profile"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('<id>/editprofile',views.editpro,name="editprofile"),
    path('search',views.search,name='search'),
    path('<id>/search',views.searchres,name='search'),
    path('searchform',views.searchform,name='searchform'),
    path('<id>/searchform',views.searchform1,name='searchform'),
    path('movieview/<id>',views.movieview,name='movieview'),
    path('fullmovieview/<id>',views.fullmovieview,name='fullmovieview'),
    path('fulltrailerview/<id>',views.fulltrailerview,name='fulltrailerview'),
]

