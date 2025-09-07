from django.contrib import admin
from django.urls import path

from shop.models import Tshirt, Brand
from shop.views import HomePageListView

admin.site.register(Tshirt)
admin.site.register(Brand)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageListView.as_view(), name='home')
]
