from django.urls import path

from mainapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path("taskform/", views.createTask, name="taskForm"),
    path("update/<str:pk>/", views.updateTask, name="updateTask"),
    path("delete/<str:pk>/", views.deleteTask, name="deleteTask"),
    path("register/", views.register, name="register")
    path("login/", views.login, name="login")
]