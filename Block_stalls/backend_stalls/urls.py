from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('blocks/', views.blocks, name='blocks'),
    path('stalls/<int:block_id>/', views.stalls, name='stalls'),
]