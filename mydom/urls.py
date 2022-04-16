from django.contrib import admin
from django.urls import path, include
from residents.views import signin


urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('signin/', signin, name='signin'),

    # RESIDENTS APP
    path('residents/', include('residents.urls'), name='residents'),
]
