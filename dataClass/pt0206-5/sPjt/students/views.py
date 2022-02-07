from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from students.models import Student

# 학생등록페이지
def regStudent(request):
    return render(request,'reg.html')

# 학생저장 
def regStuCon(request):
    name = request.POST['name']
    print("views name : ",name)
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']
    
    qs = Student(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
    qs.save()
    
    return HttpResponseRedirect(reverse('index'))

# 학생전체리스트
def regStuAll(request):
    qs = Student.objects.all()
    context = {'stuList':qs}
    return render(request,'stuList.html',context)