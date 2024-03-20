from django.urls import path
from .views import AddDeptView,AddTeacherView,AddClassView,AddStudentView, DeptUpdateView,manage,DeptView,DeptDetailView,DeptUpdateView,DeptDeleteView
from .views import StudView,StudUpdateView,StudDeleteView,StudDetailView
urlpatterns = [
    path('department/add/',AddDeptView.as_view(),name='add_department'),
    path('teacher/add/',AddTeacherView.as_view(),name='add_teacher'),
    path('class/add/',AddClassView.as_view(),name='add_class'),
    path('student/add/',AddStudentView.as_view(),name='add_student'),
    path('',manage,name='manage'),
    path('department/',DeptView.as_view(),name='department'),
    path('department/<int:pk>/',DeptDetailView.as_view(),name='dept_detail'),
    path('department/<int:pk>/update/',DeptUpdateView.as_view(),name='dept_update'),
    path('department/<int:pk>/delete/',DeptDeleteView.as_view(),name='dept_delete'),
    path('student/',StudView.as_view(),name='student'),
    path('student/<int:pk>/',StudDetailView.as_view(),name='stud_detail'),
    path('student/<int:pk>/update/',StudUpdateView.as_view(),name='stud_update'),
    path('student/<int:pk>/delete/',StudDeleteView.as_view(),name='stud_delete'),

]