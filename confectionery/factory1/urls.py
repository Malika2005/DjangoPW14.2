from django.urls import path
from . import views

app_name = 'factory1'

urlpatterns = [
    path('', views.product_list, name='product_list1'),
    path('<int:pk>/', views.product_detail, name='product_detail1')
]