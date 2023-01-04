
from django.contrib import admin
from django.urls import path, include

#django.admin@gmail.com
#tarek
#django@1205

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('watchlist_app.api.urls')),
]
