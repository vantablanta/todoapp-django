from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add_todo/', views.add_todo, name='add-todo'),
    path('view_todo/<str:pk>', views.view_todo, name='view-todo'),
    path('update_todo/<str:pk>', views.update_todo, name='update-todo'),
    path('assign_todo/<str:pk>/', views.assignTodo, name='assign-todo'),
    path('delete_todo/<str:pk>', views.delete_todo, name='delete-todo'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
]