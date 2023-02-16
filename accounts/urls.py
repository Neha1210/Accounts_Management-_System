from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.Home,name="home"),
    path("products",views.products,name="products"),
    path('customers<str:pk>',views.customer ,name="customers"),
    path('create_order<str:pk>',views.create_order,name="create_order"),
    path('update_order<str:pk>',views.update_order,name="update_order"),
    path('delete_order<str:pk>',views.delete_order,name="delete_order"),
    path('create_customer',views.create_customer,name="create_customer"),
    path('Add_product',views.Add_product,name="Add_product"),
    path('view_product<str:pk>',views.view_product,name="view_product"),
    path('update_customer<str:pk>',views.update_customer,name="update_customer"),
    path('registerpage',views.register,name="register"),
    path('loginpage',views.login,name="login")
]
