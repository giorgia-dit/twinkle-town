from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('town/', views.TownPageView.as_view(), name='town'),
    path('houses/', include([
        path('<slug:slug>/', views.HouseDetailView.as_view(), name='house_detail')
    ])),
    path('users/', views.UserListView.as_view(), name='users'),
    path('thanks/', views.ThanksPageView.as_view(), name='thanks')
]
