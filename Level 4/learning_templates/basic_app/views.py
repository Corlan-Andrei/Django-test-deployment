from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':"hello worlds","number":100}
    return render(request,'basic_app/index.html',context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def info(request):
    return render(request,'basic_app/url_info.html')
