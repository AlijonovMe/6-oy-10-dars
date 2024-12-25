from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('course/<int:course_id>/', courses, name='courses_detail'),
    path('course/<int:course_id>/update/', updateCourse, name='updateCourse'),
    path('course/<int:course_id>/delete/', deleteCourse, name='deleteCourse'),
    path('lesson/<int:lesson_id>/', lessons, name='lessons_detail'),
    path('lesson/<int:lesson_id>/update/', updateLesson, name='updateLesson'),
    path('lesson/<int:lesson_id>/delete/', deleteLesson, name='deleteLesson'),
    path('course/add/', addCourse, name='addCourse'),
    path('lesson/add/', addLesson, name='addLesson')
]