from django.urls import path,include
from .views import *
#from . import views
app_name = "home"

urlpatterns = [
    path('', home, name='home'),
    # path('', HomeView.as_view(), name='index'),
]