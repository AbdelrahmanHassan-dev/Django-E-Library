from django.urls import path
from . import views

urlpatterns=[
    path('about/',views.about,name="about"),
    path('contact/',views.contact, name="contact"),
    path('base/',views.base, name="base"),
    path('',views.home, name="Home"),
    path('search/',views.search, name = 'search'), 
    path('signup/', views.signup,name='signup'),
    # path('profile/<int:id>/',views.profile, name ='profile'),
    path('profile/',views.profile, name ='profile'),
]