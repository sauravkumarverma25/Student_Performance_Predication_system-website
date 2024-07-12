from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('create_student_profile/', views.create_student_profile, name='create_student_profile'),
    path('upload_file/', views.teacher_dash, name='teacher_dash'),
    path('dash/', views.dash, name='dash'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('subject_wise_low_performers/<str:student_name>/', views.subject_wise_low_performers, name='subject_wise_low_performers'),
    path('teacher_signup', views.teacher_signup, name='teacher_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout1/', views.logout1, name='logout1'),
    path('student_signup', views.student_signup, name='student_signup'),
    path("input", views.input, name='input'),
    path("result", views.result, name='result'),

]
