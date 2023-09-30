from django.urls import path 
from Testapp import views
urlpatterns = [
    path('GetDatabase/',views.Temp),
    path('RegForm/',views.RegForm),
]