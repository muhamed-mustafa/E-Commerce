from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
    path('product/',include('product.urls',namespace='products')),
    path('social-auth/',include('social_django.urls', namespace='social')),
    path('cart/',include('cart.urls',namespace='cart')),
    path('order/',include('orders.urls',namespace='orders')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

