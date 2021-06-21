from django.contrib import admin
from django.urls import path, include
import product.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product.views.home, name='home'),
    path('account/', include('account.urls')),
]
