from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView,LogoutView
from . import views
urlpatterns = [
    path('',LoginView.as_view(),name="login_url"),
    path('dashboard/',views.dashboardView,name="dashboard "),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='login_url'),name="logout"),
    path('delete/<int:id>', views.delete),


]