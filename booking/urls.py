from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('services/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('reservation/',views.reservation,name='reservation'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('car_info',views.car_info,name='car_info'),
]
