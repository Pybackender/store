from django.urls import path
from . import views
from django.views.generic import RedirectView 

app_name = 'cart'

urlpatterns = [
    
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    path('index/', RedirectView.as_view(url='/index', permanent=False)),
    path('product/', RedirectView.as_view(url='/product', permanent=False)),
    path('blog/', RedirectView.as_view(url='/blog', permanent=False)),
    path('about/', RedirectView.as_view(url='/about', permanent=False)),
    path('contact/', RedirectView.as_view(url='/contact', permanent=False)),
    path('login/', RedirectView.as_view(url='/login', permanent=False)),
    path('register/', RedirectView.as_view(url='/register', permanent=False)),
    path('cart/', RedirectView.as_view(url='/cart', permanent=False)),
    path('checkout/', RedirectView.as_view(url='/checkout', permanent=False)),
    path('product-single/', RedirectView.as_view(url='/product-single', permanent=False)),
]
