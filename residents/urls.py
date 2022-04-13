from django.urls import path
from .views import lk, BaseView


app_name = 'residents'

urlpatterns = [
    path('lk/', lk, name='lk'),
    path('lk/profile/', BaseView.as_view(), name='profile'),

]
