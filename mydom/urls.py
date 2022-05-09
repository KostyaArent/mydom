from django.contrib import admin
from django.urls import path, include
from residents.views import SignInView


urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('signin/', SignInView.as_view(), name='signin'),

    # RESIDENTS APP
    path('residents/', include('residents.urls'), name='residents'),
]
