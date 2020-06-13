# secondapp/urls.py
from django.urls import path
from . import views
app_name = "secondapp"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('static_exmaple/',views.static_exmaple, name="static_exmaple"),
]