from django.urls import path
from .views import lk, BaseView, ProfileDetailView


app_name = 'residents'

urlpatterns = [
    path('lk/', lk, name='lk'),
    path('lk/owns/', BaseView.as_view(), name='owns'),
    path('lk/profile/', ProfileDetailView.as_view(), name='profile'),

]
