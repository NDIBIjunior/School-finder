from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.owner_dashboard, name='dashboard'),
    path('dashboard/add/', views.add_school, name='add_school'),
    path('dashboard/edit/<int:school_id>/', views.edit_school, name='edit_school'),
    path('dashboard/delete/<int:school_id>/', views.delete_school, name='delete_school'),
    path('login/', views.login_view, name='login'),

    path('school/<int:school_id>/levels/', views.list_level, name='list_levels'),
    path('school/<int:school_id>/levels/add/', views.add_level, name='add_level'),
    path('level/<int:level_id>/edit/', views.edit_level, name='edit_level'),

    path('school/<int:school_id>/exams/', views.list_exam, name='list_exam'),
    path('school/<int:school_id>/exams/add/', views.add_exam, name='add_exam'),
    path('exam/<int:exam_id>/edit/', views.edit_exam, name='edit_exam'),
]