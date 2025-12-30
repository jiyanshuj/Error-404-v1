from django.urls import path
from . import views

urlpatterns = [
    path('', views.trip_view, name='trip_view'),
    path('booking/', views.final, name='booking'),
    path('forming/',views.payment,name='forming'),
    path('pay/',views.pay,name='pay'),
]