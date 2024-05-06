
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Department(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=55)
    hod=models.CharField(max_length=55)
    class Meta:
        db_table="department"
    def __str__(self) -> str:
        return self.name
    def getvalues(self):
        return list(vars(self).values())[2:]
    def update(self):
        return "dept_update"
    def delt(self):
        return "dept_delete"
    def detail(self):
        return "dept_detail"
    def add(self):
        return "dept_add"
    
class Teacher(User):
    dept=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    phno=models.IntegerField(unique=True)
    class Meta:
        db_table="teacher"
    
    def __str__(self) -> str:
        return self.username
    def getvalues(self):
        return list(vars(self).values())[2:]
    def update(self):
        return 'teacb_update'
    def delt(self):
        return 'teach_delete'
    def detail(self):
        return 'teach_detail'
    def add(self):
        return 'teach_add'
    
class Classs(models.Model):
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    sec=models.CharField(max_length=1,choices=[('A','A'),('B','B'),('C','C'),('D','D'),('E','E')])
    batch=models.IntegerField()
    class Meta:
        db_table="classs"
    def __str__(self) -> str:
        return self.dept.name +"-"+self.sec
    def getvalues(self):
        return list(vars(self).values())[2:]
    def update(self):
        return 'class_update'
    def delt(self):
        return 'class_delete'
    def detail(self):
        return 'class_detail'
    def add(self):
        return 'class_add'

class Student(User):
    rollno=models.IntegerField(primary_key=True)
    phno=models.CharField(max_length=12,unique=True)
    class_sec=models.ForeignKey(Classs,on_delete=models.SET_NULL,null=True)
    class Meta:
        db_table="student"
    def __str__(self) -> str:
        return self.username
    def getvalues(self):
        return list(vars(self).values())[2:]
    def update(self):
        return 'stud_update'
    def delt(self):
        return 'stud_delete'
    def detail(self):
        return 'stud_detail'
    def add(self):
        return 'stud_add'