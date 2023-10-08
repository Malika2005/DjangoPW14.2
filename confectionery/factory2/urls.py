from django.urls import path
from . import views

app_name = 'factory2'

urlpatterns = [
    path('', views.product_list, name='product_list2'),
    path('<int:pk>/', views.product_detail, name='product_detail2')
]