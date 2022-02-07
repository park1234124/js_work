from django.shortcuts import render

# Create your views here.
def index(request):
    context={'user_id':'황근출','u_count':4588}
    return render(request,'index.html',context)