from django.urls import path
from . import views

urlpatterns = [
    # /pages
    path('', views.HeatmapView.as_view(), name='plot'),
]