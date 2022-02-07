from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'user_id':'dfa','nickName':'파크동현'}
    #   count='2day' -> 변수 count전송시킴
    return render(request,'index.html',context)