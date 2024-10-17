
from django.contrib import admin
from account.views import PasswordChangeView
from django.urls import include, path
from django.conf.urls.static import static
from account.views import aboutView, accountView, blogView, blogsingleView, checkoutView, contactView, faqView, productView, productsingleView, register, socialbackenderView, user_login
from liquid import settings
from django.contrib.auth import views as auth_views

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
    path('faq', faqView, name="faq"),
    path('cart/', include('cart.urls', namespace='cart')),
    # path('', include('django.contrib.auth.urls')),

    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
