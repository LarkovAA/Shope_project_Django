"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product import views as prod, urls
from authnapp import urls as urls_aupp
from baskets import urls as urls_bask
from admins import urls as urls_adm
from ordersapp import urls as urls_ord
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
import debug_toolbar


urlpatterns = [
    path('', prod.index, name='index'),
    path('admin/', admin.site.urls),
    path('products/', include(urls, namespace='products')),
    path('auth/', include(urls_aupp, namespace='auth')),
    path('baskets/', include(urls_bask, namespace='baskets')),
    path('admins/', include(urls_adm, namespace='admins')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('social_django.urls', namespace='social')),
    path('orders/', include(urls_ord, namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('debug/', include(debug_toolbar.urls))]

