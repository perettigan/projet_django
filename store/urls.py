from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.listing),

    path('<int:album_id>/', views.detail),
    #re_path(r'^(?P<album_id>[0-9]+)/$', views.detail),
]