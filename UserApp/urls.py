from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='user_dashboard'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
]
