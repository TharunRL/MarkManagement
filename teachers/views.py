from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView,DeleteView

from .models import *
from .forms import AddDeptForm,AddClassForm,AddStudentForm,AddTeacherForm
from django.urls import reverse_lazy
# Create your views here.
class AddDeptView(CreateView):
    form_class=AddDeptForm
    success_url= reverse_lazy('department')
    template_name= 'manage/add.html'
    
class AddTeacherView(CreateView):
    form_class=AddTeacherForm
    success_url= reverse_lazy('home')
    template_name= 'manage/add.html'
    
class AddClassView(CreateView):
    form_class=AddClassForm
    success_url= reverse_lazy('home')
    template_name= 'manage/add.html'
    
class AddStudentView(CreateView):
    form_class=AddStudentForm
    success_url= reverse_lazy('home')
    template_name= 'manage/add.html'
    
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def manage(request):
    return render(request,'manage/manage.html')

class DeptView(ListView):
    model=Department
    template_name='manage/list.html'
    
class DeptDetailView(DetailView):
    model=Department
    template_name="manage/detail.html"
    
class DeptUpdateView(UpdateView):
    model=Department
    fields='__all__'
    template_name="manage/update.html"
    success_url= reverse_lazy('department')
    
class DeptDeleteView(DeleteView):
    model=Department
    template_name="manage/delete.html"
    success_url= reverse_lazy('department')
    
class StudView(ListView):
    model=Student
    template_name='manage/list.html'
    
class StudDetailView(DetailView):
    model=Student
    template_name="manage/detail.html"
    
class StudUpdateView(UpdateView):
    model=Student
    fields='__all__'
    template_name="manage/update.html"
    success_url= reverse_lazy('student')
    
class StudDeleteView(DeleteView):
    model=Student
    template_name="manage/delete.html"
    success_url= reverse_lazy('student')


class TeachView(ListView):
    model = Teacher
    template_name = 'manage/list.html'


class TeachDetailView(DetailView):
    model = Teacher
    template_name = "manage/detail.html"


class TeachUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    template_name = "manage/update.html"
    success_url = reverse_lazy('teacher')


class TeachDeleteView(DeleteView):
    model = Teacher
    template_name = "manage/delete.html"
    success_url = reverse_lazy('teacher')


class ClassView(ListView):
    model = Classs
    template_name = 'manage/list.html'


class ClassDetailView(DetailView):
    model = Classs
    template_name = "manage/detail.html"


class ClassUpdateView(UpdateView):
    model = Classs
    fields = '__all__'
    template_name = "manage/update.html"
    success_url = reverse_lazy('class')


class ClassDeleteView(DeleteView):
    model = Classs
    template_name = "manage/delete.html"
    success_url = reverse_lazy('class')