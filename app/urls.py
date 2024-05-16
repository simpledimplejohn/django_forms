from django.urls import path
from . import views
from .views import potato_view

urlpatterns = [
    path("", views.index, name="index"),
    path('potato/',potato_view,name='potato')
]
