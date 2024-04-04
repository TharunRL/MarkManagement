from django import forms
from .models import Department,Teacher,Classs,Student
from django.contrib.auth.forms import UserCreationForm

class AddDeptForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'
        
class AddTeacherForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=Teacher
        fields=['username','email','password1','password2','dept','phno']
        
class AddClassForm(forms.ModelForm):
    class Meta:
        model=Classs
        fields='__all__'
        
class AddStudentForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=Student
        fields=['username','rollno','email','password1','password2','class_sec','phno']