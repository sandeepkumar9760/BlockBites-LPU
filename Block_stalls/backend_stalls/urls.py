from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('blocks/', views.blocks, name='blocks'),
    path('stalls/<int:block_id>/', views.stalls, name='stalls'),
    path('login/', views.login_view, name='login'),
    path('menu/<int:stall_id>/', views.menu, name='menu'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.order_success, name='order_success'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update-cart/<int:item_id>/<str:action>/', views.update_cart, name='update_cart'),
]