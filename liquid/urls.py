
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from account.views import aboutView, accountView, blogView, blogsingleView, checkoutView, contactView, productView, productsingleView, register, socialbackenderView, user_login
from liquid import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accountView, name="index"),
    path('index', accountView, name="index"),
    path('about', aboutView, name="about"),
    path('blog', blogView, name="blog"),
    path('contact', contactView, name="contact"),
    path('product', productView, name="product"),
    path('product-single', productsingleView, name="product-single"),
    path('checkout', checkoutView, name="checkout"),
    path('social-backender', socialbackenderView, name="social-backender"),
    path('blog-single', blogsingleView, name="blog-single"),
    path('login/', user_login, name='login'),
    # path('', include('django.contrib.auth.urls')),
    path('register/',register, name='register'),
    path('cart/', include('cart.urls', namespace='cart')),
    


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
