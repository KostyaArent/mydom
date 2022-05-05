from django.urls import path
from .views import (
    lk, BaseView, ProfileDetailView,
    AppealListView, AppealDetailView
    )


app_name = 'residents'

urlpatterns = [
    path('lk/', lk, name='lk'),
    path('lk/owns/', BaseView.as_view(), name='owns'),
    path('lk/profile/', ProfileDetailView.as_view(), name='profile'),
    path('lk/appeals/', AppealListView.as_view(), name='appeal_list'),
    path('lk/appeals/<int:pk>/', AppealDetailView.as_view(),  name='appeal_detail'),
]
