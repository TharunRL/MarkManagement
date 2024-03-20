from django.urls import path
from .views import AddDeptView,AddTeacherView,AddClassView,AddStudentView,manage,DeptView,DeptDetailView
urlpatterns = [
    path('department/add/',AddDeptView.as_view(),name='add_department'),
    path('teacher/add/',AddTeacherView.as_view(),name='add_teacher'),
    path('class/add/',AddClassView.as_view(),name='add_class'),
    path('student/add/',AddStudentView.as_view(),name='add_student'),
    path('',manage,name='manage'),
    path('department/',DeptView.as_view(),name='department'),
    path('department/<int:pk>/',DeptDetailView.as_view(),name='dept_detail'),
]