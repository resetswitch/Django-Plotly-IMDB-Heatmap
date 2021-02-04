from django.urls import path, re_path

from . import views

# urlpatterns = [
#     # /pages
#     re_path(r'^plot1d/$', views.Plot1DView.as_view(), name='plot1d'),
#     #http://127.0.0.1:8001/app1/plot1d/
# ]

urlpatterns = [
    # /pages
    path('', views.HeatmapView.as_view(), name='heatmap'),
    #http://127.0.0.1:8001/app1/plot1d/
]