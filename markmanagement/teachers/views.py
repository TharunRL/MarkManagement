from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,DetailView

from teachers.models import Department
from .forms import AddDeptForm,AddClassForm,AddStudentForm,AddTeacherForm
from django.urls import reverse_lazy
# Create your views here.
class AddDeptView(CreateView):
    form_class=AddDeptForm
    success_url= reverse_lazy('home')
    template_name= 'manage/add_dept.html'
    
class AddTeacherView(CreateView):
    form_class=AddTeacherForm
    success_url= reverse_lazy('home')
    template_name= 'manage/add_teacher.html'
    
class AddClassView(CreateView):
    form_class=AddClassForm
    success_url= reverse_lazy('home')
    template_name= 'manage/add_class.html'
    
class AddStudentView(CreateView):
    form_class=AddStudentForm
    success_url= reverse_lazy('home')
    template_name= 'manage/add_student.html'
    
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def manage(request):
    return render(request,'manage/manage.html')

class DeptView(ListView):
    model=Department
    template_name='manage/department.html'
    
class DeptDetailView(DetailView):
    model=Department
    template_name="manage/dept-detail.html"