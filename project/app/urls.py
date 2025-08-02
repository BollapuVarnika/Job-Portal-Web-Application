from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path("signup",views.signup),
    path("user_login",views.user_login),
    path("profile",views.profile),
    path("search_job",views.search_job),
    path("user_details",views.user_details),
    path('edit/<str:username>/', views.edit, name='edit')
]
