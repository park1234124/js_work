from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student

# 학생등록페이지 호출
def regStudent(request):
    context ={'user_id':'공군출','user_pw':'150100'}
    stuStr = ['admin']
    return render(request,'reg.html',context)

# 학생등록저장후 list페이지 이동
def regCon(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    print("regCon views : ",name)
    
    # db에 저장
    qs = Student(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
    qs.save()
    
    return HttpResponseRedirect(reverse('students:reglist'))

# 학생리스트 페이지
def reglist(request):
    qs = Student.objects.all()
    #s_count = qs.count()
    context = {'stuList':qs}  # views->html dictionary형태로 보냄.
    return render(request,'reglist.html',context)

# 학생상세페이지
def regview(request,name,major):
    #name = request.GET.get('name')
    print("views request : ",name)
    print("views request : ",major)
    qs = Student.objects.get(s_name=name)
    context ={'stu':qs}
    return render(request,'regview.html',context)

# 학생정보수정페이지
def regmodify(request,name):
    qs = Student.objects.get(s_name=name)
    context={'stu':qs}
    return render(request,'regmodify.html',context)

#학생정보수정저장 후 학생리스트 페이지 이동
def regmodifyCon(request):
    
    name = request.POST.get('name')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    
    # db에 수정저장
    qs = Student.objects.get(s_name=name)
    qs.s_major=major
    qs.s_age=age
    qs.s_grade=grade
    qs.s_gender=gender
    qs.save()
    
    return HttpResponseRedirect(reverse('students:reglist'))

def regdelete(request,name):
    qs = Student.objects.get(s_name=name)
    qs.delete()
    
    
    return HttpResponseRedirect(reverse('students:reglist'))