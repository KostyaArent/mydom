from django.urls import path
from .views import (
    PersonalCabinetIndex, BaseView, ProfileDetailView,
    AppealListView, AppealDetailView, AppealCreateView
    )


app_name = 'residents'

urlpatterns = [
    path('lk/', PersonalCabinetIndex.as_view(), name='lk'),
    path('lk/owns/', BaseView.as_view(), name='owns'),
    path('lk/profile/', ProfileDetailView.as_view(), name='profile'),
    path('lk/appeals/', AppealListView.as_view(), name='appeal_list'),
    path('lk/appeals/add', AppealCreateView.as_view(), name='appeal_create'),
    path('lk/appeals/<int:pk>/', AppealDetailView.as_view(),  name='appeal_detail'),
]
