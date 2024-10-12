from django.urls import path
from .views import productsingleView

urlpatterns = [
    path('product/<int:product_id>/', productsingleView, name='product_single'),
]
