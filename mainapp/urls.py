from django.urls import path

from mainapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("createtask/", views.createtask, name="createtask"),
    path("logout/", views.logout, name="logout"),
    path("viewtask/", views.viewtask, name="viewtask"),
    path("updatetask/<str:pk>/", views.updatetask, name="updatetask"),
    path("deletetask/<str:pk>/", views.deletetask, name="deletetask"),
]
